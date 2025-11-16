# MAI Advisor - Deployment Guide

## Dual Deployment: HuggingFace Space + MCP Server

This app is designed to run in two modes:

1. **HuggingFace Space**: Web-based Gradio interface
2. **MCP Server**: Model Context Protocol server for Claude Desktop/other MCP clients

---

## Option 1: HuggingFace Space Deployment

### Requirements

Create a `README.md` file with HuggingFace Space frontmatter:

```markdown
---
title: MAI Advisor - Grant Planning System
emoji: 🎯
colorFrom: blue
colorTo: green
sdk: gradio
sdk_version: 5.49.1
app_file: app_workflow.py
pinned: false
license: mit
tags:
  - mcp-in-action-track-enterprise
  - grant-planning
  - ai-assistant
  - nonprofit
short_description: AI-powered grant planning system with strategic frameworks and browser agent support
---
```

### Files Needed

- `app_workflow.py` - Main Gradio application
- `requirements.txt` - Python dependencies
- `src/` directory - All source files
- Agent instructions and output directories (created automatically)

### Deploy to HuggingFace

1. Create new Space on HuggingFace
2. Select "Gradio" as SDK
3. Upload all files
4. Space will auto-launch at `https://huggingface.co/spaces/YOUR_USERNAME/mai-advisor`

---

## Option 2: MCP Server Deployment

### For Claude Desktop Integration

**Step 1**: Create MCP server file (`src/server_mcp.py`):

```python
"""MCP Server for MAI Advisor - Grant Planning System."""
import asyncio
from typing import Any, Sequence
from dotenv import load_dotenv

from mcp.server import Server
from mcp.types import (
    Resource,
    Tool,
    TextContent,
    ImageContent,
    EmbeddedResource,
)
from pydantic import AnyUrl

# Import our workflow functions
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from dork_generator import GrantDorkGenerator
from output_manager import output_manager

# Load environment variables
load_dotenv()

# Initialize MCP server
app = Server("mai-advisor")


@app.list_tools()
async def list_tools() -> list[Tool]:
    """List available MCP tools."""
    return [
        Tool(
            name="generate_grant_strategy",
            description="Generate complete grant planning strategy including dorks, expert frameworks, and AI agent instructions",
            inputSchema={
                "type": "object",
                "properties": {
                    "topic": {
                        "type": "string",
                        "description": "Grant topic/focus area (e.g., 'community health initiative')"
                    },
                    "location": {
                        "type": "string",
                        "description": "Geographic location (optional, e.g., 'Phoenix, Arizona')"
                    }
                },
                "required": ["topic"]
            }
        ),
        Tool(
            name="generate_search_dorks",
            description="Generate optimized search queries for Google, Bing, and DuckDuckGo",
            inputSchema={
                "type": "object",
                "properties": {
                    "topic": {"type": "string"},
                    "location": {"type": "string"}
                },
                "required": ["topic"]
            }
        )
    ]


@app.call_tool()
async def call_tool(name: str, arguments: Any) -> Sequence[TextContent]:
    """Handle tool calls."""
    if name == "generate_search_dorks":
        topic = arguments["topic"]
        location = arguments.get("location")
        
        dorks = GrantDorkGenerator.generate_all_dorks(
            topic=topic,
            location=location if location else None
        )
        
        result = f"""# Search Engine Dorks for: {topic}

## Google
```
{dorks['google']}
```

## Bing
```
{dorks['bing']}
```

## DuckDuckGo
```
{dorks['duckduckgo']}
```

Copy these queries and paste them into the respective search engines to find grant opportunities.
"""
        
        return [TextContent(type="text", text=result)]
    
    elif name == "generate_grant_strategy":
        topic = arguments["topic"]
        location = arguments.get("location", "")
        
        # Run the full workflow (imported from app_workflow)
        from app_workflow import run_complete_workflow
        
        result = run_complete_workflow(topic, location)
        
        status_msg = f"""# Grant Strategy Generated Successfully

**Topic:** {topic}
**Location:** {location or "Not specified"}

## Files Created:

- `grant_dorks/` - Search engine queries
- `advisors_output/` - 3 expert strategic frameworks
- `orchestrator_output/` - Comprehensive grant plan
- `agent-instructions/` - AI browser agent task list

All files have been saved with timestamps. Use the file viewing tabs in the Gradio interface or check the output directories directly.

**Next Step:** Provide the `agent-instructions/agent-todo.*.md` file to your AI assistant with browser capabilities to begin discovering and applying for grants.
"""
        
        return [TextContent(type="text", text=status_msg)]
    
    raise ValueError(f"Unknown tool: {name}")


@app.list_resources()
async def list_resources() -> list[Resource]:
    """List available resources."""
    return [
        Resource(
            uri=AnyUrl("mai://guide/getting-started"),
            name="MAI Advisor Getting Started Guide",
            mimeType="text/markdown",
            description="Introduction to the grant planning system"
        ),
        Resource(
            uri=AnyUrl("mai://guide/ai-agent-integration"),
            name="AI Agent Integration Guide",
            mimeType="text/markdown",
            description="How to use agent-todo.md with AI browser agents"
        )
    ]


@app.read_resource()
async def read_resource(uri: AnyUrl) -> str:
    """Read resource content."""
    uri_str = str(uri)
    
    if uri_str == "mai://guide/getting-started":
        return """# MAI Advisor - Getting Started

## Overview

MAI Advisor is a comprehensive grant planning system that generates:

1. **Search Engine Dorks** - Optimized queries for finding grants
2. **Expert Strategic Frameworks** - Financial, grant writing, and research guidance
3. **Comprehensive Grant Plan** - Synthesized strategic roadmap
4. **AI Agent Instructions** - Task list for browser-enabled AI assistants

## Quick Start

Use the `generate_grant_strategy` tool with:
- **topic**: Your grant focus area (required)
- **location**: Geographic location (optional)

Example:
```json
{
  "topic": "youth STEM education program",
  "location": "Seattle, Washington"
}
```

The system will generate all four output types and save them to organized directories.

## Understanding the Outputs

**grant_dorks/** - Copy-paste search queries into Google, Bing, DuckDuckGo

**advisors_output/** - Read these for strategic guidance:
- financial.*.md - Budget planning, fiscal management
- grant.*.md - Proposal development, funder relationships
- research.*.md - Evidence-based design, evaluation

**orchestrator_output/** - Your comprehensive strategic roadmap

**agent-instructions/** - Give this to your AI assistant for automated grant discovery and application support

## For MCP Clients

This server integrates with:
- Claude Desktop
- Cursor
- Cline
- Any MCP-compatible client

The tools appear in your client's tool list and can be invoked during conversations.
"""
    
    elif uri_str == "mai://guide/ai-agent-integration":
        return """# AI Agent Integration Guide

## Using agent-todo.md with AI Browser Agents

The `agent-instructions/agent-todo.*.md` file contains comprehensive instructions for AI agents with browser capabilities.

## Prerequisites

Your AI assistant needs:
- Browser automation (navigate websites, fill forms, click buttons)
- Document reading and generation
- File management (upload/download)
- Multi-step task execution

## Compatible AI Frameworks (2025+)

- **Playwright** + LLM - Browser automation with AI
- **LangChain Agents** - Multi-tool orchestration
- **AutoGPT-style systems** - Autonomous task execution
- **Custom implementations** - Using libraries like Selenium, Puppeteer

## How to Use

1. **Locate the file**: `agent-instructions/agent-todo.{timestamp}.md`

2. **Provide to AI agent**: Upload or paste the entire content

3. **AI agent will**:
   - Execute search dorks across search engines
   - Discover 15-25 grant opportunities
   - Gather your organizational information
   - Help complete grant applications
   - Submit applications (with your approval)
   - Manage post-submission tracking

## Expected Workflow

**Week 1-2**: Quick-win grants (LOI only, rolling deadlines)
**Week 3-6**: High-priority applications (strong alignment)
**Week 7-12**: Medium-priority + relationship cultivation

**Goal**: 10-15 submitted applications in 90 days

## Important Reminders

⚠️ **AI agent should ALWAYS get your approval before**:
- Submitting any application
- Sending emails to funders
- Making commitments on your behalf

⚠️ **You remain responsible for**:
- Accuracy of all information
- Quality of narratives
- Meeting deadlines
- Funder relationships

The AI agent is a powerful assistant, but you're the decision-maker.

## Security & Privacy

- Use trusted, secure AI services
- Don't share sensitive data (EIN, financial details) with untrusted systems
- Keep organizational passwords secure
- Review all AI-generated content before use

## Questions?

See the full documentation in the agent-todo.md file itself for detailed phase-by-phase instructions.
"""
    
    raise ValueError(f"Unknown resource: {uri}")


async def main():
    """Run the MCP server."""
    from mcp.server.stdio import stdio_server
    
    async with stdio_server() as (read_stream, write_stream):
        await app.run(
            read_stream,
            write_stream,
            app.create_initialization_options()
        )


if __name__ == "__main__":
    asyncio.run(main())
```

**Step 2**: Configure Claude Desktop

Edit `~/Library/Application Support/Claude/claude_desktop_config.json` (macOS) or
`%APPDATA%\Claude\claude_desktop_config.json` (Windows):

```json
{
  "mcpServers": {
    "mai-advisor": {
      "command": "python",
      "args": ["/FULL/PATH/TO/mai-advisor-mcp/mai-advisor-mcp/src/server_mcp.py"],
      "env": {
        "PYTHONPATH": "/FULL/PATH/TO/mai-advisor-mcp/mai-advisor-mcp"
      }
    }
  }
}
```

**Step 3**: Restart Claude Desktop

The "mai-advisor" server will appear in Claude's MCP tools.

---

## Option 3: Hybrid Deployment (Best of Both)

### Run Gradio app with MCP Integration

The `app_workflow.py` file can be extended to include MCP server capabilities:

```python
# At the end of app_workflow.py

def start_mcp_server():
    """Start MCP server in background."""
    import subprocess
    import sys
    
    mcp_process = subprocess.Popen(
        [sys.executable, "src/server_mcp.py"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    return mcp_process


# Add to the main block
if __name__ == "__main__":
    # Optional: Start MCP server alongside Gradio
    import os
    if os.getenv("ENABLE_MCP_SERVER"):
        mcp_proc = start_mcp_server()
        print("MCP server started alongside Gradio app")
    
    app.launch(server_name="0.0.0.0", server_port=7860, share=False)
```

Then set environment variable to enable MCP:
```bash
ENABLE_MCP_SERVER=true python app_workflow.py
```

---

## FastMCP Alternative (Simpler)

For even easier MCP integration, use FastMCP from the Python SDK:

```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("MAI Advisor")

@mcp.tool()
def generate_dorks(topic: str, location: str = "") -> str:
    """Generate search dorks."""
    dorks = GrantDorkGenerator.generate_all_dorks(topic, location or None)
    return f"Google: {dorks['google']}\nBing: {dorks['bing']}\nDuckDuckGo: {dorks['duckduckgo']}"

if __name__ == "__main__":
    mcp.run()  # Automatically handles stdio transport
```

Run directly or via Claude Desktop config:
```json
{
  "mcpServers": {
    "mai-advisor": {
      "command": "python",
      "args": ["src/server_fastmcp.py"]
    }
  }
}
```

---

## Environment Variables

Required for all deployments:

```env
# Optional: If using AI features
ANTHROPIC_API_KEY=your_key_here
TAVILY_API_KEY=your_key_here

# Optional: Enable MCP server alongside Gradio
ENABLE_MCP_SERVER=false
```

---

## Testing Your Deployment

### Test Gradio App
```bash
python app_workflow.py
# Visit http://localhost:7860
```

### Test MCP Server
```bash
# Install MCP inspector
npm install -g @modelcontextprotocol/inspector

# Test server
mcp-inspector python src/server_mcp.py
```

### Test Claude Desktop Integration
1. Configure claude_desktop_config.json
2. Restart Claude Desktop
3. Start new conversation
4. Type "@" to see MCP tools
5. Select "mai-advisor" tools

---

## Deployment Checklist

- [ ] `app_workflow.py` - Main Gradio app
- [ ] `src/server_mcp.py` - MCP server implementation
- [ ] `requirements.txt` - All dependencies
- [ ] `README.md` - HuggingFace frontmatter
- [ ] `.env` - Environment variables (local only, not committed)
- [ ] Test Gradio interface works
- [ ] Test MCP server with Claude Desktop
- [ ] Documentation for both modes
- [ ] Video demo for HuggingFace submission

---

## HuggingFace Space Tags

For MCP 1st Birthday Hackathon:

- **Track 1** (Building MCP): `building-mcp-track-enterprise`
- **Track 2** (MCP in Action): `mcp-in-action-track-enterprise`

Choose based on your focus:
- Building MCP = focus on the server/tool implementation
- MCP in Action = focus on the autonomous agent workflow

---

## Resources

- [MCP Documentation](https://modelcontextprotocol.io)
- [Python MCP SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Gradio + MCP Guide](https://huggingface.co/blog/gradio-mcp)
- [Claude Desktop MCP Setup](https://claude.ai/docs/mcp)

---

**Ready to deploy!** 🚀

Choose your deployment mode and follow the corresponding section above.
