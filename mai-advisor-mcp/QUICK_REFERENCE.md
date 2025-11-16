# Quick Reference: LLM Dork Generation & Validation

## Setup

```python
from dork_validator import (
    SearchEngineType, 
    DorkValidator,
    get_dork_generation_guidance
)
from dork_generator import GrantDorkGenerator
```

## Get LLM Guidance (Include in System Prompts)

```python
# For specific engine
guidance = get_dork_generation_guidance('google')

# For all engines
all_guidance = GrantDorkGenerator.get_llm_guidance("all")
```

## Generate Dorks

```python
# Basic generation
dorks = GrantDorkGenerator.generate_all_dorks(
    topic="indigenous grants",
    location="Michigan"
)
# Returns: {'google': '...', 'bing': '...', 'duckduckgo': '...'}

# With validation
results = GrantDorkGenerator.generate_validated_dorks(
    topic="STEM education", 
    location="California",
    validate=True
)
# Returns: {'google': {'dork': '...', 'validation': ValidationResult}}
```

## Validate Dorks

```python
validator = DorkValidator(SearchEngineType.GOOGLE)
result = validator.validate(my_dork)

if result.is_valid:
    print("✓ Valid dork")
else:
    print("Errors:", result.errors)
    print("Suggestions:", result.suggestions)
```

## Search Engine Rules

### Google ✓ Full Support
- Use: `intext:`, `inurl:`, `intitle:`, `*`, `OR`, `AROUND(n)`
- Example: `(intext:grant OR inurl:grant) "nonprofit" site:grants.gov`

### Bing ⚠️ Modified
- Use `inbody:` NOT `intext:`
- Use `loc:"Location"` for geography
- Example: `(inbody:grant) intitle:nonprofit loc:"Michigan" site:gov`

### DuckDuckGo ⚠️ Limited
- NO `OR`, `intext:`, wildcards
- Generate 3-5 simple queries
- Example: `["tribal grant" "Michigan" site:grants.gov`, ...]

## Common Errors

❌ `intext: grant` - Space after colon  
✓ `intext:grant`

❌ `"grant OR funding"` - OR inside quotes  
✓ `"grant" OR "funding"`

❌ `or` - Lowercase  
✓ `OR`

## LLM Integration Pattern

```python
# 1. Get schema guidance
guidance = get_dork_generation_guidance('google')

# 2. Build prompt
prompt = f"""
Generate Google dork for: {user_query}

{guidance}

Follow ALL rules above.
"""

# 3. Generate
dork = llm.generate(prompt)

# 4. Validate
validator = DorkValidator(SearchEngineType.GOOGLE)
result = validator.validate(dork)

# 5. Use or retry
if result.is_valid:
    search(dork)
else:
    retry_with_errors(result.errors)
```

## Demo

```bash
python demo_llm_dork_validation.py
```

## Files

- `SEARCH_ENGINE_SCHEMA_GUIDE.md` - Full reference
- `DORK_VALIDATION_README.md` - User guide
- `src/dork_validator.py` - Validation module
- `demo_llm_dork_validation.py` - Examples
