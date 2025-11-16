"""
Example Integration: Adding Dork Schema Validation to Grant Agent

This shows how to integrate the dork validator into grant_agent.py
to ensure the LLM generates properly formatted search queries.
"""

# Add to grant_agent.py imports
from dork_validator import (
    SearchEngineType,
    DorkValidator,
    get_dork_generation_guidance
)


# Enhanced system prompt with schema guidance
def get_enhanced_grant_assistant_prompt(search_engine: str = "google") -> str:
    """
    Get system prompt with embedded dork generation schema.
    
    Args:
        search_engine: Target search engine (google, bing, duckduckgo)
    
    Returns:
        Complete system prompt with schema guidance
    """
    
    # Get schema guidance for the target engine
    schema_guidance = get_dork_generation_guidance(search_engine)
    
    base_prompt = """You are an expert grant finder and funding advisor. Your role is to help users:

1. **Discover Grant Opportunities**: Find relevant grants, fellowships, and funding sources
2. **Generate Search Strategies**: Create advanced search queries optimized for the user's search engine
3. **Analyze Opportunities**: Evaluate grant fit and eligibility
4. **Provide Guidance**: Offer strategic advice on grant applications

## Available Tools

### `search_grants`
Search for grants using AI-powered research. Provide search criteria including:
- Keywords (required)
- Organization type (nonprofit, business, individual, etc.)
- Sector (education, healthcare, technology, etc.)
- Location
- Funding range

### `generate_search_operators`
Generate advanced search engine queries optimized for the user's preferred search engine.

### `internet_search`
Run direct web searches for grant information.

## Best Practices

- Always clarify user's organization type and sector
- Ask about funding range and location if not specified
- Generate multiple search strategies for comprehensive coverage
- Analyze results for relevance and feasibility
- Provide actionable next steps

"""
    
    # Add schema guidance
    enhanced_prompt = f"""{base_prompt}

## Search Query Generation Rules

When generating search queries (dorks), follow these CRITICAL rules:

{schema_guidance}

IMPORTANT: Always validate your generated queries against these rules before presenting them to the user.
"""
    
    return enhanced_prompt


# Example: Using validation in the grant agent
class EnhancedGrantResearchAgent:
    """
    Enhanced Grant Research Agent with dork validation.
    
    This extends the original GrantResearchAgent with validation capabilities.
    """
    
    def __init__(self, search_engine: str = "google", **kwargs):
        """
        Initialize with search engine preference.
        
        Args:
            search_engine: Target search engine (google, bing, duckduckgo)
        """
        self.search_engine = search_engine
        self.validator = DorkValidator(SearchEngineType(search_engine))
        
        # Get enhanced system prompt with schema
        self.system_prompt = get_enhanced_grant_assistant_prompt(search_engine)
    
    def validate_and_fix_dork(self, dork: str, max_retries: int = 3) -> str:
        """
        Validate a generated dork and attempt to fix if invalid.
        
        Args:
            dork: Generated dork string
            max_retries: Maximum fix attempts
        
        Returns:
            Valid dork string
        
        Raises:
            ValueError: If unable to create valid dork after max_retries
        """
        for attempt in range(max_retries):
            result = self.validator.validate(dork)
            
            if result.is_valid:
                return dork
            
            # Log validation errors
            print(f"Validation attempt {attempt + 1} failed:")
            print(f"  Errors: {result.errors}")
            print(f"  Suggestions: {result.suggestions}")
            
            # Simple fixes
            if "No space allowed after operator colon" in str(result.errors):
                # Remove spaces after colons
                dork = dork.replace(': ', ':')
                continue
            
            if "OR operator should be UPPERCASE" in str(result.warnings):
                # Fix OR case
                import re
                dork = re.sub(r'\s+or\s+', ' OR ', dork, flags=re.IGNORECASE)
                continue
            
            # If we can't auto-fix, raise error
            if attempt == max_retries - 1:
                raise ValueError(
                    f"Unable to generate valid dork after {max_retries} attempts.\n"
                    f"Errors: {result.errors}\n"
                    f"Suggestions: {result.suggestions}"
                )
        
        return dork
    
    def generate_validated_search_query(self, criteria: dict) -> dict:
        """
        Generate and validate search query.
        
        Args:
            criteria: Search criteria dict
        
        Returns:
            Dict with 'dork', 'validation', 'engine'
        """
        from dork_generator import GrantDorkGenerator, DorkInput
        
        # Create input
        input_data = DorkInput(
            topic=criteria.get('topic', ''),
            location=criteria.get('location')
        )
        
        # Generate dork based on search engine
        if self.search_engine == 'google':
            dork = GrantDorkGenerator.generate_google_dork(input_data)
        elif self.search_engine == 'bing':
            dork = GrantDorkGenerator.generate_bing_dork(input_data)
        elif self.search_engine == 'duckduckgo':
            dork = GrantDorkGenerator.generate_duckduckgo_dork(input_data)
        else:
            dork = GrantDorkGenerator.generate_google_dork(input_data)
        
        # Validate and fix if needed
        try:
            valid_dork = self.validate_and_fix_dork(dork)
            validation_result = self.validator.validate(valid_dork)
            
            return {
                'dork': valid_dork,
                'validation': validation_result,
                'engine': self.search_engine,
                'is_valid': validation_result.is_valid
            }
        except ValueError as e:
            return {
                'dork': dork,
                'validation': self.validator.validate(dork),
                'engine': self.search_engine,
                'is_valid': False,
                'error': str(e)
            }


# Example usage
if __name__ == '__main__':
    print("=" * 80)
    print("ENHANCED GRANT AGENT WITH DORK VALIDATION")
    print("=" * 80)
    
    # Create agent with Google preference
    agent = EnhancedGrantResearchAgent(search_engine='google')
    
    # Test criteria
    criteria = {
        'topic': 'indigenous tribal native american grants',
        'location': 'Michigan, Minnesota'
    }
    
    print(f"\nSearch Criteria: {criteria}\n")
    
    # Generate and validate
    result = agent.generate_validated_search_query(criteria)
    
    print(f"Engine: {result['engine']}")
    print(f"Valid: {'✓' if result['is_valid'] else '✗'}")
    print(f"\nGenerated Dork:")
    print(result['dork'][:200] + "...")
    
    if result['validation'].warnings:
        print(f"\nWarnings: {result['validation'].warnings}")
    
    if not result['is_valid']:
        print(f"\nErrors: {result['validation'].errors}")
        print(f"Suggestions: {result['validation'].suggestions}")
    
    print("\n" + "=" * 80)
    
    # Show how system prompt looks
    print("\nSYSTEM PROMPT SAMPLE (first 500 chars):")
    print("-" * 80)
    print(agent.system_prompt[:500] + "...")
