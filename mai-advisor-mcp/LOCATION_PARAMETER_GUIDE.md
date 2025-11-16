# Location Parameter Quick Reference

## Using Location in MAI Advisor MCP

The location parameter is fully integrated into all grant search tools and dork generators.

## Syntax

### Single Location
```json
{
  "topic": "indigenous education",
  "location": "Michigan"
}
```

### Multiple Locations (Comma-Separated)
```json
{
  "topic": "tribal healthcare",
  "location": "Michigan, Minnesota, Wisconsin"
}
```

### Regions
```json
{
  "topic": "native american arts",
  "location": "Pacific Northwest"
}
```

## How Location Works

### In Google Dorks
Locations are converted to quoted phrases with OR logic:
```
"Michigan" OR "Minnesota" OR "Wisconsin"
```

### In Bing Dorks
First location uses the `loc:` operator:
```
loc:"Michigan"
```

### In DuckDuckGo Dorks
All locations are quoted and OR'd:
```
("Michigan" OR "Minnesota" OR "Wisconsin")
```

## Examples

### Example 1: Indigenous Grants in Great Lakes States
```json
{
  "topic": "indigenous tribal grants",
  "location": "Michigan, Minnesota, Wisconsin"
}
```

**Generated Google Dork:**
```
(intext:grant OR inurl:grant OR ... OR inurl:fund OR 
intext:tribal OR intext:indigenous OR ...) 
"tribal" OR "indigenous" OR ... OR "tribal identification" 
"our grant ** process" OR ... OR "consideration" 
"Michigan" OR "Minnesota" OR "Wisconsin"
```

### Example 2: Education Technology in California
```json
{
  "topic": "education technology",
  "location": "California"
}
```

**Generated Google Dork:**
```
(intext:grant OR inurl:grant OR ... OR inurl:fund) 
"education technology" OR "education" OR "technology" 
"our grant ** process" OR ... OR "consideration" 
"California"
```

### Example 3: Healthcare Without Location
```json
{
  "topic": "rural healthcare"
}
```

**Generated Google Dork:**
```
(intext:grant OR inurl:grant OR ... OR inurl:fund) 
"rural healthcare" OR "rural" OR "healthcare" 
"our grant ** process" OR ... OR "consideration"
```
*Note: No location clause added when not specified*

## MCP Tool Usage

### via find_grants Tool
```json
{
  "name": "find_grants",
  "arguments": {
    "topic": "indigenous education technology",
    "location": "Michigan, Minnesota"
  }
}
```

### via search_grants Tool
```json
{
  "name": "search_grants",
  "arguments": {
    "keywords": ["indigenous", "education", "technology"],
    "location": "Michigan, Minnesota",
    "organization_type": "nonprofit"
  }
}
```

## Python API Usage

```python
from src.dork_generator import GrantDorkGenerator

# Single location
dorks = GrantDorkGenerator.generate_all_dorks(
    topic="indigenous healthcare",
    location="Arizona"
)

# Multiple locations
dorks = GrantDorkGenerator.generate_all_dorks(
    topic="tribal education",
    location="Michigan, Minnesota, Wisconsin, Montana"
)

# Access specific engine
google_dork = dorks['google']
```

## Best Practices

### ✅ Do

- Use comma-separated format for multiple locations
- Be specific (state names, regions, cities)
- Include relevant geographic terms in topic if needed
- Test with single location first, then expand

### ❌ Don't

- Don't use complex formatting (just commas)
- Don't include quotes in the input (they're added automatically)
- Don't mix location types (states + countries) without reason
- Don't use too many locations (diminishes precision)

## Location + Identity Context

When combining identity-specific topics with locations:

```json
{
  "topic": "indigenous tribal native american",
  "location": "Michigan, Minnesota"
}
```

Produces comprehensive dork with:
1. Grant terms (intext/inurl)
2. Identity terms (intext/inurl)
3. Identity qualifications (quoted)
4. Process terms (wildcards)
5. **Location terms (quoted OR logic)**

## Testing

Run location tests:
```bash
python3 test_extensive_dorks.py
```

Verify location appears in generated dorks:
```python
assert '"Michigan"' in google_dork
assert '"Minnesota"' in google_dork
```

## Troubleshooting

### Location not appearing in dork?
- Check spelling and spacing
- Verify comma separation
- Review generated output

### Too many/few results?
- Adjust location specificity (state vs. city)
- Combine with other filters (sector, organization_type)
- Test different location combinations

## Files

- **dork_generator.py** - Core location handling
- **advisor_tools.py** - MCP integration
- **server_simplified.py** - Simple interface
- **DORK_GENERATION_GUIDE.md** - Complete guide
