import base64
import os
import re
from typing import Annotated
from urllib.parse import unquote

import requests
from dotenv import load_dotenv
from fpdf import FPDF
from pydantic import Field
from mcp.server import MCPServer

load_dotenv()

mcp = MCPServer("wiki-story")
PDF_FOLDER = os.path.join(os.path.dirname(__file__), "stories")
os.makedirs(PDF_FOLDER, exist_ok=True)

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
GITHUB_REPO = os.environ.get("GITHUB_REPO")


def _clean(text):
    # The built-in PDF font only supports basic characters, so replace the rest
    return text.encode("latin-1", "replace").decode("latin-1")


@mcp.tool()
def fetch_wikipedia(
    topic_or_url: Annotated[str, Field(description="A topic like 'Eiffel Tower' or a full Wikipedia URL")],
) -> str:
    """Fetch the text of a Wikipedia page. Use this first, then write a creative
    story based on the returned text. Always keep the returned URL so it can be
    passed to create_story_pdf later."""
    if "wikipedia.org/wiki/" in topic_or_url:
        title = unquote(topic_or_url.split("/wiki/")[-1])
    else:
        title = topic_or_url

    resp = requests.get(
        "https://en.wikipedia.org/w/api.php",
        params={
            "action": "query",
            "prop": "extracts",
            "explaintext": 1,
            "titles": title,
            "redirects": 1,
            "format": "json",
        },
        headers={"User-Agent": "wiki-story-mcp/1.0"},
    )
    if resp.status_code != 200:
        return f"Wikipedia request failed ({resp.status_code})"

    page = next(iter(resp.json()["query"]["pages"].values()))
    if "missing" in page or not page.get("extract"):
        return f"No Wikipedia page found for '{title}'"

    url = "https://en.wikipedia.org/wiki/" + page["title"].replace(" ", "_")
    text = page["extract"][:6000]  # keep it short enough to read easily
    return f"Title: {page['title']}\nURL: {url}\n\n{text}"


@mcp.tool()
def create_story_pdf(
    title: Annotated[str, Field(description="Topic of the story, e.g. 'Eiffel Tower'")],
    story: Annotated[str, Field(description="The full story you wrote, based on the Wikipedia text")],
    wikipedia_url: Annotated[str, Field(description="The Wikipedia URL the story is based on")],
) -> str:
    """Create a PDF containing the story title, the story, and the Wikipedia source URL.
    Call this after writing the story. Returns the PDF filename."""
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Helvetica", "B", 20)
    pdf.multi_cell(0, 10, _clean(title), new_x="LMARGIN", new_y="NEXT")
    pdf.ln(5)

    pdf.set_font("Helvetica", "", 12)
    pdf.multi_cell(0, 8, _clean(story), new_x="LMARGIN", new_y="NEXT")
    pdf.ln(8)

    pdf.set_font("Helvetica", "I", 10)
    pdf.multi_cell(0, 6, _clean(f"Source: {wikipedia_url}"), new_x="LMARGIN", new_y="NEXT")

    filename = re.sub(r"[^a-zA-Z0-9]+", "_", title).strip("_").lower() + ".pdf"
    pdf.output(os.path.join(PDF_FOLDER, filename))
    return f"PDF created: {filename}"


@mcp.tool()
def push_to_github(
    filename: Annotated[str, Field(description="Name of the PDF created earlier, e.g. 'eiffel_tower.pdf'")],
) -> str:
    """Push a story PDF to the 'stories' folder in the configured GitHub repo."""
    if not GITHUB_TOKEN or not GITHUB_REPO:
        return "GitHub is not configured. Set GITHUB_TOKEN and GITHUB_REPO in your .env file."

    path = os.path.join(PDF_FOLDER, filename)
    if not os.path.exists(path):
        return f"File '{filename}' not found. Create the PDF first."

    with open(path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()

    url = f"https://api.github.com/repos/{GITHUB_REPO}/contents/stories/{filename}"
    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json",
    }

    existing = requests.get(url, headers=headers)
    sha = existing.json().get("sha") if existing.status_code == 200 else None

    payload = {"message": f"add {filename}", "content": encoded}
    if sha:
        payload["sha"] = sha

    resp = requests.put(url, headers=headers, json=payload)
    if resp.status_code in (200, 201):
        return f"Pushed to {GITHUB_REPO}/stories/{filename}"
    return f"Failed ({resp.status_code}): {resp.text}"


@mcp.prompt()
def wiki_story(topic: str) -> str:
    """Reusable prompt template to turn a Wikipedia topic into a story PDF on GitHub."""
    return (
        f"Fetch the Wikipedia page for '{topic}', write a short creative story "
        "based on its facts, save it as a PDF with the Wikipedia URL, "
        "and push the PDF to GitHub."
    )


if __name__ == "__main__":
    mcp.run()