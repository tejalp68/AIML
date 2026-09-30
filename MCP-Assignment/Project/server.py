
"""
Wikipedia -> Story MCP Server
==============================

Implements the pipeline:

  1. User sends message with Wikipedia URL -> "Generate a story from this"
  2. Backend extracts URL from message
  3. Backend calls Wikipedia API -> gets clean article text
  4. Backend sends article text + system prompt to Claude API -> gets story text back
  5. Backend renders story text -> PDF (via weasyprint) -> saves to /storage/pdfs/
  6. Backend inserts row into SQL DB: {url, topic, story_text, pdf_path, timestamp}
  7. Backend returns PDF (or confirmation + link) to the user

...as exactly THREE MCP primitives:

  TOOL      generate_story_from_url   -> does steps 2-7. An action with side
                                         effects (network calls, file write,
                                         DB write). The model decides to call
                                         this mid-conversation when the user
                                         asks it to turn a Wikipedia URL into
                                         a story.

  RESOURCE  stories://recent          -> passive, addressable data. No side
            stories://{story_id}         effects. Lets a client pull past
                                         generated stories into context
                                         (e.g. "what did we generate earlier?").

  PROMPT    story_writing_style       -> a reusable instruction template with
                                         a `style` argument (fairy_tale, noir,
                                         sci_fi, epic_poem, ...) that a PERSON
                                         picks on purpose before asking for a
                                         story, rather than something the
                                         model decides on its own.

Run:
    python server.py

Requires env var ANTHROPIC_API_KEY for the Claude API call in the tool.
"""

import os
import re
import sqlite3
import uuid
from datetime import datetime, timezone
from pathlib import Path

import requests
from dotenv import load_dotenv
from fastmcp import FastMCP
from weasyprint import HTML

load_dotenv()

# ---------------------------------------------------------------------------
# Paths / storage
# ---------------------------------------------------------------------------

BASE_DIR = Path(__file__).parent
STORAGE_DIR = BASE_DIR / "storage"
PDF_DIR = STORAGE_DIR / "pdfs"
DB_PATH = STORAGE_DIR / "stories.db"

PDF_DIR.mkdir(parents=True, exist_ok=True)


def get_db() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS stories (
            id         TEXT PRIMARY KEY,
            url        TEXT NOT NULL,
            topic      TEXT NOT NULL,
            story_text TEXT NOT NULL,
            pdf_path   TEXT NOT NULL,
            timestamp  TEXT NOT NULL
        )
        """
    )
    conn.commit()
    return conn


# ---------------------------------------------------------------------------
# Step-level helper functions (pure plumbing, not primitives themselves)
# ---------------------------------------------------------------------------

WIKIPEDIA_URL_RE = re.compile(
    r"https?://(?:[a-z]{2,3}\.)?wikipedia\.org/wiki/([^\s#?]+)", re.IGNORECASE
)


def extract_wikipedia_title(text_or_url: str) -> str:
    """Step 2: extract the article title from a URL (or raw title) the user gave us."""
    match = WIKIPEDIA_URL_RE.search(text_or_url)
    if match:
        raw_title = match.group(1)
    else:
        # Allow callers to pass a bare title too.
        raw_title = text_or_url.strip().replace(" ", "_")
    from urllib.parse import unquote

    return unquote(raw_title).replace("_", " ")


def fetch_wikipedia_article(title: str) -> dict:
    """Step 3: call the Wikipedia API and return clean article text + metadata."""
    resp = requests.get(
        "https://en.wikipedia.org/w/api.php",
        params={
            "action": "query",
            "prop": "extracts",
            "explaintext": 1,
            "titles": title,
            "format": "json",
            "redirects": 1,
        },
        headers={"User-Agent": "wiki-story-mcp/1.0"},
        timeout=15,
    )
    resp.raise_for_status()
    pages = resp.json().get("query", {}).get("pages", {})
    if not pages:
        raise ValueError(f"No Wikipedia page found for '{title}'")

    page = next(iter(pages.values()))
    if "missing" in page:
        raise ValueError(f"Wikipedia page '{title}' does not exist")

    extract = page.get("extract", "").strip()
    if not extract:
        raise ValueError(f"Wikipedia page '{title}' has no extractable text")

    return {"topic": page.get("title", title), "text": extract}


def generate_story_with_claude(topic: str, article_text: str, style: str = "adventure") -> str:
    """Step 4: send article text + system prompt to the Claude API, get story text."""
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise RuntimeError("ANTHROPIC_API_KEY is not set")

    # Truncate very long articles so we stay within a reasonable context budget.
    trimmed = article_text[:12000]

    system_prompt = (
        f"You are a skilled creative writer. You will be given factual "
        f"reference material extracted from Wikipedia. Write an engaging, "
        f"original short story (roughly 500-900 words) in a {style} style "
        f"that is inspired by and factually consistent with this material. "
        f"Do not just summarize the article -- write an actual narrative "
        f"with characters, scenes, and a clear arc. Do not reproduce "
        f"Wikipedia's wording verbatim; this must be original prose."
    )

    resp = requests.post(
        "https://api.anthropic.com/v1/messages",
        headers={
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json",
        },
        json={
            "model": "claude-sonnet-4-6",
            "max_tokens": 2000,
            "system": system_prompt,
            "messages": [
                {
                    "role": "user",
                    "content": f"Topic: {topic}\n\nReference material:\n{trimmed}",
                }
            ],
        },
        timeout=60,
    )
    resp.raise_for_status()
    data = resp.json()
    return "".join(block.get("text", "") for block in data.get("content", []))


def render_story_to_pdf(topic: str, story_text: str, story_id: str) -> Path:
    """Step 5: render story text to PDF via weasyprint, save to storage/pdfs/."""
    paragraphs = "".join(f"<p>{p.strip()}</p>" for p in story_text.split("\n") if p.strip())
    html = f"""
    <html>
      <head>
        <meta charset="utf-8">
        <style>
          body {{ font-family: Georgia, serif; margin: 2.5cm; line-height: 1.6; }}
          h1 {{ font-size: 22pt; margin-bottom: 0.2em; }}
          p {{ font-size: 12pt; text-align: justify; margin: 0 0 1em 0; }}
        </style>
      </head>
      <body>
        <h1>{topic}</h1>
        {paragraphs}
      </body>
    </html>
    """
    pdf_path = PDF_DIR / f"{story_id}.pdf"
    HTML(string=html).write_pdf(str(pdf_path))
    return pdf_path


def save_story_record(url: str, topic: str, story_text: str, pdf_path: Path) -> dict:
    """Step 6: insert a row into the SQL DB."""
    story_id = str(uuid.uuid4())
    timestamp = datetime.now(timezone.utc).isoformat()
    conn = get_db()
    conn.execute(
        "INSERT INTO stories (id, url, topic, story_text, pdf_path, timestamp) "
        "VALUES (?, ?, ?, ?, ?, ?)",
        (story_id, url, topic, story_text, str(pdf_path), timestamp),
    )
    conn.commit()
    conn.close()
    return {
        "id": story_id,
        "url": url,
        "topic": topic,
        "pdf_path": str(pdf_path),
        "timestamp": timestamp,
    }


# ---------------------------------------------------------------------------
# MCP server + the exactly-three primitives
# ---------------------------------------------------------------------------

mcp = FastMCP("wiki-story-mcp")


# ============================== 1. TOOL ====================================
# An action: takes input, does side-effecting work, returns a result.
# This is what the model calls mid-conversation when the user says
# "generate a story from this [Wikipedia URL]".

@mcp.tool
def generate_story_from_url(url: str, style: str = "adventure") -> dict:
    """
    Generate an original short story from a Wikipedia article and save it as a PDF.

    Runs the full pipeline: extract the article title from the URL, fetch clean
    article text from the Wikipedia API, ask Claude to write a story from it,
    render the story to a PDF, and log the result in the database.

    Args:
        url: A Wikipedia article URL (e.g. https://en.wikipedia.org/wiki/Roman_Empire).
        style: Narrative style to write in, e.g. "adventure", "fairy_tale",
            "noir", "sci_fi", "epic_poem". Defaults to "adventure". A caller
            can also pass the `story_writing_style` prompt's rendered text here.

    Returns:
        dict with story id, topic, a short preview of the story, the pdf path,
        and the timestamp it was generated -- i.e. a confirmation + link.
    """
    title = extract_wikipedia_title(url)
    article = fetch_wikipedia_article(title)
    story_text = generate_story_with_claude(article["topic"], article["text"], style=style)

    # Reserve an id early so the PDF filename matches the DB row.
    story_id = str(uuid.uuid4())
    pdf_path = render_story_to_pdf(article["topic"], story_text, story_id)

    timestamp = datetime.now(timezone.utc).isoformat()
    conn = get_db()
    conn.execute(
        "INSERT INTO stories (id, url, topic, story_text, pdf_path, timestamp) "
        "VALUES (?, ?, ?, ?, ?, ?)",
        (story_id, url, article["topic"], story_text, str(pdf_path), timestamp),
    )
    conn.commit()
    conn.close()

    return {
        "story_id": story_id,
        "topic": article["topic"],
        "style": style,
        "story_preview": story_text[:280] + ("..." if len(story_text) > 280 else ""),
        "pdf_path": str(pdf_path),
        "timestamp": timestamp,
    }


# ============================= 2. RESOURCE ==================================
# Addressable data, no side effects. The client pulls this into context;
# the model doesn't "call" it as an action the way it calls the tool.

@mcp.resource("stories://recent")
def recent_stories() -> list[dict]:
    """The 20 most recently generated stories (metadata only, no full text)."""
    conn = get_db()
    rows = conn.execute(
        "SELECT id, url, topic, pdf_path, timestamp FROM stories "
        "ORDER BY timestamp DESC LIMIT 20"
    ).fetchall()
    conn.close()
    return [dict(row) for row in rows]


@mcp.resource("stories://{story_id}")
def story_by_id(story_id: str) -> dict:
    """Full record for a single generated story, including the story text."""
    conn = get_db()
    row = conn.execute(
        "SELECT id, url, topic, story_text, pdf_path, timestamp FROM stories WHERE id = ?",
        (story_id,),
    ).fetchone()
    conn.close()
    if row is None:
        raise ValueError(f"No story found with id '{story_id}'")
    return dict(row)


# ============================== 3. PROMPT ===================================
# A reusable instruction template a PERSON selects on purpose (e.g. from a
# client's prompt picker) before generating a story -- not something the
# model reaches for unprompted.

STYLE_GUIDES = {
    "fairy_tale": "Write in the voice of a classic fairy tale: 'Once upon a time...', "
                  "a clear moral, gentle magic, and a satisfying resolution.",
    "noir": "Write in hardboiled noir style: cynical first-person narration, "
            "shadows and moral ambiguity, clipped sentences, a sense of foreboding.",
    "sci_fi": "Write as speculative science fiction: extrapolate the subject "
              "matter into a future or alternate-technology setting.",
    "epic_poem": "Write as an epic narrative poem in free verse, with heightened, "
                 "rhythmic language and a heroic tone.",
    "adventure": "Write as a fast-paced adventure story with vivid action, "
                 "a clear protagonist, and rising stakes.",
}


@mcp.prompt
def story_writing_style(style: str = "adventure") -> str:
    """
    Pick a narrative style for the next Wikipedia-to-story generation.

    Args:
        style: One of "adventure", "fairy_tale", "noir", "sci_fi", "epic_poem".
    """
    guide = STYLE_GUIDES.get(style, STYLE_GUIDES["adventure"])
    return (
        f"When generating the next story from a Wikipedia article, use the "
        f"following style: {guide} Keep the story grounded in the real facts "
        f"from the source article while fully committing to this style."
    )


# ---------------------------------------------------------------------------

if __name__ == "__main__":
    mcp.run()