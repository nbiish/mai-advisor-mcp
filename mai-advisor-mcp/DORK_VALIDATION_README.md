# Search Engine Schema Validation & LLM Guidance System

## Overview

This system ensures that LLMs generate properly formatted "dorks" (advanced search queries) that are correctly translated for Google, Bing, and DuckDuckGo search engines.

## Problem Solved

When LLMs generate search queries, they need to understand:
1. **Search engine-specific operator syntax** - Each engine supports different operators
2. **Proper formatting rules** - Syntax errors break queries
3. **Cross-engine translation** - How to adapt queries between engines

Without this guidance, LLMs may generate invalid queries that don't work or produce poor results.

## Components

### 1. **SEARCH_ENGINE_SCHEMA_GUIDE.md**
Comprehensive documentation of:
- Supported operators for each engine
- Verified examples with explanations
- Common mistakes to avoid
- Translation rules between engines

### 2. **src/dork_validator.py**
Python module providing:

#### Classes:
- **`SearchEngineSchemas`** - Definitive operator schemas for all engines
- **`DorkValidator`** - Validates dorks against engine-specific rules
- **`SearchEngineExamples`** - Verified working examples
- **`LLMDorkGuidance`** - Generates LLM prompts with schema rules

#### Key Functions:
```python
# Get LLM generation guidance
guidance = get_dork_generation_guidance('google')

# Validate a dork
validator = DorkValidator(SearchEngineType.GOOGLE)
result = validator.validate(my_dork)
```

### 3. **Enhanced src/dork_generator.py**
Extended with:
```python
# Generate with validation
results = GrantDorkGenerator.generate_validated_dorks(
    topic="indigenous grants",
    location="Michigan",
    validate=True
)

# Get LLM guidance
guidance = GrantDorkGenerator.get_llm_guidance("all")
```

### 4. **demo_llm_dork_validation.py**
Demonstration script showing:
- How to validate dorks
- How to integrate guidance into LLM prompts
- How to generate properly formatted queries

## Usage

### For LLM Integration

**Step 1: Get Schema Guidance**
```python
from dork_validator import get_dork_generation_guidance

# Get guidance for specific engine
google_guidance = get_dork_generation_guidance('google')
```

**Step 2: Include in System Prompt**
```python
system_prompt = f"""
You are a search expert. Generate search dorks following these rules:

{google_guidance}

User request: {{user_request}}

Generate a properly formatted dork.
"""
```

**Step 3: Validate Generated Dorks**
```python
from dork_validator import DorkValidator, SearchEngineType

validator = DorkValidator(SearchEngineType.GOOGLE)
result = validator.validate(llm_generated_dork)

if not result.is_valid:
    print("Errors:", result.errors)
    print("Suggestions:", result.suggestions)
```

### For Dork Generation

**Generate for All Engines:**
```python
from dork_generator import GrantDorkGenerator

dorks = GrantDorkGenerator.generate_all_dorks(
    topic="community health grants",
    location="California"
)

# Returns: {'google': '...', 'bing': '...', 'duckduckgo': '...'}
```

**Generate with Validation:**
```python
results = GrantDorkGenerator.generate_validated_dorks(
    topic="STEM education",
    location="New York",
    validate=True
)

# Check validation
for engine, data in results.items():
    if data['validation'].is_valid:
        print(f"{engine}: ✓ Valid")
    else:
        print(f"{engine}: ✗ Errors: {data['validation'].errors}")
```

## Search Engine Differences

### Google (Full Support)
- ✓ `intext:`, `inurl:`, `intitle:`
- ✓ Wildcards `*`
- ✓ `OR` operator
- ✓ Complex boolean logic
- ✓ `AROUND(n)` proximity
- ✓ All operators

**Example:**
```
(intext:grant OR inurl:grant OR intext:funding) ("nonprofit" OR "501(c)(3)") ("Michigan") site:grants.gov filetype:pdf
```

### Bing (Modified Syntax)
- ⚠️ Use `inbody:` NOT `intext:`
- ⚠️ Use `loc:` for location
- ⚠️ Use `NOT` or `-` for exclusion
- ✓ Supports most operators
- ✓ Simpler structure preferred

**Example:**
```
(inbody:grant OR inbody:funding) intitle:nonprofit loc:"Michigan" site:grants.gov filetype:pdf
```

### DuckDuckGo (Limited Support)
- ⚠️ NO `OR` operator (unreliable)
- ⚠️ NO `intext:`, `inurl:`
- ⚠️ NO wildcards
- ⚠️ NO complex operators
- ✓ Basic: quotes, `site:`, `filetype:`, `-`
- **Strategy:** Generate multiple simple queries

**Example (Multiple Queries):**
```
Query 1: "nonprofit grant" "Michigan" site:grants.gov filetype:pdf
Query 2: "community funding" "Michigan" site:grants.gov filetype:pdf
Query 3: "501(c)(3) grant" site:grants.gov filetype:pdf
```

## Validation Rules

### Common Syntax Errors

❌ **Wrong:**
```
intext: grant          # Space after colon
"grant OR funding"     # OR inside quotes
site: grants.gov       # Space after colon
or                     # Lowercase OR
```

✅ **Correct:**
```
intext:grant
"grant" OR "funding"
site:grants.gov
OR
```

### Engine-Specific Errors

**Google → Bing:**
- Replace `intext:` with `inbody:`
- Replace `"Location"` with `loc:"Location"`

**Google → DuckDuckGo:**
- Remove `OR` - split into multiple queries
- Remove `intext:`, `inurl:`, wildcards
- Keep only basic operators

## Verified Examples

All examples in `SEARCH_ENGINE_SCHEMA_GUIDE.md` and `dork_validator.py` have been verified to work correctly.

### Indigenous/Tribal Grant Search

**Topic:** "indigenous tribal native american grants"  
**Location:** "Michigan, Minnesota"

**Google:**
```
(intext:grant OR inurl:grant OR intext:tribal OR intext:indigenous) ("tribal" OR "indigenous" OR "native american" OR "federally recognized") ("Michigan" OR "Minnesota") site:grants.gov
```

**Bing:**
```
(inbody:grant OR inbody:tribal OR inbody:indigenous) intitle:grant loc:"Michigan" OR loc:"Minnesota" site:gov
```

**DuckDuckGo:**
```
1. "tribal grant" "Michigan" site:grants.gov filetype:pdf
2. "indigenous funding" "Michigan" site:grants.gov filetype:pdf  
3. "native american grant" "Minnesota" site:grants.gov filetype:pdf
```

## Running the Demo

```bash
cd mai-advisor-mcp
python demo_llm_dork_validation.py
```

This will:
1. Generate dorks for all engines
2. Validate each dork
3. Show LLM guidance examples
4. Demonstrate integration patterns
5. Save guidance to `llm_dork_generation_guidance.txt`

## Integration Checklist

When integrating with an LLM:

- [ ] Include engine-specific guidance in system prompt
- [ ] Specify target search engine clearly
- [ ] Validate LLM output before using
- [ ] Handle validation errors with retry logic
- [ ] For DuckDuckGo, expect multiple queries as output
- [ ] Test with diverse topics to ensure correct formatting

## Files Reference

| File | Purpose |
|------|---------|
| `SEARCH_ENGINE_SCHEMA_GUIDE.md` | Human-readable documentation |
| `src/dork_validator.py` | Validation & guidance module |
| `src/dork_generator.py` | Dork generation with validation |
| `demo_llm_dork_validation.py` | Usage demonstrations |

## LLM System Prompt Template

```
You are generating search queries (dorks) for {search_engine}.

CRITICAL RULES:
{get_dork_generation_guidance(search_engine)}

User Request: {user_request}

Generate a properly formatted dork following ALL the rules above.
```

## Benefits

1. **Consistency** - LLMs generate valid queries every time
2. **Cross-Engine** - Proper translation between search engines
3. **Validation** - Catch errors before execution
4. **Examples** - LLMs learn from verified patterns
5. **Maintainability** - Centralized schema definitions

## Troubleshooting

**Import Error:**
```python
# If dork_validator import fails
# Make sure you're in the src/ directory or add it to path:
import sys
sys.path.insert(0, 'mai-advisor-mcp/src')
```

**Validation Fails:**
```python
# Check validation details
result = validator.validate(dork)
print("Errors:", result.errors)
print("Suggestions:", result.suggestions)
```

**DuckDuckGo Not Working:**
```python
# Remember: DDG needs multiple simple queries
# Don't use OR, intext, wildcards
```

## Future Enhancements

- [ ] Add Yandex, Yahoo support
- [ ] Machine learning validation from search results
- [ ] Auto-repair invalid dorks
- [ ] Performance metrics by engine
- [ ] Query optimization suggestions

## License

Same as parent project (see LICENSE file).
