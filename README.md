# MAI Advisor MCP - Workspace

This workspace contains projects for the **MCP's 1st Birthday Hackathon** hosted by Anthropic and Gradio (November 14-30, 2025).

## 📁 Projects

### MAI Advisor MCP 🎯

**Location**: `grant-finder-mcp/`

**Description**: AI-powered Model Context Protocol server for discovering and analyzing grant and funding opportunities using advanced search techniques and deep research capabilities.

**Status**: ✅ Complete and Production-Ready

**Features**:
- Multi-engine search operator generation (Google, Bing, DuckDuckGo)
- AI-powered deep research using Claude Sonnet 4.5
- Full MCP server with 3 tools and 4 resources
- Comprehensive documentation and examples
- Claude Desktop integration ready

**Quick Start**:
```bash
cd grant-finder-mcp
./setup.sh
cp .env.example .env
# Add your API keys to .env
python examples/search_operators_example.py
```

**Documentation**:
- [README.md](grant-finder-mcp/README.md) - Full documentation
- [QUICKSTART.md](grant-finder-mcp/QUICKSTART.md) - 5-minute setup
- [PROJECT_SUMMARY.md](grant-finder-mcp/PROJECT_SUMMARY.md) - Architecture details
- [COMPLETION_SUMMARY.md](grant-finder-mcp/COMPLETION_SUMMARY.md) - What we built

**Stats**:
- 15 files created
- ~2,500 lines of code and documentation
- 3 search engines supported
- 4 complete examples
- Full MCP integration

---

## 🎯 Hackathon Information

### Event Details
- **Duration**: November 14-30, 2025 (17 days)
- **Prize Pool**: $21K USD + Credits + Hardware
- **Registrations**: 6100+ participants
- **Tracks**: 2 main tracks with 3 sub-categories each

### Track Participation

**MAI Advisor MCP** participates in:
- **Track 2: MCP in Action** - Building with existing MCP servers
- **Sub-Category**: Real-world applications using MCP

### Resources
- [Hackathon Details](hackathon-info/mcp-1st-birthday.md)
- [Discord Community](https://discord.gg/fveShqytyh) - Channel: `agents-mcp-hackathon-winter25🏆`
- [Registration Form](https://huggingface.co/spaces/MCP-1st-Birthday/gradio-hackathon-registration-winter25)

---

## 🛠️ Technology Stack

### AI & LLM
- **Anthropic Claude Sonnet 4.5** - Primary AI model
- **LangChain** - Agent framework and orchestration
- **Model Context Protocol (MCP)** - AI integration standard

### Search & Research
- **Tavily** - Advanced web search API
- **Custom search operators** - Google, Bing, DuckDuckGo optimization

### Python Stack
- **Python 3.10+** - Core language
- **Pydantic** - Data validation
- **asyncio** - Async processing

### Development
- **pytest** - Testing
- **black** - Code formatting
- **ruff** - Linting
- **mypy** - Type checking

---

## 📚 Research Foundation

The MAI Advisor MCP is built on cutting-edge AI research:

1. **Open Deep Research** ([GitHub](https://github.com/langchain-ai/open_deep_research))
   - Ranked #6 on Deep Research Bench leaderboard
   - Multi-step planning and execution patterns
   - Context management strategies

2. **LangChain DeepAgents** ([Docs](https://docs.langchain.com/oss/python/deepagents/quickstart))
   - Planning and task decomposition
   - File system tools for context management
   - Subagent spawning capabilities

3. **Nebius AI Platform** ([Token Factory](https://tokenfactory.nebius.com/))
   - Cost-effective model inference
   - High-performance API access

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10 or higher
- API keys:
  - Anthropic (required)
  - Tavily (required)
  - Nebius (optional)

### Installation

```bash
# Navigate to project
cd grant-finder-mcp

# Run automated setup
./setup.sh

# Configure environment
cp .env.example .env
# Edit .env with your API keys

# Test installation
python examples/search_operators_example.py
```

### Quick Test (No API Keys)

```bash
cd grant-finder-mcp
python -m venv venv
source venv/bin/activate
pip install -e .
python examples/search_operators_example.py
```

This generates search queries without needing any API keys!

---

## 📖 Documentation Structure

```
mai-advisor-mcp/
├── hackathon-info/              # Hackathon details and guidelines
│   ├── mcp-1st-birthday.md
│   └── sample*.md
├── grant-finder-mcp/            # Main project
│   ├── src/                     # Source code
│   │   ├── server.py           # MCP server
│   │   ├── grant_agent.py      # AI research agent
│   │   ├── search_operators.py # Search query generators
│   │   └── __init__.py
│   ├── examples/                # Usage examples
│   │   ├── search_operators_example.py
│   │   ├── research_agent_example.py
│   │   └── README.md
│   ├── README.md                # Full documentation
│   ├── QUICKSTART.md            # 5-minute setup
│   ├── PROJECT_SUMMARY.md       # Architecture details
│   ├── COMPLETION_SUMMARY.md    # Build summary
│   ├── pyproject.toml           # Dependencies
│   ├── .env.example             # Config template
│   └── setup.sh                 # Setup script
└── README.md                    # This file
```

---

## 🎓 Use Cases

### 1. Nonprofit Organizations
Find community grants, program funding, operational support

**Example**:
```
Keywords: ["community", "development", "urban renewal"]
Organization: nonprofit
Sector: community development
Location: New York
Funding: $10,000 - $100,000
```

### 2. Research Institutions
Discover federal grants, foundation funding, collaborative opportunities

**Example**:
```
Keywords: ["AI", "machine learning", "computer science"]
Organization: university
Sector: research
Funding: $50,000 - $500,000
```

### 3. Small Businesses
Identify innovation grants, SBIR/STTR, industry-specific funding

**Example**:
```
Keywords: ["small business", "innovation", "technology"]
Organization: business
Sector: technology
Location: California
Funding: $25,000 - $250,000
```

### 4. Individual Artists
Find arts and culture grants, fellowships, project funding

**Example**:
```
Keywords: ["arts", "culture", "creative"]
Organization: individual
Sector: arts
Funding: Up to $50,000
```

---

## 🤝 Contributing

This is a hackathon project, but contributions and feedback are welcome!

### Areas for Enhancement
- Additional search engines (Yahoo, Ecosia, etc.)
- Grant calendar and deadline tracking
- Application progress management
- Email notifications
- Grant writing assistance
- Funder relationship management
- Success rate analytics

---

## 📄 License

MIT License - See [LICENSE](grant-finder-mcp/LICENSE) for details

---

## 🙏 Acknowledgments

### Hackathon Organizers
- **Anthropic** - Claude AI and MCP development
- **Gradio** - Platform and community support
- **Sponsors** - Nebius, Modal, HuggingFace, and others

### Technology Providers
- **LangChain Team** - DeepAgents architecture
- **Tavily** - Advanced search API
- **MCP Community** - Protocol development

### Research Sources
- Open Deep Research project
- LangChain DeepAgents documentation
- Model Context Protocol specification

---

## 📞 Contact & Support

- **Project Issues**: Open an issue in the repository
- **Hackathon Discord**: [Join here](https://discord.gg/fveShqytyh)
- **Documentation**: Check the `grant-finder-mcp/` directory

---

## 🎯 Project Status

**MAI Advisor MCP**: ✅ Complete
- [x] Multi-engine search operators
- [x] AI research agent
- [x] MCP server implementation
- [x] Claude Desktop integration
- [x] Comprehensive documentation
- [x] Working examples
- [x] Setup automation

**Hackathon Submission**: 🚀 Ready
- [x] Code complete
- [x] Documentation complete
- [x] Examples working
- [x] MCP integration verified

---

**Last Updated**: November 14, 2025  
**Hackathon**: MCP's 1st Birthday  
**Built with**: MCP, LangChain, Claude AI, Tavily
