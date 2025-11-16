"""Example usage of the MAI Advisor search operators."""
from search_operators import (
    GrantSearchCriteria,
    UnifiedSearchOperatorGenerator,
    SearchEngine
)


def example_nonprofit_search():
    """Example: Search for nonprofit community grants."""
    print("=" * 60)
    print("EXAMPLE 1: Nonprofit Community Development Grants")
    print("=" * 60)
    
    criteria = GrantSearchCriteria(
        keywords=["community", "development", "urban renewal"],
        organization_type="nonprofit",
        sector="community development",
        location="New York",
        funding_range_min=10000,
        funding_range_max=100000,
        deadline_months=6,
        exclude_terms=["loan", "debt", "scholarship"]
    )
    
    generator = UnifiedSearchOperatorGenerator()
    queries = generator.generate_queries(criteria)
    
    print(generator.format_for_display(queries))


def example_research_grant_search():
    """Example: Search for research grants."""
    print("\n" + "=" * 60)
    print("EXAMPLE 2: STEM Research Grants")
    print("=" * 60)
    
    criteria = GrantSearchCriteria(
        keywords=["artificial intelligence", "machine learning", "computer science"],
        organization_type="university",
        sector="research",
        funding_range_min=50000,
        funding_range_max=500000,
        deadline_months=12
    )
    
    generator = UnifiedSearchOperatorGenerator()
    queries = generator.generate_queries(
        criteria,
        engines=[SearchEngine.GOOGLE, SearchEngine.BING]
    )
    
    print(generator.format_for_display(queries))


def example_small_business_grant():
    """Example: Search for small business grants."""
    print("\n" + "=" * 60)
    print("EXAMPLE 3: Small Business Innovation Grants")
    print("=" * 60)
    
    criteria = GrantSearchCriteria(
        keywords=["small business", "innovation", "technology"],
        organization_type="business",
        sector="technology",
        location="California",
        funding_range_min=25000,
        funding_range_max=250000,
        exclude_terms=["franchise", "chain"]
    )
    
    generator = UnifiedSearchOperatorGenerator()
    queries = generator.generate_queries(
        criteria,
        engines=[SearchEngine.GOOGLE]
    )
    
    print(generator.format_for_display(queries))


def example_arts_grant():
    """Example: Search for arts and culture grants."""
    print("\n" + "=" * 60)
    print("EXAMPLE 4: Arts and Culture Grants")
    print("=" * 60)
    
    criteria = GrantSearchCriteria(
        keywords=["arts", "culture", "creative", "performing arts"],
        organization_type="nonprofit",
        sector="arts",
        funding_range_max=50000,
        deadline_months=3
    )
    
    generator = UnifiedSearchOperatorGenerator()
    queries = generator.generate_queries(criteria)
    
    print(generator.format_for_display(queries))


if __name__ == "__main__":
    # Run all examples
    example_nonprofit_search()
    example_research_grant_search()
    example_small_business_grant()
    example_arts_grant()
    
    print("\n" + "=" * 60)
    print("Copy any query above and paste into Google, Bing, or DuckDuckGo!")
    print("=" * 60)
