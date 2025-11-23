# MAI Advisor MCP - Quick Start Guide

## 5-Minute Setup

### Step 1: Get Your API Keys

1. **Tavily API** (Required for search)
   - Visit: https://www.tavily.com/
   - Sign up for free account
   - Get API key from dashboard

2. **Anthropic API** (Required for AI analysis)
   - Visit: https://console.anthropic.com/
   - Create account
   - Generate API key
   - Note: Requires credits/payment

3. **Optional: Nebius** (For additional AI capabilities)
   - Visit: https://tokenfactory.nebius.com/
   - Follow sign-up process

### Step 2: Install

```bash
cd grant-finder-mcp
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -e .
```

### Step 3: Configure

```bash
cp .env.example .env
nano .env  # Or use your favorite editor
```

Add your keys:
```
ANTHROPIC_API_KEY=sk-ant-xxxxx
TAVILY_API_KEY=tvly-xxxxx
```

### Step 4: Test

```bash
# Test search operators (no API needed)
python examples/search_operators_example.py

# Test full research (requires APIs)
python examples/research_agent_example.py
```

### Step 5: Use with Claude Desktop

Edit `~/Library/Application Support/Claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "mai-advisor-mcp": {
      "command": "python",
      "args": ["/FULL/PATH/TO/mai-advisor-mcp/grant-finder-mcp/src/server.py"],
      "env": {
        "ANTHROPIC_API_KEY": "your-key",
        "TAVILY_API_KEY": "your-key"
      }
    }
  }
}
```

Restart Claude Desktop.

## Your First Grant Search

In Claude Desktop:

```
I need to find grants for my nonprofit that works on 
education technology in California. We're looking for 
$25,000 to $250,000 in funding.
```

Claude will use the MAI Advisor MCP tools automatically!

## Troubleshooting

**"Import errors"**: Make sure you're in the virtual environment
```bash
source venv/bin/activate
```

**"API key errors"**: Check `.env` file has correct keys with no quotes

**"No results"**: Check your internet connection and API key validity

**"Claude doesn't see the MCP"**: 
- Verify config file path is correct
- Check full absolute path to server.py
- Restart Claude Desktop

## Next Steps

- Read full [README.md](README.md) for advanced features
- Explore [examples/](examples/) directory
- Customize search strategies in `src/search_operators.py`
- Extend AI prompts in `src/grant_agent.py`

## Common Use Cases

### Academic Research Grants
```python
keywords = ["research", "science", "innovation"]
organization_type = "university"
sector = "research"
funding_range_min = 50000
```

### Small Business Grants
```python
keywords = ["small business", "entrepreneurship"]
organization_type = "business"
location = "your state"
funding_range_max = 100000
```

### Arts & Culture
```python
keywords = ["arts", "culture", "creative"]
sector = "arts"
organization_type = "nonprofit"
```

### Environmental/Sustainability
```python
keywords = ["climate", "sustainability", "renewable"]
sector = "environmental"
```

## Support

- Check examples in `examples/` folder
- Read resource guides via MCP
- Review search operator documentation
- Test with basic searches first

Happy grant hunting! 🎯
