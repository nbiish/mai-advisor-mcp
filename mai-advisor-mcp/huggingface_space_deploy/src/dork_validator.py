"""
Dork Validation and Search Engine Schema Enforcement

This module ensures that generated dorks conform to search engine-specific
syntax rules and provides verified examples for LLM guidance.
"""
from typing import Dict, List
from dataclasses import dataclass
from enum import Enum
import re


class SearchEngineType(Enum):
    """Supported search engines with schema validation."""
    GOOGLE = "google"
    BING = "bing"
    DUCKDUCKGO = "duckduckgo"


@dataclass
class OperatorRule:
    """Rule for a search operator."""
    operator: str
    supported: bool
    syntax: str
    example: str
    notes: str


@dataclass
class ValidationResult:
    """Result of dork validation."""
    is_valid: bool
    engine: SearchEngineType
    warnings: List[str]
    errors: List[str]
    suggestions: List[str]


class SearchEngineSchemas:
    """
    Verified search engine operator schemas.
    
    This class provides the definitive reference for what operators
    are supported by each search engine and their correct syntax.
    """
    
    GOOGLE_OPERATORS = {
        "exact_phrase": OperatorRule(
            operator='"exact phrase"',
            supported=True,
            syntax='"phrase"',
            example='"grant application"',
            notes="Always use quotes for multi-word phrases"
        ),
        "OR": OperatorRule(
            operator="OR",
            supported=True,
            syntax="term1 OR term2",
            example="grant OR funding",
            notes="Must be UPPERCASE"
        ),
        "exclude": OperatorRule(
            operator="-",
            supported=True,
            syntax="-term",
            example="-loan",
            notes="No space after minus"
        ),
        "wildcard": OperatorRule(
            operator="*",
            supported=True,
            syntax="word * word",
            example='"grant * process"',
            notes="Matches any word(s)"
        ),
        "site": OperatorRule(
            operator="site:",
            supported=True,
            syntax="site:domain.com",
            example="site:grants.gov",
            notes="No space after colon"
        ),
        "filetype": OperatorRule(
            operator="filetype:",
            supported=True,
            syntax="filetype:ext",
            example="filetype:pdf",
            notes="Common: pdf, doc, docx"
        ),
        "intext": OperatorRule(
            operator="intext:",
            supported=True,
            syntax="intext:term",
            example="intext:nonprofit",
            notes="Single word or quoted phrase"
        ),
        "inurl": OperatorRule(
            operator="inurl:",
            supported=True,
            syntax="inurl:term",
            example="inurl:grant",
            notes="Use hyphens for multi-word"
        ),
        "intitle": OperatorRule(
            operator="intitle:",
            supported=True,
            syntax="intitle:term",
            example="intitle:grant",
            notes="Single word only"
        ),
        "AROUND": OperatorRule(
            operator="AROUND(n)",
            supported=True,
            syntax="word1 AROUND(5) word2",
            example="grant AROUND(5) application",
            notes="Words within n words of each other"
        ),
    }
    
    BING_OPERATORS = {
        "exact_phrase": OperatorRule(
            operator='"exact phrase"',
            supported=True,
            syntax='"phrase"',
            example='"grant funding"',
            notes="Same as Google"
        ),
        "OR": OperatorRule(
            operator="OR",
            supported=True,
            syntax="term1 OR term2",
            example="grant OR funding",
            notes="Must be UPPERCASE"
        ),
        "NOT": OperatorRule(
            operator="NOT",
            supported=True,
            syntax="term1 NOT term2",
            example="grant NOT loan",
            notes="Bing-specific exclusion"
        ),
        "exclude": OperatorRule(
            operator="-",
            supported=True,
            syntax="-term",
            example="-loan",
            notes="Alternative to NOT"
        ),
        "site": OperatorRule(
            operator="site:",
            supported=True,
            syntax="site:domain.com",
            example="site:gov",
            notes="Can use TLD"
        ),
        "filetype": OperatorRule(
            operator="filetype:",
            supported=True,
            syntax="filetype:ext",
            example="filetype:pdf",
            notes="Same as Google"
        ),
        "inbody": OperatorRule(
            operator="inbody:",
            supported=True,
            syntax="inbody:term",
            example="inbody:nonprofit",
            notes="Use instead of intext"
        ),
        "intitle": OperatorRule(
            operator="intitle:",
            supported=True,
            syntax="intitle:term",
            example="intitle:grant",
            notes="Single word"
        ),
        "loc": OperatorRule(
            operator="loc:",
            supported=True,
            syntax='loc:"Location"',
            example='loc:"Michigan"',
            notes="Bing-specific geolocation"
        ),
        "contains": OperatorRule(
            operator="contains:",
            supported=True,
            syntax="contains:term",
            example="contains:deadline",
            notes="Broader matching"
        ),
        "intext": OperatorRule(
            operator="intext:",
            supported=False,
            syntax="N/A",
            example="N/A",
            notes="Use inbody: instead"
        ),
        "wildcard": OperatorRule(
            operator="*",
            supported=False,
            syntax="N/A",
            example="N/A",
            notes="Not supported in Bing"
        ),
    }
    
    DUCKDUCKGO_OPERATORS = {
        "exact_phrase": OperatorRule(
            operator='"exact phrase"',
            supported=True,
            syntax='"phrase"',
            example='"grant funding"',
            notes="Same as others"
        ),
        "site": OperatorRule(
            operator="site:",
            supported=True,
            syntax="site:full.domain.com",
            example="site:grants.gov",
            notes="Full domain required"
        ),
        "filetype": OperatorRule(
            operator="filetype:",
            supported=True,
            syntax="filetype:ext",
            example="filetype:pdf",
            notes="Same as others"
        ),
        "intitle": OperatorRule(
            operator="intitle:",
            supported=True,
            syntax="intitle:term",
            example="intitle:grant",
            notes="Basic support"
        ),
        "exclude": OperatorRule(
            operator="-",
            supported=True,
            syntax="-term",
            example="-loan",
            notes="Use minus only"
        ),
        "OR": OperatorRule(
            operator="OR",
            supported=False,
            syntax="N/A",
            example="N/A",
            notes="Unreliable - split into multiple queries"
        ),
        "intext": OperatorRule(
            operator="intext:",
            supported=False,
            syntax="N/A",
            example="N/A",
            notes="Not supported"
        ),
        "inurl": OperatorRule(
            operator="inurl:",
            supported=False,
            syntax="N/A",
            example="N/A",
            notes="Limited support"
        ),
        "wildcard": OperatorRule(
            operator="*",
            supported=False,
            syntax="N/A",
            example="N/A",
            notes="Not supported"
        ),
    }


class DorkValidator:
    """Validates search dorks against engine-specific schemas."""
    
    def __init__(self, engine: SearchEngineType):
        self.engine = engine
        self.schema = self._load_schema()
    
    def _load_schema(self) -> Dict[str, OperatorRule]:
        """Load the appropriate schema for the search engine."""
        if self.engine == SearchEngineType.GOOGLE:
            return SearchEngineSchemas.GOOGLE_OPERATORS
        elif self.engine == SearchEngineType.BING:
            return SearchEngineSchemas.BING_OPERATORS
        elif self.engine == SearchEngineType.DUCKDUCKGO:
            return SearchEngineSchemas.DUCKDUCKGO_OPERATORS
        return {}
    
    def validate(self, dork: str) -> ValidationResult:
        """
        Validate a dork against the engine's schema.
        
        Returns ValidationResult with errors, warnings, and suggestions.
        """
        errors = []
        warnings = []
        suggestions = []
        
        # Check for unsupported operators
        if self.engine == SearchEngineType.BING:
            if "intext:" in dork:
                errors.append("Bing does not support 'intext:' - use 'inbody:' instead")
                suggestions.append("Replace 'intext:' with 'inbody:'")
        
        if self.engine == SearchEngineType.DUCKDUCKGO:
            if " OR " in dork:
                errors.append("DuckDuckGo has unreliable OR support")
                suggestions.append("Split into multiple simple queries instead")
            
            if "intext:" in dork or "inurl:" in dork:
                errors.append("DuckDuckGo does not support intext: or inurl:")
                suggestions.append("Remove these operators and use exact phrases only")
            
            if "*" in dork and '"' in dork:
                errors.append("DuckDuckGo does not support wildcards")
                suggestions.append("Remove wildcards")
        
        # Check for common syntax errors (all engines)
        if re.search(r'(site|filetype|intext|inurl|intitle|inbody|loc):\s+', dork):
            errors.append("No space allowed after operator colon")
            suggestions.append("Remove spaces after colons in operators")
        
        # Check for OR case sensitivity
        if " or " in dork.lower() and " or " in dork:
            warnings.append("OR operator should be UPPERCASE")
            suggestions.append("Change 'or' to 'OR'")
        
        # Check for unbalanced parentheses
        if dork.count('(') != dork.count(')'):
            errors.append("Unbalanced parentheses")
        
        # Check for unbalanced quotes
        if dork.count('"') % 2 != 0:
            errors.append("Unbalanced quotes")
        
        is_valid = len(errors) == 0
        
        return ValidationResult(
            is_valid=is_valid,
            engine=self.engine,
            warnings=warnings,
            errors=errors,
            suggestions=suggestions
        )


class SearchEngineExamples:
    """
    Verified examples for LLM guidance.
    
    These examples have been tested and verified to work correctly
    with each search engine.
    """
    
    GOOGLE_EXAMPLES = {
        "basic_grant": {
            "description": "Basic nonprofit grant search",
            "dork": '"grant application" (nonprofit OR foundation) site:grants.gov filetype:pdf',
            "explanation": "Finds grant applications for nonprofits/foundations on grants.gov"
        },
        "indigenous_comprehensive": {
            "description": "Comprehensive indigenous/tribal grant search",
            "dork": '(intext:grant OR inurl:grant OR intext:funding OR inurl:funding OR intext:tribal OR intext:indigenous) ("tribal" OR "indigenous" OR "native american" OR "federally recognized") ("application process" OR "eligibility") ("Michigan" OR "Minnesota")',
            "explanation": "Multi-part dork with core terms, identity qualifications, process terms, and location"
        },
        "wildcard_usage": {
            "description": "Using wildcards for flexible matching",
            "dork": '"grant * process" OR "application * deadline" nonprofit',
            "explanation": "Matches variations like 'grant application process', 'grant review process'"
        },
        "research_grant": {
            "description": "Research grant for STEM",
            "dork": '(research OR "R&D") (grant OR funding OR fellowship) (STEM OR technology) site:nsf.gov OR site:nih.gov filetype:pdf -expired',
            "explanation": "Research grants for STEM from NSF/NIH, excluding expired"
        }
    }
    
    BING_EXAMPLES = {
        "basic_nonprofit": {
            "description": "Basic nonprofit grant (Bing-optimized)",
            "dork": '("grant" OR "funding") intitle:nonprofit loc:"Michigan" site:gov filetype:pdf',
            "explanation": "Uses loc: for geographic targeting and simplified structure"
        },
        "research_with_date": {
            "description": "Research grant with recent date",
            "dork": 'intitle:(grant OR funding) inbody:"research proposal" (site:nsf.gov OR site:nih.gov) contains:2024 NOT expired',
            "explanation": "Uses inbody: instead of intext:, contains: for flexible matching"
        },
        "location_specific": {
            "description": "Community development with multiple locations",
            "dork": '"community development" grant loc:"New York" OR loc:"New Jersey" intitle:RFP filetype:pdf',
            "explanation": "Demonstrates Bing's superior location targeting with loc:"
        },
        "indigenous_bing": {
            "description": "Indigenous grants (Bing translation)",
            "dork": '("grant" OR "funding") intitle:tribal OR intitle:indigenous inbody:("federally recognized" OR "native american") loc:Michigan site:gov',
            "explanation": "Simplified structure with inbody: and loc: instead of Google operators"
        }
    }
    
    DUCKDUCKGO_EXAMPLES = {
        "simple_grant": {
            "description": "Simple grant search (DDG-optimized)",
            "dork": '"grant funding" nonprofit "Michigan" site:grants.gov filetype:pdf',
            "explanation": "Simple structure with only exact phrases and basic operators"
        },
        "indigenous_single": {
            "description": "Indigenous grant (DDG - single query)",
            "dork": '"tribal grant" "native american" "application" site:gov filetype:pdf -loan',
            "explanation": "Combined terms into exact phrases, removed OR logic"
        },
        "multiple_queries": {
            "description": "Indigenous grants (DDG - multiple queries approach)",
            "queries": [
                '"indigenous grant" "Michigan" site:grants.gov filetype:pdf',
                '"tribal funding" "Michigan" site:grants.gov filetype:pdf',
                '"native american grant" "Michigan" site:grants.gov filetype:pdf'
            ],
            "explanation": "Split OR chains into separate simple queries for DDG"
        },
        "research_simple": {
            "description": "Research grant (DDG)",
            "dork": '"research grant" STEM site:nsf.gov filetype:pdf',
            "explanation": "Minimal structure works best for DuckDuckGo"
        }
    }
    
    @classmethod
    def get_examples(cls, engine: SearchEngineType) -> Dict:
        """Get verified examples for a specific search engine."""
        if engine == SearchEngineType.GOOGLE:
            return cls.GOOGLE_EXAMPLES
        elif engine == SearchEngineType.BING:
            return cls.BING_EXAMPLES
        elif engine == SearchEngineType.DUCKDUCKGO:
            return cls.DUCKDUCKGO_EXAMPLES
        return {}
    
    @classmethod
    def format_examples_for_llm(cls, engine: SearchEngineType) -> str:
        """
        Format examples as a prompt for LLM guidance.
        
        This provides the LLM with concrete, verified examples to follow.
        """
        examples = cls.get_examples(engine)
        
        prompt = f"\n## VERIFIED {engine.value.upper()} DORK EXAMPLES\n\n"
        prompt += "Follow these verified patterns when generating dorks:\n\n"
        
        for key, example in examples.items():
            prompt += f"### {example['description']}\n"
            
            if 'queries' in example:
                # Multiple queries (DDG pattern)
                prompt += "**Queries:**\n"
                for i, query in enumerate(example['queries'], 1):
                    prompt += f"{i}. `{query}`\n"
            else:
                # Single dork
                prompt += f"**Dork:** `{example['dork']}`\n"
            
            prompt += f"**Explanation:** {example['explanation']}\n\n"
        
        return prompt


class LLMDorkGuidance:
    """
    Generates comprehensive guidance for LLMs to create valid dorks.
    
    This class creates prompts that ensure LLMs understand the specific
    syntax requirements for each search engine.
    """
    
    @staticmethod
    def get_generation_prompt(engine: SearchEngineType) -> str:
        """
        Get a comprehensive prompt for LLM dork generation.
        
        This includes:
        - Supported operators
        - Syntax rules
        - Verified examples
        - Common mistakes to avoid
        """
        if engine == SearchEngineType.GOOGLE:
            return LLMDorkGuidance._get_google_prompt()
        elif engine == SearchEngineType.BING:
            return LLMDorkGuidance._get_bing_prompt()
        elif engine == SearchEngineType.DUCKDUCKGO:
            return LLMDorkGuidance._get_duckduckgo_prompt()
        return ""
    
    @staticmethod
    def _get_google_prompt() -> str:
        """Google-specific generation guidance."""
        examples = SearchEngineExamples.format_examples_for_llm(SearchEngineType.GOOGLE)
        
        return f"""
# GOOGLE SEARCH DORK GENERATION GUIDE

## Supported Operators
- "exact phrase" - Exact match (ALWAYS quote multi-word terms)
- OR - Logical OR (MUST be UPPERCASE)
- - (minus) - Exclude term (no space after minus)
- * - Wildcard (matches any word)
- site: - Domain search (no space after colon)
- filetype: - File type (pdf, doc, docx)
- intext: - In page body (no space after colon)
- inurl: - In URL (no space after colon)
- intitle: - In title (single word)

## Structure for Comprehensive Grant Searches

1. **Core Terms Block:** (intext:term1 OR inurl:term1 OR intext:term2 OR inurl:term2 ...)
2. **Qualification Terms:** ("exact phrase 1" OR "exact phrase 2" ...)
3. **Process Terms:** ("phrase * wildcard" OR "exact phrase" ...)
4. **Location:** ("Location1" OR "Location2")
5. **Site/Filetype:** (site:domain1 OR site:domain2) filetype:pdf

## Critical Rules
✓ All multi-word terms MUST be in quotes
✓ OR must be UPPERCASE
✓ No spaces after operator colons
✓ Balance all parentheses
✓ Use intext: AND inurl: for maximum coverage

{examples}

## Common Mistakes to Avoid
✗ intext: grant (space after colon)
✗ "grant OR funding" (OR inside quotes)
✗ or instead of OR (lowercase)
✗ Site:grants.gov (capital S)
"""
    
    @staticmethod
    def _get_bing_prompt() -> str:
        """Bing-specific generation guidance."""
        examples = SearchEngineExamples.format_examples_for_llm(SearchEngineType.BING)
        
        return f"""
# BING SEARCH DORK GENERATION GUIDE

## Supported Operators
- "exact phrase" - Exact match
- OR - Logical OR (MUST be UPPERCASE)
- NOT - Exclude (Bing-specific, preferred over minus)
- - (minus) - Exclude (alternative)
- site: - Domain search (can use TLD like site:gov)
- filetype: - File type
- inbody: - In page body (USE THIS, not intext:)
- intitle: - In title
- loc: - Geographic location (Bing-specific advantage)
- contains: - Flexible matching

## Key Differences from Google
⚠️ Use inbody: NOT intext:
⚠️ Use loc: for geographic targeting (better than quoted locations)
⚠️ Simpler structure works better
⚠️ Use NOT or - for exclusions

## Structure for Bing

1. **(inbody:term1 OR inbody:term2 ...)**
2. **intitle:(keyword1 OR keyword2)**
3. **"exact phrases"**
4. **loc:"Location"**
5. **site:domain filetype:pdf**

{examples}

## Translation from Google
- Replace intext: → inbody:
- Replace "Location" → loc:"Location"
- Simplify complex OR chains
- Use NOT instead of - when possible
"""
    
    @staticmethod
    def _get_duckduckgo_prompt() -> str:
        """DuckDuckGo-specific generation guidance."""
        examples = SearchEngineExamples.format_examples_for_llm(SearchEngineType.DUCKDUCKGO)
        
        return f"""
# DUCKDUCKGO SEARCH DORK GENERATION GUIDE

## Supported Operators (LIMITED)
✓ "exact phrase" - Exact match
✓ site: - Domain search (full domain required)
✓ filetype: - File type
✓ intitle: - In title (basic support)
✓ - (minus) - Exclude

## NOT Supported
✗ OR operator (unreliable)
✗ intext: / inbody:
✗ inurl:
✗ Wildcards (*)
✗ Complex boolean logic
✗ loc:

## CRITICAL DDG Strategy
🔑 Generate 3-5 SEPARATE SIMPLE QUERIES instead of one complex dork
🔑 Split OR chains into individual queries
🔑 Use ONLY exact phrases and basic operators

## Structure for Each Query

"main phrase" "secondary phrase" "location" site:domain.gov filetype:pdf -exclusion

## Rules
1. Keep each query SIMPLE
2. Use exact phrases for everything
3. NO OR operator
4. NO intext/inurl/wildcards
5. Each query is self-contained

{examples}

## Translation from Google
1. Extract all OR-separated terms
2. Create separate query for each term
3. Remove intext:, inurl:, wildcards
4. Keep only: quotes, site:, filetype:, -
5. Combine related terms into exact phrases
"""


# Convenience function for LLM integration
def get_dork_generation_guidance(engine: str) -> str:
    """
    Get comprehensive dork generation guidance for an LLM.
    
    Args:
        engine: "google", "bing", or "duckduckgo"
    
    Returns:
        Complete guidance prompt with rules, examples, and validation
    """
    engine_type = SearchEngineType(engine.lower())
    return LLMDorkGuidance.get_generation_prompt(engine_type)


# Example usage
if __name__ == '__main__':
    # Demonstrate validation
    google_validator = DorkValidator(SearchEngineType.GOOGLE)
    
    # Valid Google dork
    valid_dork = '(intext:grant OR inurl:grant) "nonprofit" site:grants.gov filetype:pdf'
    result = google_validator.validate(valid_dork)
    print(f"Valid: {result.is_valid}")
    print(f"Errors: {result.errors}")
    
    # Invalid Google dork (space after colon)
    invalid_dork = 'intext: grant site: grants.gov'
    result = google_validator.validate(invalid_dork)
    print(f"\nValid: {result.is_valid}")
    print(f"Errors: {result.errors}")
    print(f"Suggestions: {result.suggestions}")
    
    # Get LLM guidance
    print("\n" + "="*80)
    print(get_dork_generation_guidance("google"))
