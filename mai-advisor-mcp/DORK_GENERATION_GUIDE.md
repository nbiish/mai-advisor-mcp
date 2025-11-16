# Extensive Google Dork Generation Guide

## Overview

Our dork generator produces comprehensive, production-grade Google search queries (dorks) designed to find grant opportunities with maximum coverage and precision.

## Key Features

### 1. **Extensive Grant Terminology Coverage**
Every dork includes comprehensive intext/inurl variations for:
- grant, philanthropy, application, funding
- opportunit*, intake, award, fellowship
- unrestricted, guidelines, apply, endowment, fund

### 2. **Identity-Aware Generation**
For identity-specific topics (indigenous, tribal, native american), the generator automatically:
- Adds identity terms to the intext/inurl clause
- Includes comprehensive quoted qualifications
- Covers recognition variants (federally recognized, state recognized, CIB, etc.)

### 3. **Location Integration**
Location parameters are fully integrated:
- Accepts comma-separated locations (e.g., "Michigan, Minnesota")
- Generates quoted location terms for precise targeting
- Works seamlessly across all search engines

### 4. **Process Term Wildcards**
Includes grant process indicators with wildcards:
- "our grant ** process"
- "our ** process"
- Plus specific terms like "consideration", "eligibility", "criteria"

## Example Output

### Indigenous/Tribal Grant Search

**Input:**
```python
topic = "indigenous tribal native american grants"
location = "Michigan, Minnesota"
```

**Output:**
```
(intext:grant OR inurl:grant OR intext:philanthropy OR inurl:philanthropy OR 
intext:application OR inurl:application OR intext:funding OR inurl:funding OR 
intext:opportunit* OR inurl:opportunit* OR intext:intake OR inurl:intake OR 
intext:award OR inurl:award OR intext:fellowship OR inurl:fellowship OR 
intext:unrestricted OR inurl:unrestricted OR intext:guidelines OR 
inurl:guidelines OR intext:apply OR inurl:apply OR intext:endowment OR 
inurl:endowment OR intext:fund OR inurl:fund OR intext:tribal OR 
intext:indigenous OR intext:native american OR intext:first nation OR 
intext:native OR intext:federally recognized OR inurl:tribal OR 
inurl:indigenous OR inurl:native-american OR inurl:first-nation OR 
inurl:native OR inurl:federally-recognized) 
"tribal" OR "indigenous" OR "native" OR "first nation" OR "native american" OR 
"federally recognized" OR "cib" OR "state recognized" OR "tribal citizen" OR 
"tribal id" OR "tribal identification" OR "indigena" 
"our grant ** process" OR "our ** process" OR "application process" OR 
"how to apply" OR "submit application" OR "request for proposals" OR "rfp" OR 
"letter of inquiry" OR "loi" OR "eligibility" OR "criteria" OR "consideration" 
"Michigan" OR "Minnesota"
```

## Dork Structure Breakdown

### Part 1: Core Terms with Operators
```
(intext:grant OR inurl:grant OR intext:funding OR inurl:funding OR ...)
```
- Covers all grant-related terminology
- Uses both intext and inurl for maximum coverage
- Includes wildcards (opportunit*) for variations

### Part 2: Identity Terms (if applicable)
```
OR intext:tribal OR intext:indigenous OR ... OR inurl:native-american OR ...
```
- Appended to Part 1 for identity-specific searches
- Includes both intext and inurl variations
- Handles multi-word terms with hyphens in URLs

### Part 3: Qualification Terms (quoted)
```
"tribal" OR "indigenous" OR "native" OR ... OR "tribal id" OR "indigena"
```
- Exact phrase matching for identity qualifications
- Comprehensive coverage of recognition types
- Includes administrative terms (CIB, tribal ID, etc.)

### Part 4: Process Indicators
```
"our grant ** process" OR "our ** process" OR "consideration" OR ...
```
- Wildcards for flexible matching
- Common grant process terminology
- Application-specific phrases

### Part 5: Location Targeting
```
"Michigan" OR "Minnesota"
```
- Exact phrase matching for locations
- Handles comma-separated input
- OR logic for multi-location searches

## Usage Examples

### Via MCP Tool (find_grants)

```json
{
  "topic": "indigenous education technology",
  "location": "Michigan, Minnesota"
}
```

### Via Python API

```python
from src.dork_generator import GrantDorkGenerator

# Generate all dorks
dorks = GrantDorkGenerator.generate_all_dorks(
    topic="indigenous education",
    location="California, Oregon, Washington"
)

# Access specific engine dorks
google_dork = dorks['google']
bing_dork = dorks['bing']
duckduckgo_dork = dorks['duckduckgo']
```

### Direct Google Search

Copy the generated Google dork and paste directly into Google Search. The extensive query will:
1. Find pages with grant terminology in text/URLs
2. Match identity qualifications
3. Target specific processes
4. Filter by location

## Supported Identity Contexts

The generator automatically detects and expands these identity contexts:

- **indigenous** → tribal, indigenous, native american, first nation, native, federally recognized
- **tribal** → Same as indigenous
- **native** → Same as indigenous  
- **native american** → Same as indigenous

Each context includes comprehensive qualification terms:
- tribal, indigenous, native, first nation, native american
- federally recognized, cib, state recognized
- tribal citizen, tribal id, tribal identification
- indigena

## Multi-Search Engine Support

### Google
- Full extensive format
- All operators (intext, inurl, quoted phrases, wildcards)
- Optimized for maximum coverage

### Bing
- Simplified format using Bing operators
- intitle, inbody, loc operators
- Focused on core terms

### DuckDuckGo
- Basic format for DDG compatibility
- Standard operators only
- Simplified structure

## Best Practices

1. **Be Specific with Topics**: More specific topics generate better-targeted dorks
2. **Use Multiple Locations**: Comma-separate locations for broader geographic coverage
3. **Review Generated Dorks**: Always preview before running extensive searches
4. **Test Incrementally**: Start with one search engine, then expand
5. **Save Results**: Use the MCP tool to automatically save dorks to JSON files

## Testing

Run the comprehensive test suite:

```bash
python3 test_extensive_dorks.py
```

This verifies:
- All key components are present
- Structure matches production examples
- Identity detection works correctly
- Location integration functions properly

## Files

- **dork_generator.py** - Core generation logic
- **advisor_tools.py** - MCP tool integration
- **server_simplified.py** - Simple MCP interface
- **test_extensive_dorks.py** - Comprehensive tests

## Future Enhancements

Potential additions:
- Custom identity maps for other communities
- Funding amount filters
- Deadline proximity operators
- File type targeting (PDF, DOC)
- Site-specific targeting (grants.gov, etc.)
