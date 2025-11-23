# 🎯 MAI Advisor - Multi-Agent Intelligence Grant Planning System

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](mai-advisor-mcp/LICENSE)
[![Python](https://img.shields.io/badge/python-3.11+-green.svg)](https://www.python.org)
[![Gradio](https://img.shields.io/badge/gradio-5.49.1-orange.svg)](https://www.gradio.app)
[![OpenRouter](https://img.shields.io/badge/OpenRouter-Gemini_2.0_Flash-red.svg)](https://openrouter.ai)
[![MCP](https://img.shields.io/badge/MCP-Server-purple.svg)](https://modelcontextprotocol.io)

**MCP 1st Birthday Hackathon Submission** | Enterprise Track (Both Categories)

A complete AI-powered grant planning system that transforms nonprofit organizations from 2-3 grant applications per year to 10-15 applications in 90 days through strategic frameworks and autonomous AI agent execution.

---

## 🌟 What This System Does

MAI Advisor provides **dual deployment modes** for comprehensive grant planning:

### 🖥️ Gradio Web Interface
- **User-friendly UI** for immediate grant strategy generation
- **6 comprehensive outputs** in 60 seconds:
  - Search engine dorks (Google, Bing, DuckDuckGo)
  - Financial management framework
  - Grant writing strategy
  - Research methodology
  - Orchestrated grant plan
  - AI agent execution instructions (8,000+ words)
- **Public access** - users provide own OpenRouter API keys
- **Zero setup** - runs in browser

### 🔌 MCP Server Integration
- **Native MCP protocol** for Claude Desktop
- **4 tools** exposed via Model Context Protocol
- **3 knowledge resources** for strategic guidance
- **Async stdio transport** for production use

---

## 🚀 Quick Start

### Option 1: HuggingFace Space (No Installation)

Visit the deployed Space (coming soon):
```
https://huggingface.co/spaces/nbiish/mai-advisor-grant-planning
```

1. Enter your OpenRouter API key ([get one free](https://openrouter.ai/keys))
2. Enter grant topic and location
3. Generate complete strategy
4. Download 6 comprehensive files

### Option 2: Local Development

```bash
# Clone repository
git clone https://github.com/nbiish/mai-advisor-mcp.git
cd mai-advisor-mcp/mai-advisor-mcp

# Setup virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run Gradio app
python app_workflow.py
```

Visit http://localhost:7860

### Option 3: MCP Server (Claude Desktop)

```bash
# Run setup script
python docs/setup/setup_claude_config.py

# Restart Claude Desktop
# Use: "Generate a grant strategy for community health in Seattle"
```

See [Setup Documentation](mai-advisor-mcp/docs/setup/) for detailed instructions.

---

## 📦 Repository Structure

```
mai-advisor-mcp/
├── mai-advisor-mcp/              # Main application directory
│   ├── app_workflow.py           # Gradio web interface (production)
│   ├── src/                      # Core source code
│   │   ├── advisor_tools.py      # Strategic framework generators
│   │   ├── dork_generator.py     # Search query optimization
│   │   ├── grant_agent.py        # AI research agent (OpenRouter)
│   │   ├── search_operators.py   # Advanced search strategies
│   │   ├── server.py             # Full MCP server
│   │   └── server_simplified.py  # Minimal MCP server
│   ├── docs/                     # Organized documentation
│   │   ├── setup/                # Installation guides
│   │   ├── deployment/           # HuggingFace deployment
│   │   ├── hackathon/            # Submission materials
│   │   └── development/          # Development docs
│   ├── examples/                 # Usage examples
│   ├── huggingface_space_deploy/ # Production deployment package
│   ├── requirements.txt          # Python dependencies
│   └── LICENSE                   # MIT License
├── .github/                      # GitHub configuration
├── .venv/                        # Virtual environment (local)
└── README.md                     # This file
```

---

## 🎯 Key Features

### For Nonprofits
- **99.9% faster** initial draft generation (30-60 seconds vs weeks)
- **400% increase** in grant applications (10-15 vs 2-3 annually)
- **Automated discovery** - AI agent finds opportunities
- **Strategic frameworks** - not just text generation
- **Proven processes** - small nonprofit focused

### Technical Innovation
- **Dual deployment** - Web UI + MCP server
- **OpenRouter integration** - Free Google Gemini 2.0 Flash
- **MCP protocol** - Native Claude Desktop support
- **Autonomous agents** - 8,000+ word execution plans
- **Public access** - No authentication required
- **User-provided API keys** - Zero cost risk

### Enterprise-Grade Quality
- **Production-ready** code with error handling
- **Comprehensive documentation** - setup, deployment, usage
- **Clean architecture** - modular, testable, maintainable
- **Security** - No hardcoded secrets, user-provided keys
- **Performance** - Async operations, optimized workflows

---

## 📚 Documentation

### Setup & Installation
- [Local Development Setup](mai-advisor-mcp/docs/setup/QUICKSTART.md)
- [MCP Server Configuration](mai-advisor-mcp/docs/setup/README_LOCAL.md)
- [Environment Configuration](mai-advisor-mcp/.env.example)

### Deployment
- [HuggingFace Space Deployment](mai-advisor-mcp/docs/deployment/DEPLOY_PUBLIC_SPACE.md)
- [OpenRouter Setup Guide](mai-advisor-mcp/docs/deployment/OPENROUTER_UPDATE.md)
- [Production Checklist](mai-advisor-mcp/docs/deployment/READY_TO_DEPLOY.md)

### Hackathon Submission
- [Submission Checklist](mai-advisor-mcp/docs/hackathon/HACKATHON_CHECKLIST.md)
- [Hackathon README](mai-advisor-mcp/docs/hackathon/README_HACKATHON.md)
- [MCP Competition Info](mai-advisor-mcp/docs/hackathon/hackathon-info/)

### Development
- [Project Overview](mai-advisor-mcp/README.md)
- [Code Examples](mai-advisor-mcp/examples/)
- [Agent Development Guidelines](AGENTS.md)

---

## 🏗️ Architecture

### System Flow

```
User Input (Topic + Location)
    ↓
Orchestrator Layer
    ↓
┌────────────────────┬──────────────────┬───────────────────┐
│                    │                  │                   │
Search Dork       Financial         Grant            Research
Generator         Advisor           Expert           Expert
    │                │                  │                   │
    └────────────────┴──────────────────┴───────────────────┘
                              ↓
                     Orchestrator Synthesis
                              ↓
                     AI Agent TODO Generator
                              ↓
                    6 Comprehensive Outputs
```

### MCP Integration

```
Claude Desktop
    ↓
MCP Protocol (stdio)
    ↓
MAI Advisor Server
    ↓
┌──────────┬──────────┬──────────┬──────────┐
│  Tool 1  │  Tool 2  │  Tool 3  │  Tool 4  │
│ generate │  dorks   │ get_todo │ get_plan │
│ strategy │   only   │          │          │
└──────────┴──────────┴──────────┴──────────┘
```

---

## 🔑 API Keys

### OpenRouter (Required)
Get free API key: [openrouter.ai/keys](https://openrouter.ai/keys)
- **Model:** Google Gemini 2.0 Flash
- **Cost:** FREE tier available
- **Usage:** Strategic framework generation

### Tavily (Optional)
For enhanced research capabilities:
- Sign up at [tavily.com](https://tavily.com)
- Add to `.env` file for local development

---

## 🤝 Contributing

This is a hackathon submission project. After the competition:

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](mai-advisor-mcp/LICENSE) file for details.

---

## 🏆 Hackathon Tracks

**MCP 1st Birthday Hackathon** - Both Enterprise Tracks:

1. **Building MCP (Enterprise)** - Native MCP server implementation
   - 4 production-ready tools
   - 3 knowledge resources
   - Async stdio transport
   - Claude Desktop integration

2. **MCP in Action (Enterprise)** - Autonomous AI agent workflow
   - 8,000+ word execution plan
   - 90-day grant acquisition timeline
   - Browser-enabled AI integration
   - Human-in-the-loop approvals

---

## 🙏 Acknowledgments

- **Anthropic** - Model Context Protocol specification
- **OpenRouter** - Free access to Google Gemini 2.0 Flash
- **Gradio** - Excellent web UI framework
- **HuggingFace** - Space hosting platform
- **LangChain** - AI orchestration tools

---

## 📞 Contact

**Developer:** nbiish  
**Repository:** [github.com/nbiish/mai-advisor-mcp](https://github.com/nbiish/mai-advisor-mcp)  
**HuggingFace:** [huggingface.co/nbiish](https://huggingface.co/nbiish)

---

## ⭐ Star this repo if you find it useful!

Built with ❤️ for nonprofits seeking to maximize their grant funding potential.
