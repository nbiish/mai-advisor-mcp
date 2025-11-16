# Search Engine Schema & Operator Validation Guide

## Purpose
This guide provides **verified examples** of search operators for Google, Bing, and DuckDuckGo to ensure LLMs generate properly formatted dorks that translate correctly across search engines.

---

## Table of Contents
1. [Google Search Operators](#google-search-operators)
2. [Bing Search Operators](#bing-search-operators)
3. [DuckDuckGo Search Operators](#duckduckgo-search-operators)
4. [Cross-Engine Translation Rules](#cross-engine-translation-rules)
5. [Validation Examples](#validation-examples)

---

## Google Search Operators

### Supported Operators

| Operator | Purpose | Example | Notes |
|----------|---------|---------|-------|
| `"exact phrase"` | Exact match | `"grant application"` | Always use quotes for multi-word phrases |
| `OR` | Logical OR | `grant OR funding` | Must be UPPERCASE |
| `AND` | Logical AND | `grant AND nonprofit` | Implied by space, rarely needed explicitly |
| `-term` | Exclude | `-loan` | No space after minus |
| `*` | Wildcard | `grant * process` | Matches any word(s) |
| `site:` | Domain search | `site:grants.gov` | No space after colon |
| `filetype:` | File type | `filetype:pdf` | Common: pdf, doc, docx |
| `intitle:` | In title | `intitle:grant` | Single word only |
| `allintitle:` | All in title | `allintitle:grant funding` | All words must be in title |
| `inurl:` | In URL | `inurl:grant` | Single word or use hyphens |
| `allinurl:` | All in URL | `allinurl:grant funding` | All words must be in URL |
| `intext:` | In body | `intext:nonprofit` | Page body text |
| `allintext:` | All in text | `allintext:grant application` | All words in body |
| `AROUND(n)` | Proximity | `grant AROUND(5) application` | Words within n words |
| `..` | Number range | `$10000..$50000` | Numeric ranges |

### Verified Google Examples

#### Example 1: Basic Grant Search
```
"grant application" (nonprofit OR foundation) site:grants.gov filetype:pdf
```
**Translates to:** Find exact phrase "grant application" mentioning nonprofit or foundation on grants.gov in PDF format.

#### Example 2: Indigenous Grant Search (Comprehensive)
```
(intext:grant OR inurl:grant OR intext:funding OR inurl:funding OR intext:tribal OR intext:indigenous OR intext:"native american" OR inurl:tribal OR inurl:indigenous OR inurl:native-american) ("tribal" OR "indigenous" OR "native american" OR "federally recognized" OR "cib") ("application process" OR "how to apply" OR "eligibility") ("Michigan" OR "Minnesota")
```
**Breakdown:**
- **Part 1:** Core terms with intext/inurl variations
- **Part 2:** Identity qualifications (quoted)
- **Part 3:** Process terms (quoted)
- **Part 4:** Location targeting (quoted)

#### Example 3: Wildcard Usage
```
"grant * process" OR "application * deadline" nonprofit
```
**Translates to:** Matches "grant application process", "grant review process", etc.

#### Example 4: Complex Research Grant
```
(research OR "R&D") (grant OR funding OR fellowship) (STEM OR technology OR innovation) site:nsf.gov OR site:nih.gov filetype:pdf -expired
```
**Translates to:** Research grants for STEM from NSF/NIH, excluding expired listings.

---

## Bing Search Operators

### Supported Operators

| Operator | Purpose | Example | Notes |
|----------|---------|---------|-------|
| `"exact phrase"` | Exact match | `"grant funding"` | Same as Google |
| `OR` | Logical OR | `grant OR funding` | Must be UPPERCASE |
| `NOT` | Exclude | `grant NOT loan` | Use NOT instead of minus |
| `-term` | Exclude (alt) | `grant -loan` | Also supported |
| `site:` | Domain search | `site:gov` | Can use TLD |
| `filetype:` | File type | `filetype:pdf` | Same as Google |
| `intitle:` | In title | `intitle:grant` | Single word |
| `inbody:` | In body | `inbody:nonprofit` | **Use instead of intext:** |
| `inanchor:` | In anchor text | `inanchor:grant` | Links pointing to page |
| `loc:` | Location | `loc:"New York"` | **Bing-specific geolocation** |
| `contains:` | Contains term | `contains:deadline` | Broader matching |
| `url:` | URL contains | `url:grant` | Similar to inurl |
| `prefer:` | Prefer term | `prefer:recent` | Boost ranking |

### Verified Bing Examples

#### Example 1: Basic Nonprofit Grant (Bing-Optimized)
```
("grant" OR "funding" OR "fellowship") intitle:nonprofit loc:"Michigan" site:gov filetype:pdf
```
**Key Differences from Google:**
- Uses `loc:` for geographic targeting
- Simpler structure works better
- `site:gov` finds all .gov domains

#### Example 2: Research Grant with Date
```
intitle:(grant OR funding) inbody:"research proposal" (site:nsf.gov OR site:nih.gov) contains:2024 NOT expired
```
**Key Differences:**
- `inbody:` instead of `intext:`
- `contains:` for flexible matching
- `NOT` instead of `-`

#### Example 3: Location-Specific Search
```
"community development" grant loc:"New York" OR loc:"New Jersey" intitle:RFP filetype:pdf
```
**Bing Advantage:** `loc:` provides better geographic targeting than Google's location terms.

#### Example 4: Indigenous Grants (Bing Translation)
```
("grant" OR "funding" OR "application") intitle:tribal OR intitle:indigenous inbody:("federally recognized" OR "native american") loc:Michigan site:gov
```
**Translation Notes:**
- Simplified structure vs Google
- Uses `inbody:` for qualification terms
- `loc:` for location instead of quoted terms

---

## DuckDuckGo Search Operators

### Supported Operators (Limited)

| Operator | Purpose | Example | Notes |
|----------|---------|---------|-------|
| `"exact phrase"` | Exact match | `"grant funding"` | Same as others |
| `site:` | Domain search | `site:grants.gov` | Full domain required |
| `filetype:` | File type | `filetype:pdf` | Same as others |
| `intitle:` | In title | `intitle:grant` | Basic support |
| `-term` | Exclude | `-loan` | Use minus only |
| `region:` | Region code | `region:us-en` | **DDG-specific** |

### NOT Supported (DDG Limitations)
- ❌ `OR` operator (unreliable)
- ❌ `intext:` / `inbody:`
- ❌ `inurl:` (limited)
- ❌ `loc:`
- ❌ Wildcards `*`
- ❌ `AROUND(n)`
- ❌ Complex boolean logic

### Verified DuckDuckGo Examples

#### Example 1: Simple Grant Search (DDG-Optimized)
```
"grant funding" nonprofit "Michigan" site:grants.gov filetype:pdf
```
**Key Points:**
- Keep it simple - no complex operators
- Use exact phrases only
- No OR operator (unreliable)
- Full domain in site:

#### Example 2: Indigenous Grant (DDG Translation)
```
"tribal grant" "native american" "application" site:gov filetype:pdf -loan
```
**Translation Strategy:**
- Combine terms into exact phrases
- Remove OR logic (list alternatives as separate searches)
- Use simple exclusions only

#### Example 3: Multiple Simplified Queries
Since DDG doesn't handle OR well, generate **multiple simple queries** instead:

**Query 1:**
```
"indigenous grant" "Michigan" site:grants.gov filetype:pdf
```

**Query 2:**
```
"tribal funding" "Michigan" site:grants.gov filetype:pdf
```

**Query 3:**
```
"native american grant" "Michigan" site:grants.gov filetype:pdf
```

#### Example 4: Research Grant (DDG)
```
"research grant" STEM site:nsf.gov filetype:pdf
```
**Keep it minimal** - DDG works best with straightforward queries.

---

## Cross-Engine Translation Rules

### From Google to Bing

| Google Operator | Bing Equivalent | Notes |
|----------------|-----------------|-------|
| `intext:` | `inbody:` | Direct replacement |
| `"location"` in query | `loc:"location"` | Use Bing's location operator |
| `-term` | `NOT term` or `-term` | Both work, NOT preferred |
| Complex OR chains | Simplify slightly | Bing handles OR but prefers simpler |
| `allintext:` | `inbody:` | No "all" variant in Bing |

### From Google to DuckDuckGo

| Google Operator | DDG Strategy | Notes |
|----------------|--------------|-------|
| `intext:` / `inurl:` | Remove, use phrases | DDG ignores these |
| `OR` chains | **Split into multiple queries** | Most critical change |
| `*` wildcard | Remove | Not supported |
| Complex boolean | Simplify to phrases | Keep minimal |
| Location in `()` | Use exact phrase `"Location"` | No special operators |

### Universal Translation Algorithm

```python
def translate_dork(google_dork: str, target_engine: str) -> Union[str, List[str]]:
    """
    Translate Google dork to target search engine.
    
    Returns:
        - String for Google/Bing
        - List[str] for DuckDuckGo (multiple simple queries)
    """
    if target_engine == "google":
        return google_dork
    
    elif target_engine == "bing":
        # Replace operators
        bing_dork = google_dork.replace("intext:", "inbody:")
        bing_dork = bing_dork.replace("allintext:", "inbody:")
        
        # Extract location if present
        # Convert: "Michigan" OR "Minnesota" -> loc:"Michigan" OR loc:"Minnesota"
        # (Implementation depends on parser)
        
        return bing_dork
    
    elif target_engine == "duckduckgo":
        # Extract core components
        # - Quoted phrases
        # - site: operators
        # - filetype: operators
        # - Exclusions (-)
        
        # Split OR chains into separate queries
        # Remove unsupported operators
        
        # Return list of simple queries
        return [
            "simple query 1",
            "simple query 2",
            "simple query 3"
        ]
```

---

## Validation Examples

### Test Case 1: Indigenous Tribal Grant Search

**Topic:** "indigenous tribal native american grants"  
**Location:** "Michigan, Minnesota"

#### Google Dork (Full Complexity)
```
(intext:grant OR inurl:grant OR intext:philanthropy OR inurl:philanthropy OR intext:application OR inurl:application OR intext:funding OR inurl:funding OR intext:tribal OR intext:indigenous OR intext:"native american" OR inurl:tribal OR inurl:indigenous OR inurl:native-american) ("tribal" OR "indigenous" OR "native american" OR "federally recognized" OR "cib" OR "state recognized") ("application process" OR "how to apply" OR "eligibility" OR "criteria") ("Michigan" OR "Minnesota")
```

#### Bing Translation
```
(inbody:grant OR inbody:philanthropy OR inbody:application OR inbody:funding OR inbody:tribal OR inbody:indigenous OR inbody:"native american") intitle:(grant OR funding OR tribal) ("federally recognized" OR "native american") ("application process" OR "eligibility") loc:"Michigan" OR loc:"Minnesota" site:gov
```

**Changes:**
- `intext:` → `inbody:`
- Removed `inurl:` (less critical for Bing)
- Added `loc:` for locations
- Simplified overall structure

#### DuckDuckGo Translation (Multiple Queries)

**Query 1:**
```
"tribal grant" "Michigan" site:grants.gov filetype:pdf
```

**Query 2:**
```
"indigenous funding" "Michigan" site:grants.gov filetype:pdf
```

**Query 3:**
```
"native american grant" "Minnesota" site:grants.gov filetype:pdf
```

**Query 4:**
```
"federally recognized" "tribal grant" site:gov filetype:pdf
```

**Changes:**
- Complex OR chain → 4 separate simple queries
- Removed all `intext:` / `inurl:`
- Kept only: exact phrases, site:, filetype:
- Split locations into separate queries

---

### Test Case 2: Research Grant for STEM Education

**Criteria:**
- Keywords: ["STEM education", "K-12", "curriculum"]
- Organization: "nonprofit"
- Amount: $50,000 - $500,000
- Location: "California"

#### Google Dork
```
("STEM education" OR "K-12 STEM" OR "STEM curriculum") (grant OR funding OR fellowship) nonprofit ("$50,000" OR "$100,000" OR "$500,000" OR "six figures") "California" (site:nsf.gov OR site:ed.gov OR site:grants.gov) filetype:pdf
```

#### Bing Translation
```
intitle:(STEM OR education) ("K-12" OR curriculum) (grant OR funding) inbody:nonprofit contains:("$50,000" OR "$100,000") loc:"California" (site:nsf.gov OR site:ed.gov) filetype:pdf
```

#### DuckDuckGo Queries

**Query 1:**
```
"STEM education grant" nonprofit "California" site:nsf.gov filetype:pdf
```

**Query 2:**
```
"K-12 STEM funding" nonprofit "California" site:ed.gov filetype:pdf
```

**Query 3:**
```
"STEM curriculum" grant nonprofit site:grants.gov filetype:pdf
```

---

## LLM Prompt Instructions

### For Google Dork Generation

```
Generate a Google search dork with these components:

1. CORE TERMS with intext/inurl:
   Format: (intext:term1 OR inurl:term1 OR intext:term2 OR inurl:term2 ...)
   
2. QUALIFICATION TERMS (quoted):
   Format: ("exact phrase 1" OR "exact phrase 2" OR "exact phrase 3")
   
3. PROCESS TERMS (with wildcards):
   Format: ("phrase * wildcard" OR "exact phrase" OR "criteria")
   
4. LOCATION (quoted):
   Format: ("Location1" OR "Location2")
   
5. SITE/FILETYPE:
   Format: (site:domain1.gov OR site:domain2.gov) filetype:pdf

Example output:
(intext:grant OR inurl:grant OR intext:funding OR inurl:funding) ("nonprofit" OR "501(c)(3)") ("application * process" OR "how to apply") ("Michigan") site:grants.gov filetype:pdf
```

### For Bing Dork Generation

```
Generate a Bing search dork with these components:

1. USE inbody: instead of intext:
2. USE loc: for geographic targeting
3. USE NOT or - for exclusions
4. Keep structure simpler than Google
5. Use intitle: for key terms

Format:
(inbody:term1 OR inbody:term2) intitle:(keyword1 OR keyword2) ("exact phrase") loc:"Location" site:domain.gov filetype:pdf

Example:
(inbody:grant OR inbody:funding) intitle:(nonprofit OR community) ("application process") loc:"Michigan" site:grants.gov filetype:pdf
```

### For DuckDuckGo Dork Generation

```
Generate multiple simple DuckDuckGo queries (list of 3-5 queries):

RULES:
- Use ONLY: "exact phrases", site:, filetype:, -exclusion
- NO OR operator
- NO intext:, inurl:, wildcards
- Split complex logic into separate queries
- Each query must be self-contained

Format per query:
"main phrase" "secondary phrase" "location" site:domain.gov filetype:pdf -exclusion

Example queries:
1. "nonprofit grant" "Michigan" site:grants.gov filetype:pdf
2. "community funding" "Michigan" site:grants.gov filetype:pdf -loan
3. "501(c)(3) grant" site:grants.gov filetype:pdf
```

---

## Validation Checklist

Before generating dorks, verify:

### Google Checklist
- [ ] All multi-word terms in quotes
- [ ] OR is UPPERCASE
- [ ] `intext:` and `inurl:` properly formatted (no spaces after colon)
- [ ] Parentheses balanced
- [ ] Wildcards `*` used appropriately
- [ ] `site:` has no space after colon
- [ ] `filetype:` valid (pdf, doc, docx)

### Bing Checklist
- [ ] Uses `inbody:` not `intext:`
- [ ] Uses `loc:` for locations
- [ ] Uses `NOT` or `-` for exclusions
- [ ] OR is UPPERCASE
- [ ] Structure is simplified vs Google
- [ ] Valid operators only

### DuckDuckGo Checklist
- [ ] Multiple simple queries generated
- [ ] NO OR operator used
- [ ] NO intext/inurl/wildcards
- [ ] Only exact phrases, site:, filetype:, -
- [ ] Each query is self-contained
- [ ] Queries test different term combinations

---

## Error Prevention

### Common Mistakes

❌ **Wrong (Google):**
```
intext: grant OR funding  // Space after colon
"grant OR funding"        // OR inside quotes
Site:grants.gov          // Capital S
```

✅ **Correct (Google):**
```
intext:grant OR intext:funding
"grant" OR "funding"
site:grants.gov
```

❌ **Wrong (Bing):**
```
intext:grant             // Use inbody
"Michigan" OR "Ohio"     // Use loc:
```

✅ **Correct (Bing):**
```
inbody:grant
loc:"Michigan" OR loc:"Ohio"
```

❌ **Wrong (DuckDuckGo):**
```
(grant OR funding) intext:nonprofit  // Complex operators
"grant * application"                // Wildcard not supported
```

✅ **Correct (DuckDuckGo):**
```
"grant funding" nonprofit
Multiple queries: ["grant nonprofit", "funding nonprofit"]
```

---

## Summary

1. **Google:** Full operator support - use comprehensive dorks with intext/inurl/wildcards
2. **Bing:** Use `inbody:` and `loc:` - slightly simplified structure
3. **DuckDuckGo:** Generate 3-5 simple queries - avoid complex operators entirely

**Key Principle:** Always validate that generated dorks follow the engine-specific syntax rules documented above.
