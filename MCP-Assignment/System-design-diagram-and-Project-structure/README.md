# Project structure

---

Project/
├── server.py # the whole MCP server (1 resource, 2 tools, 1 prompt)
└── System-design-diagram-and-Project-structure/
├── Connector created successfully.png
|.....
└── Claude successfully pushed file to GITHUB.png

What each part does

server.py contains everything:

- wikipedia_page (resource) fetches the page text from Wikipedia.
- create_story_md (tool) writes the story to stories/Topic.md.
- push_to_github (tool) uploads that file to your repo.
- wiki_story (prompt) is the template you select to start the flow.

stories/ is the local copy of every story. GitHub gets the same files in its own stories/ folder.
.venv/ is the virtual environment with fastmcp, requests, python-dotenv and pydantic installed. It is not part of the project logic.

Claude Desktop's own claude_desktop_config.json sits outside this folder. It only tells Claude how to start server.py.
