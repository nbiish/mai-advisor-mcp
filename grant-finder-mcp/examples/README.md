# Grant Research Examples

This directory contains example scripts demonstrating the MAI Advisor MCP capabilities.

## Examples

### 1. `search_operators_example.py`
Demonstrates generating advanced search queries for multiple search engines.

**No API keys required** - just generates query strings.

```bash
python search_operators_example.py
```

**Output**: Formatted search queries for Google, Bing, and DuckDuckGo that you can copy and paste.

**Examples included**:
- Nonprofit community development grants
- STEM research grants
- Small business innovation grants
- Arts and culture grants

---

### 2. `research_agent_example.py`
Demonstrates full AI-powered grant research capabilities.

**Requires**: TAVILY_API_KEY and ANTHROPIC_API_KEY in `.env`

```bash
python research_agent_example.py
```

**Examples included**:
- Basic grant search (quick results)
- Deep research with AI analysis (comprehensive)
- Query generation without execution

**Output**: 
- Search results count
- AI-generated analysis report
- Formatted recommendations

---

## Running Examples

### Without API Keys
```bash
# Just generate search queries
python search_operators_example.py
```

### With API Keys
```bash
# Full research capabilities
python research_agent_example.py
```

### Customize

Edit the example files to try different search criteria:

```python
criteria = GrantSearchCriteria(
    keywords=["YOUR", "KEYWORDS"],
    organization_type="YOUR_TYPE",  # nonprofit, business, etc.
    sector="YOUR_SECTOR",           # education, healthcare, etc.
    location="YOUR_LOCATION",
    funding_range_min=AMOUNT,
    funding_range_max=AMOUNT
)
```

## Example Output

### Search Operators Example
```
=== GENERATED GRANT SEARCH QUERIES ===

## GOOGLE Search Queries
--------------------------------------------------
Query 1:
  ("education" OR "technology" OR "STEM") (grant OR funding OR fellowship) ...
```

### Research Agent Example
```
# Grant Research Report

## Search Criteria
- Keywords: education, technology, STEM
- Organization Type: nonprofit
- Sector: education

## Analysis
Based on the search results, here are the top grant opportunities...
```

## Next Steps

After reviewing examples:
1. Modify criteria to match your needs
2. Run the MCP server: `python src/server.py`
3. Connect via Claude Desktop or other MCP client
4. Start finding grants with AI assistance!
