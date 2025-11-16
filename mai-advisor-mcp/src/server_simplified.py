"""
Simplified MCP Server for MAI Advisor - Grant Dork Generator
Single tool interface: find_grants(topic, location) -> saves dorks to output folder
Uses OutputManager for organized file storage.
"""
from typing import Any, Sequence
from dotenv import load_dotenv

from mcp.server import Server
from mcp.types import Resource, Tool, TextContent
from mcp.server.stdio import stdio_server
from pydantic import AnyUrl

from dork_generator import GrantDorkGenerator
from output_manager import output_manager

# Load environment variables
load_dotenv()

# Initialize MCP server
app = Server("mai-advisor-mcp")


# Initialize MCP server
app = Server("mai-advisor-mcp")


@app.list_tools()
async def list_tools() -> list[Tool]:
    """List available MCP tools."""
    return [
        Tool(
            name="find_grants",
            description=(
                "Generate comprehensive grant search queries (Google dorks) and save to output folder. "
                "Simple 2-input interface: just provide a topic/focus area and optional location. "
                "The tool automatically generates extensive search queries for Google, Bing, and DuckDuckGo, "
                "covering all grant-related terminology, process terms, and location targeting. "
                "Results are saved to grant_dorks/ directory using OutputManager."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "topic": {
                        "type": "string",
                        "description": (
                            "Main topic or focus area for grant search. Can be general (e.g., 'education') "
                            "or specific (e.g., 'indigenous tribal healthcare technology'). "
                            "The expert system will analyze this and generate comprehensive search queries."
                        )
                    },
                    "location": {
                        "type": "string",
                        "description": (
                            "Geographic focus for grants. Can be city, state, country, or multiple locations "
                            "separated by commas (e.g., 'Michigan, Minnesota' or 'California'). "
                            "Optional - leave empty for nationwide/global search."
                        )
                    }
                },
                "required": ["topic"]
            }
        )
    ]


@app.call_tool()
async def call_tool(name: str, arguments: Any) -> Sequence[TextContent]:
    """Handle tool calls."""
    if name == "find_grants":
        topic = arguments.get("topic", "")
        location = arguments.get("location", "")
        
        if not topic:
            return [TextContent(
                type="text",
                text="❌ Error: Topic is required. Please provide a topic or focus area for your grant search."
            )]
        
        # Generate dorks
        dorks = GrantDorkGenerator.generate_all_dorks(topic=topic, location=location or None)
        
        # Save to file using output manager
        filepath = output_manager.save_dorks(topic, location or None, dorks)
        
        # Format response
        response = f"""✅ Grant search dorks generated successfully!

**Topic:** {topic}
**Location:** {location or "Not specified"}
**Saved to:** {filepath}

---

## 🔍 Google Dork
```
{dorks['google']}
```

## 🔍 Bing Dork
```
{dorks['bing']}
```

## 🔍 DuckDuckGo Dork  
```
{dorks['duckduckgo']}
```

---

## 📋 How to Use

1. **Google**: Copy the Google dork above and paste into https://www.google.com/search
2. **Bing**: Copy the Bing dork and paste into https://www.bing.com/search  
3. **DuckDuckGo**: Copy the DuckDuckGo dork and paste into https://duckduckgo.com

## 📁 Output File

All dorks have been saved to: `{filepath}`

The JSON file contains:
- Generated dorks for all three search engines
- Timestamp and search parameters
- Usage instructions

You can share this file with colleagues or use it for documentation.
"""
        
        return [TextContent(type="text", text=response)]
    
    raise ValueError(f"Unknown tool: {name}")


@app.list_resources()
async def list_resources() -> list[Resource]:
    """List available resources."""
    return [
        Resource(
            uri=AnyUrl("mai://config/output-directories"),
            name="Output Directory Structure",
            mimeType="text/plain",
            description="View configured output directories for advisors, orchestrator, and dorks",
        ),
        Resource(
            uri=AnyUrl("mai://guide/usage"),
            name="Usage Guide",
            mimeType="text/markdown",
            description="Quick start guide for MAI Advisor MCP",
        ),
    ]


@app.read_resource()
async def read_resource(uri: AnyUrl) -> str:
    """Read a specific resource."""
    uri_str = str(uri)
    
    if uri_str == "mai://config/output-directories":
        return f"""# Output Directory Structure

**Advisors Output:** {output_manager.advisors_dir}
Individual advisor reports (financial, grant, research)

**Orchestrator Output:** {output_manager.orchestrator_dir}
Final synthesized business & grant plans

**Dorks Output:** {output_manager.dorks_dir}
Generated search dorks

All directories are automatically created and managed by OutputManager.
"""
    
    elif uri_str == "mai://guide/usage":
        return """# MAI Advisor MCP - Usage Guide

## Quick Start

### Find Grants Tool

The `find_grants` tool is your one-stop interface for generating comprehensive grant search queries.

**Inputs:**
- `topic` (required): What you're looking for (e.g., "indigenous education", "climate technology")
- `location` (optional): Geographic focus (e.g., "Michigan, Minnesota")

**What It Does:**
1. Analyzes your topic using expert knowledge
2. Generates extensive Google dorks with intext/inurl variants
3. Creates optimized queries for Google, Bing, and DuckDuckGo
4. Saves everything to a timestamped JSON file

**Example:**
```
Tool: find_grants
Args: {
  "topic": "indigenous tribal healthcare",
  "location": "Michigan, Minnesota"
}
```

**Output:**
- Comprehensive search queries for all 3 engines
- Saved to: `grant_dorks/YYYYMMDD_HHMMSS_topic.json`
- Ready to copy/paste into search engines

## Configuration

Set output directory via environment variable:
```
MAI_OUTPUT_DIR=/path/to/your/grants/folder
```

Default: `./grant_dorks/` (relative to server)

## Tips

- Be specific with topics for better results
- Use comma-separated locations for multi-state search
- Check the output folder for all saved searches
- Share generated files with your team
"""
    
    return "Resource not found"


async def main():
    """Run the MCP server."""
    async with stdio_server() as (read_stream, write_stream):
        await app.run(
            read_stream,
            write_stream,
            app.create_initialization_options()
        )


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
