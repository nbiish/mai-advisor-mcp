"""
MCP Server for MAI Advisor - Grant Planning System

This server exposes the grant planning workflow as MCP tools for Claude Desktop
and other MCP-compatible clients.

Usage:
    python src/server_mcp.py

Or via Claude Desktop config:
    {
      "mcpServers": {
        "mai-advisor": {
          "command": "python",
          "args": ["/full/path/to/src/server_mcp.py"]
        }
      }
    }
"""

import asyncio
import json
import sys
import os
from datetime import datetime
from typing import Any, Sequence
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from mcp.server import Server
from mcp.types import (
    Resource,
    Tool,
    TextContent,
    ImageContent,
    EmbeddedResource,
)
from pydantic import AnyUrl

# Import workflow components
from dork_generator import GrantDorkGenerator
from output_manager import output_manager
from grant_agent import GrantAdvisorWorkflow


# Initialize MCP server
app = Server("mai-advisor")


@app.list_tools()
async def list_tools() -> list[Tool]:
    """List available MCP tools for grant planning."""
    return [
        Tool(
            name="generate_grant_strategy",
            description="""Generate complete grant planning strategy for a nonprofit/organization.
            
            Creates:
            1. Search engine dorks (Google, Bing, DuckDuckGo)
            2. 3 expert strategic frameworks (financial, grant writing, research)
            3. Comprehensive orchestrated grant plan
            4. AI browser agent task list for autonomous grant discovery/application
            
            All outputs saved to timestamped files in organized directories.
            Perfect for starting a new grant planning initiative.""",
            inputSchema={
                "type": "object",
                "properties": {
                    "topic": {
                        "type": "string",
                        "description": "Grant focus area (e.g., 'youth STEM education', 'community health initiative', 'environmental conservation')"
                    },
                    "location": {
                        "type": "string",
                        "description": "Geographic location (optional - e.g., 'Phoenix, Arizona', 'Seattle metro area')"
                    }
                },
                "required": ["topic"]
            }
        ),
        Tool(
            name="generate_search_dorks",
            description="""Generate optimized search engine queries (dorks) for finding grant opportunities.
            
            Returns queries for:
            - Google (advanced search operators)
            - Bing (site restrictions, file types)
            - DuckDuckGo (clean queries)
            
            Use these queries to find RFPs, grant applications, and funding opportunities.""",
            inputSchema={
                "type": "object",
                "properties": {
                    "topic": {
                        "type": "string",
                        "description": "Grant topic/focus area"
                    },
                    "location": {
                        "type": "string",
                        "description": "Geographic location (optional)"
                    }
                },
                "required": ["topic"]
            }
        ),
        Tool(
            name="get_latest_agent_todo",
            description="""Retrieve the most recent AI browser agent task list.
            
            This file contains comprehensive instructions for AI assistants with browser
            capabilities to autonomously discover and apply for grants. Includes:
            - Phase-by-phase execution plan (90 days)
            - Specific browser automation tasks
            - Application completion guidelines
            - Submission tracking requirements
            
            Provide this to AI agents like AutoGPT, LangChain agents, or custom implementations.""",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            }
        ),
        Tool(
            name="get_latest_orchestrator_plan",
            description="""Retrieve the most recent comprehensive grant planning strategy.
            
            This is the synthesized strategic roadmap combining all three expert frameworks
            (financial, grant writing, research) into a cohesive action plan.""",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            }
        )
    ]


@app.call_tool()
async def call_tool(name: str, arguments: Any) -> Sequence[TextContent | ImageContent | EmbeddedResource]:
    """Handle MCP tool calls."""
    
    if name == "generate_search_dorks":
        topic = arguments["topic"]
        location = arguments.get("location")
        
        # Generate dorks
        dorks = GrantDorkGenerator.generate_all_dorks(
            topic=topic,
            location=location if location else None
        )
        
        # Save to file
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        topic_slug = topic.lower().replace(" ", "_")[:30]
        output_manager.save_dorks(dorks, f"{timestamp}_{topic_slug}")
        
        # Format response
        result = f"""# Search Engine Dorks Generated

**Topic:** {topic}
**Location:** {location or "Not specified"}
**Generated:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

---

## Google Advanced Search

```
{dorks['google']}
```

## Bing Search

```
{dorks['bing']}
```

## DuckDuckGo Search

```
{dorks['duckduckgo']}
```

---

## How to Use

1. Copy each query above
2. Paste into the respective search engine
3. Review results for grant opportunities (RFPs, applications, announcements)
4. Filter for relevant deadlines and requirements

**Files saved to:** `grant_dorks/{timestamp}_{topic_slug}.json`
"""
        
        return [TextContent(type="text", text=result)]
    
    elif name == "generate_grant_strategy":
        topic = arguments["topic"]
        location = arguments.get("location", "")
        
        # Initialize workflow
        workflow = GrantAdvisorWorkflow()
        
        # Step 1: Generate dorks
        dorks = GrantDorkGenerator.generate_all_dorks(
            topic=topic,
            location=location if location else None
        )
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        topic_slug = topic.lower().replace(" ", "_")[:30]
        dorks_file = output_manager.save_dorks(dorks, f"{timestamp}_{topic_slug}")
        
        # Step 2: Generate expert plans
        financial_plan = workflow.generate_financial_plan(topic, location)
        grant_plan = workflow.generate_grant_expert_plan(topic, location)
        research_plan = workflow.generate_research_plan(topic, location)
        
        financial_file = output_manager.save_expert_plan("financial", financial_plan, timestamp)
        grant_file = output_manager.save_expert_plan("grant", grant_plan, timestamp)
        research_file = output_manager.save_expert_plan("research", research_plan, timestamp)
        
        # Step 3: Orchestrate comprehensive plan
        orchestrator_plan = workflow.orchestrate_plan(
            financial_plan, grant_plan, research_plan, topic, location
        )
        orchestrator_file = output_manager.save_orchestrator_plan(orchestrator_plan, timestamp)
        
        # Step 4: Generate AI agent todo
        from app_workflow import generate_ai_agent_todo
        agent_todo = generate_ai_agent_todo(topic, location, dorks)
        agent_file = output_manager.save_ai_agent_todo(agent_todo, timestamp)
        
        # Format success response
        result = f"""# Grant Strategy Generated Successfully ✓

**Topic:** {topic}
**Location:** {location or "Not specified"}
**Generated:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

---

## Files Created

### 1. Search Engine Dorks
**File:** `{dorks_file}`
- Google, Bing, DuckDuckGo queries optimized for grant discovery

### 2. Expert Strategic Frameworks
**Files:**
- `{financial_file}` - Financial planning and budget strategy
- `{grant_file}` - Grant writing and funder relationship guidance
- `{research_file}` - Evidence-based design and evaluation

### 3. Comprehensive Grant Plan
**File:** `{orchestrator_file}`
- Synthesized strategic roadmap combining all expert frameworks

### 4. AI Browser Agent Instructions
**File:** `{agent_file}`
- 8,000+ word task list for autonomous AI assistants
- Phase-by-phase execution plan (90 days)
- Browser automation requirements
- Application completion guidelines

---

## Next Steps

### For Human Review
1. Read the orchestrator plan: `{orchestrator_file}`
2. Review expert frameworks for detailed guidance
3. Use search dorks to begin grant discovery

### For AI Agent Integration
1. Retrieve the agent instructions: `{agent_file}`
2. Provide to AI assistant with browser capabilities
3. Expected outcome: 10-15 grant applications in 90 days

### AI-Compatible Frameworks (2025+)
- Playwright + LLM orchestration
- LangChain autonomous agents
- AutoGPT-style systems
- Custom browser automation implementations

---

**All files saved with timestamp `{timestamp}` for version tracking.**
"""
        
        return [TextContent(type="text", text=result)]
    
    elif name == "get_latest_agent_todo":
        # Find most recent agent-todo file
        agent_dir = Path("agent-instructions")
        if not agent_dir.exists():
            return [TextContent(
                type="text",
                text="No agent instructions found. Generate a grant strategy first using `generate_grant_strategy`."
            )]
        
        agent_files = sorted(agent_dir.glob("agent-todo.*.md"), reverse=True)
        if not agent_files:
            return [TextContent(
                type="text",
                text="No agent instructions found. Generate a grant strategy first using `generate_grant_strategy`."
            )]
        
        latest_file = agent_files[0]
        content = latest_file.read_text()
        
        return [TextContent(type="text", text=content)]
    
    elif name == "get_latest_orchestrator_plan":
        # Find most recent orchestrator plan
        orch_dir = Path("orchestrator_output")
        if not orch_dir.exists():
            return [TextContent(
                type="text",
                text="No orchestrator plan found. Generate a grant strategy first using `generate_grant_strategy`."
            )]
        
        orch_files = sorted(orch_dir.glob("orchestrator_plan.*.md"), reverse=True)
        if not orch_files:
            return [TextContent(
                type="text",
                text="No orchestrator plan found. Generate a grant strategy first using `generate_grant_strategy`."
            )]
        
        latest_file = orch_files[0]
        content = latest_file.read_text()
        
        return [TextContent(type="text", text=content)]
    
    raise ValueError(f"Unknown tool: {name}")


@app.list_resources()
async def list_resources() -> list[Resource]:
    """List available knowledge resources."""
    return [
        Resource(
            uri=AnyUrl("mai://guide/getting-started"),
            name="MAI Advisor Getting Started Guide",
            mimeType="text/markdown",
            description="Introduction to the grant planning system and workflow overview"
        ),
        Resource(
            uri=AnyUrl("mai://guide/ai-agent-integration"),
            name="AI Agent Integration Guide",
            mimeType="text/markdown",
            description="How to use agent-todo.md with AI browser agents for autonomous grant discovery"
        ),
        Resource(
            uri=AnyUrl("mai://guide/expert-frameworks"),
            name="Expert Framework Documentation",
            mimeType="text/markdown",
            description="Understanding the three expert advisors (financial, grant writing, research)"
        )
    ]


@app.read_resource()
async def read_resource(uri: AnyUrl) -> str:
    """Read knowledge resource content."""
    uri_str = str(uri)
    
    if uri_str == "mai://guide/getting-started":
        return """# MAI Advisor - Getting Started

## Overview

MAI Advisor is a comprehensive grant planning system that generates strategic frameworks
and actionable plans for nonprofit organizations seeking funding.

## What It Creates

### 1. Search Engine Dorks
Optimized queries for Google, Bing, and DuckDuckGo to find:
- Grant RFPs (Requests for Proposals)
- Application announcements
- Funding opportunities
- Funder websites

### 2. Expert Strategic Frameworks

**Financial Advisor:** Budget planning, fiscal management, financial sustainability

**Grant Writing Expert:** Proposal development, narrative structure, funder relationships

**Research Expert:** Evidence-based program design, evaluation planning, data collection

### 3. Comprehensive Grant Plan
The Orchestrator synthesizes all three expert frameworks into a cohesive strategic
roadmap with prioritized action steps.

### 4. AI Browser Agent Instructions
A detailed task list (8,000+ words) for AI assistants with browser capabilities to:
- Execute search dorks across multiple engines
- Discover 15-25 grant opportunities
- Gather organizational information
- Complete grant applications
- Manage submission tracking

## Quick Start with MCP

Use the `generate_grant_strategy` tool:

```json
{
  "topic": "youth STEM education program",
  "location": "Seattle, Washington"
}
```

The system generates all four output types and saves them to organized directories:
- `grant_dorks/` - Search queries
- `advisors_output/` - Expert frameworks
- `orchestrator_output/` - Comprehensive plan
- `agent-instructions/` - AI agent tasks

## Workflow Timeline

**Immediate (Day 1):**
- Review search dorks
- Begin manual grant discovery
- Read expert frameworks

**Week 1-2:**
- Execute comprehensive plan
- Set up organizational infrastructure
- Begin relationship cultivation

**Month 1-3 (with AI Agent):**
- AI discovers 15-25 opportunities
- AI helps complete applications
- 10-15 submissions achieved
- Post-submission tracking

## Integration Points

### For Humans
Read the orchestrator plan and expert frameworks for strategic guidance. Use search
dorks manually.

### For AI Agents
Provide the `agent-todo.*.md` file to your AI assistant with browser capabilities.
The agent executes the full workflow autonomously (with your approval).

### For MCP Clients
This server integrates with:
- Claude Desktop
- Cursor with MCP
- Cline
- Any MCP-compatible client

Tools appear in your client's tool list and can be invoked during conversations.

## Files and Directories

All outputs are timestamped for version tracking:

```
grant_dorks/
  20250115_143022_youth_stem.json

advisors_output/
  financial.20250115_143022.md
  grant.20250115_143022.md
  research.20250115_143022.md

orchestrator_output/
  orchestrator_plan.20250115_143022.md

agent-instructions/
  agent-todo.20250115_143022.md
```

## Next Steps

1. Generate your first strategy using `generate_grant_strategy`
2. Review the orchestrator plan
3. Read expert frameworks for detailed guidance
4. Decide: Manual execution vs. AI agent integration
5. Execute search dorks to find opportunities

**Need help?** Use the other resource guides:
- `mai://guide/ai-agent-integration` - AI agent setup
- `mai://guide/expert-frameworks` - Understanding the advisors
"""
    
    elif uri_str == "mai://guide/ai-agent-integration":
        return """# AI Agent Integration Guide

## Using agent-todo.md with AI Browser Agents

The `agent-instructions/agent-todo.*.md` file contains comprehensive instructions
for AI assistants with browser automation capabilities.

## Prerequisites

Your AI assistant needs:

1. **Browser Automation**
   - Navigate websites (click, scroll, navigate)
   - Fill forms (text inputs, dropdowns, checkboxes)
   - Upload/download files
   - Handle multi-page workflows

2. **Document Processing**
   - Read and understand long instructions
   - Generate text content (narratives, budgets)
   - Format documents (PDF, DOCX, etc.)

3. **Multi-Step Execution**
   - Break down complex tasks
   - Maintain state across sessions
   - Track progress and deadlines

4. **Human-in-the-Loop**
   - Request approval before submissions
   - Ask clarifying questions
   - Report progress and blockers

## Compatible AI Frameworks (2025+)

### Playwright + LLM
```python
from playwright.async_api import async_playwright
# + Your LLM orchestration layer
```

### LangChain Agents
```python
from langchain.agents import initialize_agent
from langchain.tools import BrowserTool
```

### AutoGPT-Style Systems
- AutoGPT
- BabyAGI
- Agent-GPT
- Custom implementations

### Commercial AI Assistants
- Claude with computer use
- OpenAI Agents (when browser-enabled)
- Custom enterprise solutions

## How to Use

### Step 1: Generate Agent Instructions

Use MCP tool:
```json
{
  "name": "generate_grant_strategy",
  "arguments": {
    "topic": "community health initiative",
    "location": "Phoenix, Arizona"
  }
}
```

### Step 2: Retrieve Instructions

Use MCP tool:
```json
{
  "name": "get_latest_agent_todo"
}
```

Or manually locate: `agent-instructions/agent-todo.{timestamp}.md`

### Step 3: Provide to AI Agent

**Option A: Direct Upload**
Upload the entire .md file to your AI agent interface

**Option B: System Prompt**
Include content in your AI agent's system prompt/instructions

**Option C: Tool Context**
Provide as context document for tool-using agents

### Step 4: Configure Agent Behavior

Ensure agent knows:
- **ALWAYS get approval** before submitting applications
- **ALWAYS verify** organizational information with you
- **TRACK progress** using the provided framework
- **REPORT blockers** immediately

## Expected Workflow

### Phase 1: Discovery (Week 1-2)
AI agent executes search dorks across Google, Bing, DuckDuckGo and discovers
15-25 potential grant opportunities. Delivers organized list with:
- Grant name and funder
- Deadline
- Award amount
- Eligibility requirements
- Alignment score (1-10)

### Phase 2: Quick Wins (Week 1-2)
AI tackles 3-5 grants with:
- LOI (Letter of Inquiry) only
- Rolling deadlines
- Quick turnaround
- High alignment

### Phase 3: High Priority (Week 3-6)
AI completes 4-6 full applications for:
- Strong mission alignment
- Significant funding ($25K+)
- Reasonable requirements

### Phase 4: Medium Priority (Week 7-12)
AI pursues additional opportunities while:
- Cultivating funder relationships
- Tracking submitted applications
- Preparing for second-round requirements

### Goal: 10-15 Submitted Applications in 90 Days

## Security & Privacy

⚠️ **Important Safeguards:**

1. **Use Trusted AI Services**
   - Reputable providers with security certifications
   - Clear data handling policies
   - SOC 2 compliance preferred

2. **Protect Sensitive Data**
   - Don't share: EIN, bank accounts, passwords
   - DO share: Mission, programs, impact metrics
   - Review all AI-generated content

3. **Maintain Human Oversight**
   - Approve all submissions
   - Verify all facts and figures
   - Review narratives for accuracy

4. **Track Agent Actions**
   - Monitor browser sessions
   - Review logs and activity
   - Audit completed applications

## Approval Checkpoints

AI agent MUST get your approval before:

1. **Submitting any application** (100% required)
2. **Sending emails to funders** (relationship management)
3. **Making commitments** (partnership agreements, etc.)
4. **Spending organizational resources** (fees, subscriptions)
5. **Sharing confidential information** (financials, strategy)

## You Remain Responsible For

- **Accuracy** of all information submitted
- **Quality** of narratives and proposals
- **Meeting deadlines** and requirements
- **Funder relationships** and communications
- **Legal compliance** and certifications
- **Ethical standards** and truthfulness

The AI agent is a powerful assistant, but you're the decision-maker and
accountable party.

## Troubleshooting

**Agent gets stuck:**
- Provide additional context
- Break task into smaller steps
- Give explicit examples

**Agent misunderstands requirements:**
- Point to specific grant guidelines
- Provide sample successful applications
- Clarify organizational priorities

**Agent needs organizational info:**
- Prepare info packet in advance
- Create templates for common questions
- Maintain updated fact sheet

## Best Practices

1. **Start Small:** Test with 1-2 applications before full automation
2. **Monitor Closely:** Review agent's work daily in early phases
3. **Provide Feedback:** Correct mistakes immediately to improve future performance
4. **Maintain Templates:** Create reusable content for faster execution
5. **Track Progress:** Use the agent's built-in tracking framework

## Questions?

See the full `agent-todo.*.md` file for:
- Phase-by-phase detailed instructions
- Specific browser automation tasks
- Application completion checklists
- Submission tracking templates
- Post-submission follow-up procedures

**The agent instructions are comprehensive (8,000+ words) and designed for
autonomous execution with minimal human intervention.**
"""
    
    elif uri_str == "mai://guide/expert-frameworks":
        return """# Expert Framework Documentation

## The Three Strategic Advisors

MAI Advisor uses three specialized AI experts to provide comprehensive grant
planning guidance. Each expert contributes a unique perspective, and the
Orchestrator synthesizes all three into a cohesive action plan.

---

## 1. Financial Advisor

**Focus:** Budget planning, fiscal management, financial sustainability

### Key Contributions

**Budget Development:**
- Line-item budgeting for grant applications
- Personnel cost calculations
- Indirect cost allocation
- Cost-sharing strategies

**Fiscal Management:**
- Cash flow planning
- Grant fund tracking
- Audit compliance
- Financial reporting requirements

**Sustainability:**
- Diversified revenue streams
- Long-term financial planning
- Post-grant sustainability strategies
- Reserve fund recommendations

### When to Emphasize

- Capital campaigns
- Multi-year grants
- Large budget requests ($100K+)
- Capacity-building initiatives

### Output Format

Markdown document with:
- Executive summary
- Detailed budget framework
- Financial management recommendations
- Risk mitigation strategies

---

## 2. Grant Writing Expert

**Focus:** Proposal development, narrative structure, funder relationships

### Key Contributions

**Proposal Development:**
- Compelling narrative structure
- Problem statement formulation
- Goals and objectives alignment
- Evaluation plan design

**Funder Relationships:**
- Funder research and targeting
- Relationship cultivation strategies
- Communication best practices
- Stewardship planning

**Writing Excellence:**
- Persuasive storytelling
- Evidence-based arguments
- Clarity and conciseness
- Compliance with guidelines

### When to Emphasize

- First-time applicants
- Competitive grant opportunities
- Foundation relationship-building
- Narrative-heavy applications

### Output Format

Markdown document with:
- Narrative strategy
- Key messaging points
- Funder alignment analysis
- Relationship cultivation plan

---

## 3. Research Expert

**Focus:** Evidence-based program design, evaluation, data collection

### Key Contributions

**Program Design:**
- Logic model development
- Theory of change framework
- Evidence-based interventions
- Best practices integration

**Evaluation Planning:**
- Outcome measurement strategies
- Data collection methodologies
- Indicator selection
- Evaluation timeline

**Evidence Base:**
- Literature review guidance
- Citation of proven models
- Data-driven decision making
- Impact demonstration

### When to Emphasize

- Program/project grants
- Government funding (federal, state)
- Research-oriented foundations
- Outcome-focused initiatives

### Output Format

Markdown document with:
- Logic model
- Evaluation framework
- Evidence-based recommendations
- Data collection plan

---

## The Orchestrator

**Role:** Synthesize all three expert frameworks into a unified strategic plan

### Orchestration Process

1. **Analyze Expert Contributions**
   - Extract key recommendations from each advisor
   - Identify common threads and synergies
   - Note contradictions or tensions

2. **Prioritize Actions**
   - Immediate steps (Week 1-2)
   - Short-term goals (Month 1-3)
   - Long-term strategy (Month 4-12)

3. **Create Integrated Plan**
   - Combined budget + narrative + evaluation approach
   - Sequenced action steps
   - Resource allocation
   - Timeline with milestones

4. **Deliver Cohesive Roadmap**
   - Executive summary
   - Phased implementation plan
   - Success metrics
   - Risk management

### Output Format

Comprehensive markdown document with:
- Executive summary (all three perspectives)
- Integrated strategic framework
- Prioritized action plan
- Resource requirements
- Timeline and milestones
- Success indicators

---

## How They Work Together

### Example: Youth STEM Education Grant

**Financial Advisor:**
- Budget: $150K total ($100K personnel, $30K supplies, $20K indirect)
- Cash flow: Quarterly reimbursement model
- Sustainability: Fee-for-service model after grant period

**Grant Writing Expert:**
- Problem: STEM achievement gap in underserved communities
- Solution: After-school coding clubs + mentorship
- Narrative: Student success stories + community impact

**Research Expert:**
- Evidence: Proven coding curriculum (Code.org, Scratch)
- Evaluation: Pre/post assessments, attendance tracking
- Outcomes: 80% skill improvement, 90% engagement

**Orchestrator Synthesis:**
Integrated 12-month plan combining:
- Budget timeline aligned with program milestones
- Narrative structure supporting evidence-based approach
- Evaluation data feeding into sustainability case
- Sequenced action steps for proposal development

---

## Customization

Each expert adapts to:
- **Grant type** (foundation, government, corporate)
- **Organization size** (small nonprofit vs. large institution)
- **Funding amount** (micro-grants vs. major gifts)
- **Program stage** (new initiative vs. expansion)

---

## Using the Frameworks

### For Humans

1. Read orchestrator plan first (big picture)
2. Deep-dive into relevant expert framework
3. Use as reference during application writing
4. Return to specific sections as needed

### For AI Agents

- All frameworks provided as context
- Agent synthesizes relevant sections per grant
- Automatically adapts language and emphasis
- Maintains consistency across applications

---

**The three-expert model ensures comprehensive coverage of all grant planning
dimensions while maintaining specialized depth in each domain.**
"""
    
    raise ValueError(f"Unknown resource: {uri}")


async def main():
    """Run the MCP server via stdio transport."""
    from mcp.server.stdio import stdio_server
    
    async with stdio_server() as (read_stream, write_stream):
        await app.run(
            read_stream,
            write_stream,
            app.create_initialization_options()
        )


if __name__ == "__main__":
    asyncio.run(main())
