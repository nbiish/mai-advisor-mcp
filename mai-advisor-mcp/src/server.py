"""MCP Server for Grant Finder Assistant."""
import json
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

from search_operators import (
    GrantSearchCriteria,
    UnifiedSearchOperatorGenerator,
    SearchEngine,
)
from grant_agent import GrantResearchAgent
from advisor_tools import MAIAdvisorWorkflow

# Load environment variables
load_dotenv()


# Initialize MCP server
app = Server("mai-advisor-mcp")

# Initialize grant research agent
agent = GrantResearchAgent()

# Initialize MAI Advisor workflow
workflow = MAIAdvisorWorkflow()


@app.list_resources()
async def list_resources() -> list[Resource]:
    """List available resources."""
    return [
        Resource(
            uri=AnyUrl("grant://guide/getting-started"),
            name="MAI Advisor Getting Started Guide",
            mimeType="text/markdown",
            description="Introduction to using the MAI Advisor MCP",
        ),
        Resource(
            uri=AnyUrl("grant://guide/search-operators"),
            name="Search Operator Guide",
            mimeType="text/markdown",
            description="Guide to advanced search operators for grant finding",
        ),
        Resource(
            uri=AnyUrl("grant://templates/nonprofit"),
            name="Nonprofit Grant Search Template",
            mimeType="application/json",
            description="Template search criteria for nonprofit organizations",
        ),
        Resource(
            uri=AnyUrl("grant://templates/research"),
            name="Research Grant Search Template",
            mimeType="application/json",
            description="Template search criteria for research grants",
        ),
    ]


@app.read_resource()
async def read_resource(uri: AnyUrl) -> str:
    """Read a specific resource."""
    uri_str = str(uri)
    
    if uri_str == "grant://guide/getting-started":
        return """# MAI Advisor MCP - Getting Started

## Overview
The MAI Advisor MCP is an AI-powered tool for discovering and analyzing grant opportunities.

## Quick Start

1. **Search for Grants**
   Use the `search_grants` tool with your criteria:
   - Keywords (required)
   - Organization type
   - Sector
   - Location
   - Funding range

2. **Generate Search Operators**
   Use `generate_search_operators` to create advanced queries for:
   - Google
   - Bing
   - DuckDuckGo

3. **Analyze Results**
   Get AI-powered analysis of grant fit and eligibility.

## Example Usage

```json
{
  "keywords": ["education", "technology"],
  "organization_type": "nonprofit",
  "sector": "education",
  "location": "California",
  "funding_range_min": 10000,
  "funding_range_max": 100000
}
```
"""
    
    elif uri_str == "grant://guide/search-operators":
        return """# Advanced Search Operators Guide

## Google Search Operators
- `"exact phrase"` - Exact match
- `site:domain.com` - Search within domain
- `intitle:term` - Term in title
- `filetype:pdf` - Specific file type
- `OR` - Logical OR
- `-term` - Exclude term

## Bing Search Operators
- `intitle:term` - Term in title
- `inbody:term` - Term in body
- `loc:location` - Geographic location
- `NOT term` - Exclude term
- `contains:term` - Page contains term

## DuckDuckGo Search Operators
- `"exact phrase"` - Exact match
- `site:domain.com` - Search within domain
- `intitle:term` - Term in title
- `-term` - Exclude term

## Best Practices
1. Combine multiple operators for precision
2. Use trusted grant sites (grants.gov, nsf.gov, etc.)
3. Include deadline-related terms
4. Filter by file type (PDF, DOC) for announcements
"""
    
    elif uri_str == "grant://templates/nonprofit":
        template = {
            "keywords": ["community", "nonprofit", "social impact"],
            "organization_type": "nonprofit",
            "sector": "community development",
            "location": "",
            "funding_range_min": 5000,
            "funding_range_max": 50000,
            "deadline_months": 6,
            "exclude_terms": ["loan", "debt"]
        }
        return json.dumps(template, indent=2)
    
    elif uri_str == "grant://templates/research":
        template = {
            "keywords": ["research", "innovation", "science"],
            "organization_type": "university",
            "sector": "research",
            "location": "",
            "funding_range_min": 50000,
            "funding_range_max": 500000,
            "deadline_months": 12,
            "exclude_terms": ["undergraduate", "student"]
        }
        return json.dumps(template, indent=2)
    
    raise ValueError(f"Unknown resource: {uri}")


@app.list_tools()
async def list_tools() -> list[Tool]:
    """List available tools."""
    return [
        Tool(
            name="search_grants",
            description="Search for grant opportunities using AI-powered research. Provide keywords and optionally organization type, sector, location, and funding range.",
            inputSchema={
                "type": "object",
                "properties": {
                    "keywords": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Keywords to search for (e.g., ['education', 'technology'])"
                    },
                    "organization_type": {
                        "type": "string",
                        "description": "Type of organization (nonprofit, business, individual, university, etc.)"
                    },
                    "sector": {
                        "type": "string",
                        "description": "Sector or field (education, healthcare, technology, arts, etc.)"
                    },
                    "location": {
                        "type": "string",
                        "description": "Geographic location or region"
                    },
                    "amount_min": {
                        "type": "integer",
                        "description": "Minimum amount in dollars (e.g., grant size, revenue threshold)"
                    },
                    "amount_max": {
                        "type": "integer",
                        "description": "Maximum amount in dollars (e.g., grant size, revenue threshold)"
                    },
                    "deadline_months": {
                        "type": "integer",
                        "description": "Find grants with deadlines within X months"
                    },
                    "exclude_terms": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Terms to exclude from search"
                    },
                    "depth": {
                        "type": "string",
                        "enum": ["basic", "deep"],
                        "description": "Research depth: basic (fast) or deep (AI-analyzed)",
                        "default": "deep"
                    }
                },
                "required": ["keywords"]
            }
        ),
        Tool(
            name="generate_search_operators",
            description="Generate advanced search engine queries optimized for Google, Bing, and DuckDuckGo. Returns formatted queries you can copy and use directly.",
            inputSchema={
                "type": "object",
                "properties": {
                    "keywords": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Keywords to search for"
                    },
                    "organization_type": {
                        "type": "string",
                        "description": "Type of organization"
                    },
                    "sector": {
                        "type": "string",
                        "description": "Sector or field"
                    },
                    "location": {
                        "type": "string",
                        "description": "Geographic location"
                    },
                    "amount_min": {
                        "type": "integer",
                        "description": "Minimum amount in dollars"
                    },
                    "amount_max": {
                        "type": "integer",
                        "description": "Maximum amount in dollars"
                    },
                    "engines": {
                        "type": "array",
                        "items": {
                            "type": "string",
                            "enum": ["google", "bing", "duckduckgo"]
                        },
                        "description": "Search engines to generate queries for (defaults to all)"
                    }
                },
                "required": ["keywords"]
            }
        ),
        Tool(
            name="analyze_grant_fit",
            description="Analyze how well a grant opportunity fits your organization using AI. Provide grant details and organization information.",
            inputSchema={
                "type": "object",
                "properties": {
                    "grant_description": {
                        "type": "string",
                        "description": "Description of the grant opportunity"
                    },
                    "organization_description": {
                        "type": "string",
                        "description": "Description of your organization and mission"
                    },
                    "requirements": {
                        "type": "string",
                        "description": "Grant requirements and eligibility criteria"
                    }
                },
                "required": ["grant_description", "organization_description"]
            }
        ),
        Tool(
            name="expert_advisor_workflow",
            description="Execute complete MAI Advisor workflow: Expert advisor analyzes request → generates research tasks → research crew produces search dorks (advanced queries) → financial advisor provides guidance. This is the primary tool for comprehensive grant search strategy.",
            inputSchema={
                "type": "object",
                "properties": {
                    "topic": {
                        "type": "string",
                        "description": "Main topic or focus area (e.g., 'education technology for indigenous communities')"
                    },
                    "context": {
                        "type": "string",
                        "description": "Additional context about your needs or situation"
                    },
                    "organization_type": {
                        "type": "string",
                        "description": "Type of organization (nonprofit, business, university, individual, etc.)"
                    },
                    "sector": {
                        "type": "string",
                        "description": "Primary sector (education, healthcare, technology, arts, etc.)"
                    },
                    "amount_min": {
                        "type": "integer",
                        "description": "Minimum amount in dollars"
                    },
                    "amount_max": {
                        "type": "integer",
                        "description": "Maximum amount in dollars"
                    },
                    "timeline": {
                        "type": "string",
                        "description": "Timeline or urgency (e.g., 'need funding within 6 months')"
                    },
                    "include_financial_guidance": {
                        "type": "boolean",
                        "description": "Include financial advisor guidance in response (default: true)",
                        "default": True
                    }
                },
                "required": ["topic"]
            }
        ),
        Tool(
            name="financial_guidance",
            description="Get financial guidance for grant seeking process from expert financial advisor. Covers budgeting, compliance, planning, and grant management best practices.",
            inputSchema={
                "type": "object",
                "properties": {
                    "stage": {
                        "type": "string",
                        "enum": ["research", "planning", "application", "management", "general"],
                        "description": "Current stage in grant process"
                    },
                    "amount_min": {
                        "type": "integer",
                        "description": "Minimum funding amount being considered"
                    },
                    "amount_max": {
                        "type": "integer",
                        "description": "Maximum funding amount being considered"
                    },
                    "organization_type": {
                        "type": "string",
                        "description": "Type of organization (nonprofit, business, etc.)"
                    }
                },
                "required": ["stage"]
            }
        )
    ]


@app.call_tool()
async def call_tool(name: str, arguments: Any) -> Sequence[TextContent | ImageContent | EmbeddedResource]:
    """Handle tool calls."""
    
    if name == "search_grants":
        # Extract criteria from arguments
        criteria = GrantSearchCriteria(
            keywords=arguments["keywords"],
            organization_type=arguments.get("organization_type"),
            sector=arguments.get("sector"),
            location=arguments.get("location"),
            amount_min=arguments.get("amount_min"),
            amount_max=arguments.get("amount_max"),
            deadline_months=arguments.get("deadline_months"),
            exclude_terms=arguments.get("exclude_terms")
        )
        
        depth = arguments.get("depth", "deep")
        
        # Perform research
        results = await agent.research_grants(criteria, depth=depth)
        
        # Generate report
        report = agent.generate_grant_report(results, format="markdown")
        
        return [TextContent(type="text", text=report)]
    
    elif name == "generate_search_operators":
        # Extract criteria
        criteria = GrantSearchCriteria(
            keywords=arguments["keywords"],
            organization_type=arguments.get("organization_type"),
            sector=arguments.get("sector"),
            location=arguments.get("location"),
            amount_min=arguments.get("amount_min"),
            amount_max=arguments.get("amount_max")
        )
        
        # Parse engine list
        engine_names = arguments.get("engines", ["google", "bing", "duckduckgo"])
        engines = [SearchEngine(name) for name in engine_names]
        
        # Generate queries
        generator = UnifiedSearchOperatorGenerator()
        queries = generator.generate_queries(criteria, engines)
        
        # Format output
        output = generator.format_for_display(queries)
        
        return [TextContent(type="text", text=output)]
    
    elif name == "analyze_grant_fit":
        from langchain.schema import HumanMessage, SystemMessage
        
        system_prompt = """You are an expert grant advisor. Analyze the fit between a grant opportunity and an organization.

Provide:
1. **Fit Score** (1-10): How well the grant matches the organization
2. **Strengths**: Why this is a good match
3. **Concerns**: Potential issues or challenges
4. **Recommendations**: Strategic advice for applying
5. **Next Steps**: Concrete action items

Be honest and constructive in your assessment."""
        
        user_prompt = f"""Analyze this grant opportunity:

GRANT DESCRIPTION:
{arguments['grant_description']}

ORGANIZATION:
{arguments['organization_description']}

{'REQUIREMENTS:' + chr(10) + arguments.get('requirements', 'Not specified') if arguments.get('requirements') else ''}

Please provide a comprehensive fit analysis."""
        
        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=user_prompt)
        ]
        
        response = agent.model.invoke(messages)
        
        return [TextContent(type="text", text=response.content)]
    
    raise ValueError(f"Unknown tool: {name}")


@app.list_prompts()
async def list_prompts() -> list:
    """List available prompts."""
    return [
        {
            "name": "grant_search_wizard",
            "description": "Interactive wizard to help you search for grants",
            "arguments": []
        },
        {
            "name": "application_strategy",
            "description": "Get strategic advice for grant applications",
            "arguments": [
                {
                    "name": "grant_type",
                    "description": "Type of grant you're applying for",
                    "required": True
                }
            ]
        }
    ]


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
