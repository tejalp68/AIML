# Wiki Story: Turning Wikipedia into Stories

An MCP (Model Context Protocol) server that lets an AI agent take any Wikipedia topic and turn it into an interesting, easy-to-read story, then save it as a Markdown file and push it to GitHub.

---

## How It All Started

I'm currently doing an AI/ML course where my instructor is teaching me about LLMs. As part of the course, he gave us an assignment: **build our own MCP server**.

Around that time, he told us a story about an incident involving Hugging Face and OpenAI, and encouraged us to read more about it on the internet. So I went home and searched for it. I landed on Wikipedia and started reading.

But after a few minutes, I gave up. The page was full of long, dense text. It was dry, hard to follow, and honestly boring. I wanted to understand the incident, but the way the information was presented made it really difficult.

That's when a thought struck me:

> *Why don't I build an AI agent that converts Wikipedia topics into interesting stories?*

That idea became this project. I built it for my assignment, with Claude doing the heavy lifting of turning information into storytelling.

---

## What This Project Does

1. You give the agent a topic (for example, a historical event, a person, or a scientific concept).
2. The agent reads the relevant information from Wikipedia.
3. Claude rewrites that information as an engaging story, keeping the facts intact but making it far easier and more enjoyable to read.
4. The story is saved as a Markdown (`.md`) file named after the topic.
5. The file can be pushed to a GitHub repository, into a `stories` folder.

---

## What's Included

| Component | Description |
|-----------|-------------|
| MCP server | The core of the project, exposing tools that Claude can call |
| `create_story_md` | Creates a Markdown file named after the topic, containing the story |
| `push_to_github` | Pushes the story file to the `stories` folder of a configured GitHub repo |
| Claude (the AI agent) | Does the actual work: reading the topic and writing the story |

---

## Tech Stack

- **Python** *(update if different)*
- **MCP (Model Context Protocol)**
- **Claude** as the AI agent
- **Wikipedia** as the knowledge source
- **GitHub** for storing the generated stories

---

## Getting Started

### Prerequisites

- Python 3.10+ *(update if different)*
- A GitHub account and a repository to store the stories
- A GitHub personal access token
- Claude Desktop (or another MCP-compatible client)

### Installation

```bash
git clone <your-repo-url>
cd <your-project-folder>
pip install -r requirements.txt
```

### Configuration

Add your GitHub details (token, repository name) to your environment or config file:

```bash
GITHUB_TOKEN=your_token_here
GITHUB_REPO=your-username/your-repo
```

Then register the server in your MCP client's config so Claude can connect to it.

### Usage

Once the server is connected, just ask Claude something like:

> "Turn the Wikipedia article on *[topic]* into a story and push it to GitHub."

Claude will fetch the information, write the story, create the Markdown file, and push it to your repo.

---

## Example

**Before (Wikipedia):** long, dense paragraphs packed with dates and names.

**After (Wiki Story):** the same facts, told as a story with a beginning, a build-up, and a payoff, so you actually want to keep reading.

---

## What I Learned

- How MCP servers work and how they give an LLM real tools to use
- How to connect an AI agent to external services like Wikipedia and GitHub
- That a good idea can start with a small frustration, in this case a boring Wikipedia page

---
