---
title: MAI Advisor - AI Grant Planning System
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
  - browser-automation
  - autonomous-agents
short_description: Complete grant planning system with AI browser agent integration. Generates strategic frameworks, search queries, and autonomous agent instructions for nonprofits seeking funding.
---

# MAI Advisor - Multi-Agent Intelligence Grant Planning System

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.11+-green.svg)
![Gradio](https://img.shields.io/badge/gradio-5.49.1-orange.svg)
![MCP](https://img.shields.io/badge/MCP-Server-purple.svg)

**AI-powered grant planning system that generates comprehensive strategies and autonomous browser agent instructions for nonprofit organizations.**

🏆 **Submitted for MCP 1st Birthday Hackathon - MCP in Action Track (Enterprise)**

---

## 🌟 What This System Does

MAI Advisor is a complete grant planning workflow that:

1. **🔍 Generates Search Engine Dorks** - Optimized queries for Google, Bing, DuckDuckGo to find grant opportunities
2. **👥 Creates Expert Strategic Frameworks** - Three AI advisors (Financial, Grant Writing, Research) provide specialized guidance
3. **🎼 Orchestrates Comprehensive Plan** - Synthesizes all expert frameworks into a cohesive strategic roadmap
4. **🤖 Produces AI Browser Agent Instructions** - 8,000+ word task list for autonomous AI assistants to discover and apply for grants

**Goal:** Enable nonprofits to go from initial idea to 10-15 grant applications in 90 days with AI assistance.

---

## 🚀 Quick Start

### Option 1: HuggingFace Space (Web Interface)

**Just click "Use this Space" above!**

1. Enter your grant topic (e.g., "youth STEM education program")
2. Optional: Add location (e.g., "Phoenix, Arizona")
3. Click "Generate Complete Grant Strategy"
4. Download all generated files from the output tabs

**Outputs:**
- `grant_dorks/` - Search queries to paste into search engines
- `advisors_output/` - 3 expert strategic frameworks
- `orchestrator_output/` - Comprehensive grant plan
- `agent-instructions/` - AI browser agent task list

### Option 2: Model Context Protocol (MCP) Server

**Use MAI Advisor directly in Claude Desktop!**

#### Step 1: Clone this repository
```bash
git clone https://github.com/YOUR_USERNAME/mai-advisor-mcp.git
cd mai-advisor-mcp/mai-advisor-mcp
```

#### Step 2: Install dependencies
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

#### Step 3: Configure Claude Desktop
```bash
python setup_claude_config.py
```

This automatically adds MAI Advisor to your Claude Desktop MCP servers.

#### Step 4: Restart Claude Desktop

Quit and relaunch Claude Desktop. The MAI Advisor tools will appear in Claude's tool list.

#### Step 5: Use in Claude

Start a conversation:
> "Generate a grant strategy for a community health initiative in Seattle"

Claude will automatically invoke the MAI Advisor MCP tools and provide comprehensive results.

---

## 📊 System Architecture

### The Three Expert Advisors

#### 1. 💰 Financial Advisor
- Budget development and planning
- Fiscal management strategies
- Cash flow projections
- Sustainability planning
- Indirect cost allocation

#### 2. ✍️ Grant Writing Expert
- Compelling narrative development
- Problem statement formulation
- Funder research and targeting
- Relationship cultivation
- Proposal structure and compliance

#### 3. 🔬 Research Expert
- Evidence-based program design
- Logic model development
- Evaluation planning
- Outcome measurement
- Data collection methodologies

### The Orchestrator

Synthesizes all three expert frameworks into a unified strategic plan with:
- Prioritized action steps
- Integrated timeline
- Resource allocation
- Risk mitigation
- Success metrics

---

## 🤖 AI Browser Agent Integration

### What is the Agent TODO?

The `agent-instructions/agent-todo.*.md` file is a comprehensive task list designed for AI assistants with **browser automation capabilities**.

**Compatible AI Frameworks:**
- Playwright + LLM orchestration
- LangChain autonomous agents
- AutoGPT-style systems
- Commercial AI assistants (Claude with computer use, etc.)
- Custom browser automation implementations

### What the AI Agent Does

#### Phase 1: Discovery (Week 1-2)
- Executes search dorks across Google, Bing, DuckDuckGo
- Discovers 15-25 potential grant opportunities
- Evaluates alignment with your mission
- Prioritizes by deadline, amount, fit

#### Phase 2: Quick Wins (Week 1-2)
- Identifies 3-5 grants with LOI-only requirements
- Completes simple applications first
- Builds momentum with early submissions

#### Phase 3: High Priority (Week 3-6)
- Tackles 4-6 full applications
- Focuses on strong mission alignment
- Targets significant funding ($25K+)

#### Phase 4: Medium Priority (Week 7-12)
- Continues application pipeline
- Cultivates funder relationships
- Tracks submitted applications
- Prepares for second-round requirements

**Target:** 10-15 submitted applications in 90 days

### Security & Human Oversight

⚠️ **The AI agent ALWAYS requires approval before:**
- Submitting any application
- Sending emails to funders
- Making commitments on your behalf
- Sharing confidential information

**You remain responsible for:**
- Accuracy of all information
- Quality of narratives
- Meeting deadlines
- Funder relationships
- Legal compliance

The AI is a powerful assistant, but you're the decision-maker.

---

## 🛠️ Technical Details

### Built With

- **Gradio 5.49.1** - Web interface framework
- **Anthropic Claude** - AI expert advisors and orchestration
- **Model Context Protocol** - Claude Desktop integration
- **Python 3.11+** - Core implementation
- **FastMCP** - MCP server framework

### MCP Server Tools

When used as an MCP server, MAI Advisor exposes:

**Tools:**
- `generate_grant_strategy` - Full workflow execution
- `generate_search_dorks` - Search query generation only
- `get_latest_agent_todo` - Retrieve AI agent instructions
- `get_latest_orchestrator_plan` - Retrieve strategic plan

**Resources:**
- `mai://guide/getting-started` - System overview
- `mai://guide/ai-agent-integration` - AI agent setup
- `mai://guide/expert-frameworks` - Expert advisor documentation

### File Structure

```
mai-advisor-mcp/
├── app_workflow.py              # Main Gradio application
├── src/
│   ├── server_mcp.py           # MCP server implementation
│   ├── grant_agent.py          # Expert advisor workflows
│   ├── dork_generator.py       # Search query generation
│   ├── output_manager.py       # File output management
│   └── ...
├── grant_dorks/                # Generated search queries
├── advisors_output/            # Expert framework documents
├── orchestrator_output/        # Comprehensive strategic plans
├── agent-instructions/         # AI browser agent task lists
├── requirements.txt
├── README_DEPLOY.md            # Deployment documentation
└── setup_claude_config.py      # Claude Desktop setup helper
```

---

## 🎥 Demo Video

[Link to demo video showing:]
- Gradio interface workflow
- Generated outputs review
- MCP server integration with Claude Desktop
- AI browser agent execution (simulated)

---

## 📝 Use Cases

### For Small Nonprofits
- Limited grant writing experience
- No dedicated development staff
- Need rapid capability building

### For Medium Organizations
- Expanding program portfolio
- Diversifying revenue streams
- Scaling proven interventions

### For Consultants
- Supporting multiple clients
- Accelerating proposal development
- Providing strategic frameworks

### For AI/Automation Enthusiasts
- Experimenting with autonomous agents
- Building browser automation systems
- Exploring agentic workflows

---

## 🏆 MCP 1st Birthday Hackathon

### Track: MCP in Action - Enterprise

**Category:** Autonomous Agent Workflows

**Innovation:**
- First grant planning system with full MCP integration
- Comprehensive AI browser agent instructions (8,000+ words)
- Three-expert advisor architecture
- Dual deployment (web + MCP server)

**Business Impact:**
- Reduces grant planning time from months to days
- Enables 10-15 applications in 90 days (vs. typical 2-3)
- Democratizes access to grant funding for under-resourced nonprofits
- Provides strategic frameworks regardless of AI agent availability

**Technical Excellence:**
- Proper MCP server implementation with FastMCP
- Claude Desktop integration
- Gradio web interface
- Comprehensive resource documentation
- Autonomous agent-ready outputs

---

## 📜 License

MIT License - see [LICENSE](LICENSE) for details.

---

## 🤝 Contributing

Contributions welcome! This project is designed to help nonprofits access funding more effectively.

**Areas for contribution:**
- Additional expert advisor types (legal, marketing, etc.)
- Enhanced AI agent instructions
- Integration with grant databases
- Multi-language support
- Additional search engine support

---

## 📧 Contact & Support

- **Issues:** [GitHub Issues](https://github.com/YOUR_USERNAME/mai-advisor-mcp/issues)
- **Discussions:** [GitHub Discussions](https://github.com/YOUR_USERNAME/mai-advisor-mcp/discussions)

---

## 🙏 Acknowledgments

- **Anthropic** - Claude API and Model Context Protocol
- **HuggingFace** - Gradio framework and Space hosting
- **MCP Community** - FastMCP library and documentation

---

## 🔮 Roadmap

### Q1 2025
- [ ] Integration with grant databases (Grants.gov, Foundation Directory)
- [ ] Enhanced funder research capabilities
- [ ] Budget template library
- [ ] Multi-organization support

### Q2 2025
- [ ] AI agent execution dashboard
- [ ] Application tracking and CRM
- [ ] Funder relationship management
- [ ] Post-submission reporting automation

### Q3 2025
- [ ] Grant outcome analytics
- [ ] Success prediction models
- [ ] Peer learning network
- [ ] Training and certification program

---

**Made with ❤️ for the nonprofit sector**

Empowering organizations to secure the funding they need to make a difference.
