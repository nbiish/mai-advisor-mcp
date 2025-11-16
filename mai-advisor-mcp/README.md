# MAI Advisor MCP 🎯

AI-powered Model Context Protocol (MCP) server for discovering and analyzing grant and funding opportunities using advanced search techniques and deep research capabilities.

## 🌟 Features

### 🔍 **Extensive Google Dork Generation**
Production-grade search queries with comprehensive coverage:
- **Grant terminology** - 13+ core terms with intext/inurl variations (grant, philanthropy, funding, fellowship, etc.)
- **Identity-aware** - Automatic expansion for indigenous/tribal/native american contexts
- **Process terms** - Wildcards like "our grant ** process" for flexible matching
- **Location targeting** - Comma-separated locations (e.g., "Michigan, Minnesota")
- **Multi-engine support** - Google, Bing, DuckDuckGo optimized queries

### 🤖 **AI-Powered Research**
- Deep research using LangChain's DeepAgents architecture
- Intelligent grant discovery and analysis
- Automated fit assessment
- Strategic recommendations

### 📊 **Comprehensive Grant Analysis**
- Eligibility verification
- Funding amount extraction
- Deadline tracking
- Requirements analysis
- Application strategy guidance

## 🚀 Quick Start

### Prerequisites

- Python 3.10 or higher
- API keys for:
  - Anthropic (Claude) or OpenAI
  - Tavily (for web search)
  - Optional: Nebius for additional AI capabilities

### Installation

```bash
# Clone the repository
cd grant-finder-mcp

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -e .

# Or using uv (faster)
uv venv
source .venv/bin/activate
uv sync
```

### Configuration

1. Copy the example environment file:
```bash
cp .env.example .env
```

2. Edit `.env` and add your API keys:
```bash
ANTHROPIC_API_KEY=your_key_here
TAVILY_API_KEY=your_key_here
# Optional
OPENAI_API_KEY=your_key_here
NEBIUS_API_KEY=your_key_here
```

### Running the Server

```bash
python src/server.py
```

Or configure in Claude Desktop or other MCP clients:

**Claude Desktop Config** (`~/Library/Application Support/Claude/claude_desktop_config.json` on macOS):

```json
{
  "mcpServers": {
    "mai-advisor-mcp": {
      "command": "python",
      "args": ["/path/to/mai-advisor-mcp/grant-finder-mcp/src/server.py"],
      "env": {
        "ANTHROPIC_API_KEY": "your_key",
        "TAVILY_API_KEY": "your_key"
      }
    }
  }
}
```

## 📚 Usage Examples

### Example 1: Search for Education Technology Grants

```python
# Via MCP tool call
{
  "tool": "search_grants",
  "arguments": {
    "keywords": ["education", "technology", "STEM"],
    "organization_type": "nonprofit",
    "sector": "education",
    "location": "California",
    "funding_range_min": 25000,
    "funding_range_max": 250000,
    "depth": "deep"
  }
}
```

### Example 2: Generate Search Operators

```python
{
  "tool": "generate_search_operators",
  "arguments": {
    "keywords": ["climate", "sustainability"],
    "sector": "environmental",
    "engines": ["google", "bing"]
  }
}
```

### Example 3: Analyze Grant Fit

```python
{
  "tool": "analyze_grant_fit",
  "arguments": {
    "grant_description": "NSF SBIR Phase I - $275,000 for innovative technology startups",
    "organization_description": "AI startup developing educational tools for K-12 students",
    "requirements": "Must have working prototype, revenue under $1M, US-based"
  }
}
```

## 🛠️ Architecture

```
grant-finder-mcp/
├── src/
│   ├── server.py              # MCP server implementation
│   ├── grant_agent.py         # AI research agent
│   ├── search_operators.py    # Search query generators
│   └── __init__.py
├── pyproject.toml             # Project dependencies
├── .env.example               # Environment template
├── .gitignore
└── README.md
```

### Technology Stack

- **MCP SDK**: Model Context Protocol for AI integration
- **LangChain**: Agent framework and AI orchestration
- **Anthropic Claude**: Primary AI model (Sonnet 4.5)
- **Tavily**: Advanced web search API
- **Pydantic**: Data validation and settings

## 🎯 Available Tools

### `search_grants`
Comprehensive grant search with AI analysis.

**Input:**
- `keywords` (required): Search terms
- `organization_type`: nonprofit, business, individual, university
- `sector`: education, healthcare, technology, arts, etc.
- `location`: Geographic region
- `funding_range_min/max`: Dollar amounts
- `deadline_months`: Grants due within timeframe
- `exclude_terms`: Terms to filter out
- `depth`: "basic" or "deep" research

**Output:** Formatted report with grant opportunities, analysis, and recommendations

### `generate_search_operators`
Create advanced search engine queries.

**Input:**
- `keywords` (required): Core search terms
- `organization_type`, `sector`, `location`, `funding_range_min/max`
- `engines`: ["google", "bing", "duckduckgo"]

**Output:** Optimized queries for each search engine

### `analyze_grant_fit`
AI-powered grant fit assessment.

**Input:**
- `grant_description` (required): Grant details
- `organization_description` (required): Your organization info
- `requirements`: Eligibility criteria

**Output:** Fit score, strengths, concerns, recommendations, next steps

## 📖 Resources

The MCP server provides built-in resources:

- `grant://guide/getting-started` - Introduction and quick start
- `grant://guide/search-operators` - Search operator reference
- `grant://templates/nonprofit` - Nonprofit search template
- `grant://templates/research` - Research grant template

## 🔬 Research Approach

Based on cutting-edge AI research:

1. **Open Deep Research** ([GitHub](https://github.com/langchain-ai/open_deep_research))
   - Multi-step research planning
   - Context management with file system tools
   - Subagent spawning for specialized tasks

2. **LangChain DeepAgents** ([Docs](https://docs.langchain.com/oss/python/deepagents/quickstart))
   - Planning and task decomposition
   - Long-term memory across sessions
   - Tool-augmented reasoning

3. **Nebius AI Platform** ([Token Factory](https://tokenfactory.nebius.com/))
   - High-performance model inference
   - Cost-effective API access

## 🎓 Advanced Features

### Custom Search Strategies

The system generates multiple search variations:
- RFP-focused queries
- Open opportunity searches
- Recent announcement filters
- Trusted source targeting

### Trusted Grant Sources

Automatically searches within:
- grants.gov (Federal grants)
- nsf.gov (National Science Foundation)
- nih.gov (National Institutes of Health)
- ed.gov (Department of Education)
- candid.org (Foundation Directory)

### File Type Targeting

Prioritizes grant announcements in:
- PDF (formal announcements)
- DOC/DOCX (application templates)
- Web pages (program descriptions)

## 🧪 Development

### Running Tests

```bash
pytest tests/
```

### Code Quality

```bash
# Format code
black src/

# Lint
ruff check src/

# Type checking
mypy src/
```

### Adding New Features

1. Update `search_operators.py` for new search engines
2. Extend `grant_agent.py` for additional AI capabilities
3. Add tools in `server.py` for new MCP functions

## 🤝 Contributing

Contributions welcome! Areas for improvement:

- [ ] Additional search engines (Yahoo, Ecosia, etc.)
- [ ] Grant calendar/deadline tracking
- [ ] Application progress management
- [ ] Grant writing assistance
- [ ] Funder relationship management
- [ ] Success rate analytics

## 📄 License

MIT License - see LICENSE file

## 🙏 Acknowledgments

- **LangChain Team** - DeepAgents architecture
- **Anthropic** - Claude AI models
- **Tavily** - Advanced search API
- **Model Context Protocol** - MCP framework

## 📞 Support

For issues, questions, or feature requests:
- Open an issue on GitHub
- Check documentation resources
- Review example templates

## 🗺️ Roadmap

- [ ] Integration with grant management systems
- [ ] Email notifications for new opportunities
- [ ] Application deadline reminders
- [ ] Grant writing templates and guidance
- [ ] Funder research and profiling
- [ ] Success probability scoring
- [ ] Historical grant data analysis
- [ ] Multi-language support

---

**Built with ❤️ using MCP, LangChain, and Claude AI**

*Last Updated: November 2025*
