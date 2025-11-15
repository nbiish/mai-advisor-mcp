# MAI Advisor MCP - Project Summary

## 🎯 Project Overview

The **MAI Advisor MCP** is a comprehensive AI-powered Model Context Protocol server designed to help organizations discover and analyze grant and funding opportunities using advanced search techniques and deep research capabilities.

## 📁 Project Structure

```
grant-finder-mcp/
├── src/
│   ├── __init__.py              # Package initialization
│   ├── server.py                # MCP server implementation
│   ├── grant_agent.py           # AI research agent
│   └── search_operators.py      # Search query generators
├── examples/
│   ├── README.md                # Examples documentation
│   ├── search_operators_example.py  # Query generation demo
│   └── research_agent_example.py    # Full research demo
├── pyproject.toml               # Project dependencies
├── .env.example                 # Environment template
├── .gitignore                   # Git ignore rules
├── LICENSE                      # MIT License
├── README.md                    # Main documentation
└── QUICKSTART.md                # 5-minute setup guide
```

## 🔑 Key Components

### 1. Search Operator Generators (`search_operators.py`)

Advanced search query generation for:
- **Google**: 15+ advanced operators including site:, intitle:, filetype:, AROUND()
- **Bing**: Location-based, inbody:, contains:, specialized operators
- **DuckDuckGo**: Privacy-focused queries with essential operators

**Features**:
- Multi-criteria filtering (keywords, location, sector, funding range)
- Automatic trusted source targeting (grants.gov, nsf.gov, etc.)
- File type optimization (PDF, DOC for grant announcements)
- Deadline proximity searches
- Term exclusion capabilities

### 2. Grant Research Agent (`grant_agent.py`)

AI-powered research agent using:
- **LangChain** framework for agent orchestration
- **Anthropic Claude Sonnet 4.5** for analysis
- **Tavily** for advanced web search
- **DeepAgents** architecture patterns

**Capabilities**:
- Basic search: Fast results compilation
- Deep research: AI-analyzed opportunities with fit scoring
- Context management for large result sets
- Markdown/JSON/Text report generation

### 3. MCP Server (`server.py`)

Full Model Context Protocol implementation with:

**Tools**:
- `search_grants`: AI-powered grant discovery
- `generate_search_operators`: Query generation
- `analyze_grant_fit`: Opportunity assessment

**Resources**:
- Getting started guide
- Search operator reference
- Template criteria (nonprofit, research)

**Integration**: Compatible with Claude Desktop, Cline, and other MCP clients

## 🎨 Search Strategy Design

### Multi-Query Approach
Each search generates 2-4 query variations:
1. Main comprehensive query
2. RFP-focused query
3. Open opportunities query
4. Recent announcements query

### Trusted Sources Targeting
Automatically searches within:
- grants.gov (Federal grants database)
- nsf.gov (National Science Foundation)
- nih.gov (National Institutes of Health)
- ed.gov (Department of Education)
- candid.org (Foundation Center)

### Smart Filtering
- Organization type matching
- Sector-specific terminology
- Geographic targeting
- Funding range indicators
- Deadline proximity signals

## 🧠 AI Architecture

Based on cutting-edge research:

### Deep Research Pattern
1. **Planning**: Generate multi-pronged search strategy
2. **Execution**: Run searches across engines and sources
3. **Analysis**: AI evaluates relevance and fit
4. **Synthesis**: Compile ranked opportunities with recommendations

### Context Management
- File system tools for large results
- Summarization for token efficiency
- Structured data extraction

### Subagent Capabilities
Future enhancement: Specialized subagents for:
- Application strategy
- Funder research
- Deadline tracking
- Writing assistance

## 🔬 Research Foundation

### Open Deep Research
- Repository: github.com/langchain-ai/open_deep_research
- Leaderboard ranking: #6 on Deep Research Bench
- Multi-model support
- MCP server integration

### LangChain DeepAgents
- Docs: docs.langchain.com/oss/python/deepagents
- Planning with write_todos tool
- Context offloading to file system
- Persistent memory across sessions

### Nebius AI Platform
- Token factory for efficient inference
- Cost-effective API access
- Alternative to Anthropic/OpenAI

## 📊 Use Cases

### 1. Nonprofit Organizations
Search for community grants, program funding, operational support
- **Input**: Mission, sector, location, budget needs
- **Output**: Ranked opportunities with eligibility assessment

### 2. Research Institutions
Find federal grants, foundation funding, collaborative opportunities
- **Input**: Research area, PI qualifications, budget range
- **Output**: Grant programs with fit analysis

### 3. Small Businesses
Discover innovation grants, SBIR/STTR, industry-specific funding
- **Input**: Business type, innovation area, development stage
- **Output**: Business grant opportunities with application guidance

### 4. Individual Researchers
Identify fellowships, travel grants, equipment funding
- **Input**: Research focus, career stage, institution
- **Output**: Fellowship opportunities with deadline tracking

## 🚀 Deployment Options

### 1. Claude Desktop Integration
```json
{
  "mcpServers": {
    "mai-advisor-mcp": {
      "command": "python",
      "args": ["/path/to/mai-advisor-mcp/grant-finder-mcp/src/server.py"],
      "env": {"ANTHROPIC_API_KEY": "...", "TAVILY_API_KEY": "..."}
    }
  }
}
```

### 2. Standalone Python Usage
```python
from grant_agent import GrantResearchAgent
from search_operators import GrantSearchCriteria

agent = GrantResearchAgent()
results = await agent.research_grants(criteria, depth="deep")
```

### 3. Command Line
```bash
python examples/search_operators_example.py  # Generate queries
python examples/research_agent_example.py     # Full research
```

## 🔧 Technical Stack

### Core Dependencies
- **mcp**: Model Context Protocol SDK
- **langchain**: Agent framework
- **langchain-anthropic**: Claude integration
- **tavily-python**: Advanced search
- **pydantic**: Data validation

### Development Tools
- **pytest**: Testing framework
- **black**: Code formatting
- **ruff**: Fast linting
- **mypy**: Type checking

### Python Version
- Requires: Python 3.10+
- Recommended: Python 3.11

## 📈 Future Enhancements

### Phase 1 (Current)
- [x] Multi-engine search operators
- [x] AI-powered research agent
- [x] MCP server implementation
- [x] Basic grant analysis

### Phase 2 (Planned)
- [ ] Grant calendar and deadline tracking
- [ ] Application progress management
- [ ] Email notifications for new opportunities
- [ ] Integration with grant management systems

### Phase 3 (Future)
- [ ] Grant writing assistance
- [ ] Funder relationship management
- [ ] Success rate analytics
- [ ] Historical grant data analysis
- [ ] Team collaboration features
- [ ] Multi-language support

## 🎓 Learning Resources

### Included Examples
1. **Search Operators Example**: Generate queries without APIs
2. **Research Agent Example**: Full AI-powered research
3. **MCP Integration**: Claude Desktop configuration

### Documentation
- **README.md**: Comprehensive project documentation
- **QUICKSTART.md**: 5-minute setup guide
- **examples/README.md**: Example usage guide
- **In-app resources**: MCP resource endpoints

### External Resources
- LangChain Deep Research Course (academy.langchain.com)
- Open Deep Research GitHub repo
- DeepAgents documentation
- MCP specification and examples

## 🎯 Key Differentiators

1. **Multi-Engine Support**: Unlike single-engine tools, generates optimized queries for Google, Bing, and DuckDuckGo
2. **AI-Powered Analysis**: Goes beyond search to provide fit assessment and strategic recommendations
3. **MCP Integration**: Seamlessly works with Claude and other AI assistants
4. **Research-Backed**: Built on proven DeepAgents architecture patterns
5. **Extensible**: Modular design for easy customization and enhancement

## 📞 Getting Help

### Quick Fixes
- Check `.env` file has correct API keys
- Ensure virtual environment is activated
- Verify Python 3.10+ is installed
- Review examples for usage patterns

### Common Issues
- **Import errors**: Activate virtual environment
- **API errors**: Verify keys in .env
- **No results**: Check internet connection
- **MCP not found**: Verify config file paths

### Resources
- GitHub Issues for bug reports
- Examples directory for code patterns
- Documentation for detailed guides
- MCP resources for built-in help

## 🏆 Success Metrics

The system is designed to:
- **Reduce search time** from hours to minutes
- **Increase opportunity discovery** with multi-engine coverage
- **Improve fit assessment** with AI analysis
- **Streamline application planning** with strategic recommendations

## 📄 License

MIT License - Free for personal and commercial use

## 🙏 Acknowledgments

Built on the shoulders of:
- LangChain Team (DeepAgents framework)
- Anthropic (Claude AI)
- Tavily (Search API)
- Model Context Protocol community

---

**Version**: 0.1.0  
**Created**: November 2025  
**Status**: Production-ready MVP  
**Maintained by**: nbiish
