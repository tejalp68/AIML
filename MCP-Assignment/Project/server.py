import base64
import os
import re
from typing import Annotated

import requests
from dotenv import load_dotenv
from pydantic import Field
from fastmcp import FastMCP

load_dotenv()

mcp = FastMCP("wiki-story")
STORY_FOLDER = os.path.join(os.path.dirname(__file__), "stories")
os.makedirs(STORY_FOLDER, exist_ok=True)

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
GITHUB_REPO = os.environ.get("GITHUB_REPO")


# RESOURCE: read-only data, no side effects
@mcp.resource("wikipedia://{topic}")
def wikipedia_page(topic: str) -> str:
    """The plain text of a Wikipedia page. Use underscores for spaces,
    e.g. wikipedia://Eiffel_Tower"""
    title = topic.replace("_", " ")
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
    return f"Title: {page['title']}\nURL: {url}\n\n{page['extract'][:6000]}"


# TOOL 1: save the story as a markdown file
@mcp.tool()
def create_story_md(
    topic: Annotated[str, Field(description="Topic of the story, e.g. 'Eiffel Tower'. Used as the file name.")],
    story: Annotated[str, Field(description="The full story you wrote, based on the Wikipedia text")],
    wikipedia_url: Annotated[str, Field(description="The Wikipedia URL the story is based on")],
) -> str:
    """Create a markdown (.md) file named after the topic, containing the story and
    the Wikipedia source URL. Returns the file name to use with push_to_github."""
    content = f"# {topic}\n\n{story}\n\n---\n\nSource: {wikipedia_url}\n"

    filename = re.sub(r"[^a-zA-Z0-9]+", "_", topic).strip("_") + ".md"
    with open(os.path.join(STORY_FOLDER, filename), "w", encoding="utf-8") as f:
        f.write(content)

    return f"Story saved: {filename}"


# TOOL 2: push the markdown file to GitHub
@mcp.tool()
def push_to_github(
    filename: Annotated[str, Field(description="Name of the markdown file created earlier, e.g. 'Eiffel_Tower.md'")],
) -> str:
    """Push a story markdown file to the 'stories' folder in the configured GitHub repo.
    Call this after create_story_md."""
    if not GITHUB_TOKEN or not GITHUB_REPO:
        return "GitHub is not configured. Set GITHUB_TOKEN and GITHUB_REPO in your .env file."

    path = os.path.join(STORY_FOLDER, filename)
    if not os.path.exists(path):
        return f"File '{filename}' not found. Create the story first."

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


# PROMPT: a reusable template the person picks on purpose
@mcp.prompt()
def wiki_story(topic: str) -> str:
    """Turn a Wikipedia topic into a short story saved as a markdown file on GitHub."""
    return (
        f"Read the Wikipedia page for '{topic}' from the resource "
        f"wikipedia://{topic.replace(' ', '_')}. Write a short, creative story "
        "that stays true to the facts on that page. Then call create_story_md "
        "with the topic, the story, and the Wikipedia URL from the page, "
        "and finally call push_to_github with the returned file name."
    )


if __name__ == "__main__":
    mcp.run()