# 🎉 MAI Advisor MCP - Complete!

## ✅ What We Built

A comprehensive **AI-powered grant and funding opportunity finder** using:
- Model Context Protocol (MCP) server
- Advanced search operator generation for Google, Bing, DuckDuckGo
- Deep research capabilities using LangChain's DeepAgents architecture
- Integration with Claude AI and Tavily search

---

## 📦 Project Components

### Core Files Created

1. **`src/search_operators.py`** (430+ lines)
   - Google search operator generator with 15+ advanced operators
   - Bing search operator generator with location targeting
   - DuckDuckGo privacy-focused search generator
   - Unified interface for all search engines
   - Smart filtering by organization, sector, location, funding range

2. **`src/grant_agent.py`** (270+ lines)
   - AI research agent using Claude Sonnet 4.5
   - Deep research with multi-step planning
   - Context management for large results
   - Report generation in Markdown/JSON/Text formats
   - Integration with Tavily search API

3. **`src/server.py`** (400+ lines)
   - Full MCP server implementation
   - Three main tools: `search_grants`, `generate_search_operators`, `analyze_grant_fit`
   - Four built-in resources with guides and templates
   - Compatible with Claude Desktop and other MCP clients

4. **`src/__init__.py`**
   - Package initialization with clean exports

### Configuration Files

5. **`pyproject.toml`**
   - Project metadata and dependencies
   - Dev tools configuration (black, ruff, mypy)
   - Python 3.10+ requirement

6. **`.env.example`**
   - Template for API keys (Anthropic, Tavily, Nebius)
   - MCP server configuration
   - Research agent settings

7. **`.gitignore`**
   - Python, virtual environments, IDE files
   - Environment variables, logs, cache

### Documentation

8. **`README.md`** (300+ lines)
   - Comprehensive project documentation
   - Features, quick start, usage examples
   - Architecture overview, technical stack
   - Advanced features and roadmap

9. **`QUICKSTART.md`** (150+ lines)
   - 5-minute setup guide
   - Step-by-step API key setup
   - Claude Desktop integration
   - Common use cases and troubleshooting

10. **`PROJECT_SUMMARY.md`** (350+ lines)
    - Complete project overview
    - Architecture deep dive
    - Research foundation explanation
    - Future enhancements and roadmap

11. **`LICENSE`**
    - MIT License for open source distribution

### Examples

12. **`examples/search_operators_example.py`**
    - 4 different grant search scenarios
    - Demonstrates query generation for all engines
    - No API keys required to run

13. **`examples/research_agent_example.py`**
    - Basic and deep research examples
    - Full AI-powered analysis demonstration
    - Requires API keys (Tavily + Anthropic)

14. **`examples/README.md`**
    - Guide to running examples
    - Customization instructions
    - Expected output descriptions

### Setup Tools

15. **`setup.sh`**
    - Automated setup script
    - Virtual environment creation
    - Dependency installation
    - Next steps guidance

---

## 🎯 Key Features Implemented

### 1. Multi-Engine Search Operators ✅

**Google Operators**:
- Exact phrase matching with "quotes"
- Site restrictions: `site:grants.gov`
- Title filtering: `intitle:grant`
- File type targeting: `filetype:pdf`
- Proximity matching: `AROUND(n)`
- Boolean logic: OR, AND
- Exclusion: `-term`
- Multiple query variations per search

**Bing Operators**:
- Location targeting: `loc:"California"`
- Body content: `inbody:term`
- Page content: `contains:term`
- Date-restricted queries
- Trusted source filtering

**DuckDuckGo Operators**:
- Privacy-focused queries
- Simplified operator set
- Site restrictions
- Title and content filtering

### 2. AI Research Agent ✅

**Basic Search Mode**:
- Fast compilation of results
- Multiple search engine queries
- Result aggregation
- Quick overview generation

**Deep Research Mode**:
- AI-powered analysis using Claude Sonnet 4.5
- Relevance scoring and ranking
- Fit assessment with reasoning
- Strategic recommendations
- Actionable next steps
- Comprehensive markdown reports

### 3. MCP Server Integration ✅

**Tools**:
- `search_grants`: Full grant discovery with AI
- `generate_search_operators`: Query generation only
- `analyze_grant_fit`: Opportunity assessment

**Resources**:
- Getting started guide
- Search operator reference
- Nonprofit template
- Research template

**Compatibility**:
- Claude Desktop
- Cline
- Any MCP-compatible client

### 4. Grant Search Capabilities ✅

**Filtering Options**:
- Keywords (required)
- Organization type (nonprofit, business, university, individual)
- Sector (education, healthcare, technology, arts, etc.)
- Geographic location
- Funding range (min/max)
- Deadline proximity (within X months)
- Term exclusion

**Trusted Sources**:
- grants.gov (Federal grants)
- nsf.gov (NSF)
- nih.gov (NIH)
- ed.gov (Education)
- candid.org (Foundation Center)

**Output Formats**:
- Markdown reports
- JSON data
- Plain text
- Structured analysis

---

## 🔬 Technical Architecture

### Research Foundation

Based on cutting-edge AI research:

1. **Open Deep Research** (github.com/langchain-ai/open_deep_research)
   - Ranked #6 on Deep Research Bench leaderboard
   - Multi-step planning and execution
   - Context management strategies

2. **LangChain DeepAgents** (docs.langchain.com/oss/python/deepagents)
   - Planning with todo tools
   - File system for context offloading
   - Subagent spawning capabilities
   - Long-term memory support

3. **Nebius AI Platform** (tokenfactory.nebius.com)
   - Cost-effective model inference
   - Alternative to Anthropic/OpenAI
   - High-performance API access

### Technology Stack

**Core**:
- Python 3.10+
- MCP SDK 1.0+
- LangChain 0.3+
- Pydantic 2.0+ for validation

**AI Models**:
- Anthropic Claude Sonnet 4.5 (default)
- OpenAI GPT-4 (optional)
- Nebius models (optional)

**Search**:
- Tavily API for advanced search
- Multi-engine query generation
- Structured data extraction

**Development**:
- pytest for testing
- black for formatting
- ruff for linting
- mypy for type checking

---

## 📊 Usage Scenarios

### Nonprofit Organizations
```
Find community development grants in New York
$10,000 - $100,000, deadlines within 6 months
```

### Research Institutions
```
Discover AI/ML research grants
$50,000 - $500,000, for university researchers
```

### Small Businesses
```
Search for innovation grants in California
Technology sector, $25,000 - $250,000
```

### Individual Artists
```
Find arts and culture grants
Under $50,000, deadlines within 3 months
```

---

## 🚀 Getting Started

### Quick Setup (5 minutes)

```bash
cd grant-finder-mcp
./setup.sh  # Automated setup
cp .env.example .env
# Edit .env with your API keys
python examples/search_operators_example.py
```

### API Keys Needed

1. **Tavily** (Required): https://www.tavily.com/
2. **Anthropic** (Required): https://console.anthropic.com/
3. **Nebius** (Optional): https://tokenfactory.nebius.com/

### Claude Desktop Integration

Add to `~/Library/Application Support/Claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "mai-advisor-mcp": {
      "command": "python",
      "args": ["/full/path/to/mai-advisor-mcp/grant-finder-mcp/src/server.py"],
      "env": {
        "ANTHROPIC_API_KEY": "your-key",
        "TAVILY_API_KEY": "your-key"
      }
    }
  }
}
```

---

## 📈 What's Next

### Immediate Use
1. Run examples to see capabilities
2. Generate search queries for manual use
3. Integrate with Claude Desktop for AI assistance
4. Customize search criteria for your needs

### Future Enhancements
- Grant calendar and deadline tracking
- Application progress management
- Email notifications for new grants
- Grant writing assistance
- Funder relationship management
- Success rate analytics
- Historical data analysis

---

## 🎓 Learning Resources

### Included Documentation
- **README.md**: Full project documentation
- **QUICKSTART.md**: 5-minute setup
- **PROJECT_SUMMARY.md**: Architecture deep dive
- **examples/README.md**: Example usage

### External Resources
- LangChain Deep Research Course
- Open Deep Research GitHub
- DeepAgents documentation
- MCP specification

---

## 🏆 Key Achievements

✅ **Multi-engine search** with 3 search engines supported  
✅ **AI-powered analysis** using Claude Sonnet 4.5  
✅ **MCP integration** for seamless AI assistant use  
✅ **Research-backed** using proven DeepAgents patterns  
✅ **Production-ready** with complete documentation  
✅ **Extensible** modular design for customization  
✅ **Open source** MIT License for free use  

---

## 📞 Support

- **Documentation**: Check README.md and QUICKSTART.md
- **Examples**: Review examples/ directory
- **Issues**: Open GitHub issues for bugs
- **Questions**: Review PROJECT_SUMMARY.md for architecture

---

## 📄 File Manifest

```
grant-finder-mcp/
├── src/                          # Source code (4 files)
│   ├── __init__.py
│   ├── server.py                 # 400+ lines
│   ├── grant_agent.py            # 270+ lines
│   └── search_operators.py       # 430+ lines
├── examples/                      # Examples (3 files)
│   ├── README.md
│   ├── search_operators_example.py
│   └── research_agent_example.py
├── pyproject.toml                # Dependencies
├── .env.example                  # Config template
├── .gitignore                    # Git rules
├── setup.sh                      # Setup script
├── LICENSE                       # MIT License
├── README.md                     # Main docs (300+ lines)
├── QUICKSTART.md                 # Quick start (150+ lines)
└── PROJECT_SUMMARY.md            # Summary (350+ lines)
```

**Total**: 15 files, ~2,000+ lines of code and documentation

---

## 🎯 Summary

We've successfully created a **complete, production-ready MCP server** for AI-powered grant discovery that:

1. ✅ Generates optimized search queries for Google, Bing, DuckDuckGo
2. ✅ Uses Claude AI for deep research and analysis
3. ✅ Integrates seamlessly with Claude Desktop via MCP
4. ✅ Includes comprehensive documentation and examples
5. ✅ Supports multiple use cases (nonprofits, research, business, arts)
6. ✅ Built on proven research (DeepAgents, Open Deep Research)
7. ✅ Ready for immediate use and future extension

**Built with ❤️ using MCP, LangChain, Claude AI, and Tavily**

---

*MAI Advisor MCP v0.1.0 - November 2025*
