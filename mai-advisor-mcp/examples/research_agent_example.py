"""Example of using the Grant Research Agent."""
import asyncio
import os
from dotenv import load_dotenv

# Add parent directory to path
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from search_operators import GrantSearchCriteria
from grant_agent import GrantResearchAgent

load_dotenv()


async def example_basic_search():
    """Example: Basic grant search without deep analysis."""
    print("=" * 60)
    print("EXAMPLE 1: Basic Grant Search")
    print("=" * 60)
    
    agent = GrantResearchAgent()
    
    criteria = GrantSearchCriteria(
        keywords=["education", "technology", "STEM"],
        organization_type="nonprofit",
        sector="education",
        location="Massachusetts",
        funding_range_min=25000,
        funding_range_max=150000
    )
    
    print("\nSearching for grants...")
    results = await agent.research_grants(criteria, depth="basic")
    
    print(f"\nFound {results['total_results']} potential grants")
    print(f"Searched {len(results['search_results'])} different sources")


async def example_deep_research():
    """Example: Deep AI-powered grant research."""
    print("\n" + "=" * 60)
    print("EXAMPLE 2: Deep Research with AI Analysis")
    print("=" * 60)
    
    agent = GrantResearchAgent()
    
    criteria = GrantSearchCriteria(
        keywords=["climate change", "renewable energy", "sustainability"],
        organization_type="nonprofit",
        sector="environmental",
        funding_range_min=50000,
        funding_range_max=500000,
        deadline_months=6
    )
    
    print("\nConducting deep research (this may take a moment)...")
    results = await agent.research_grants(criteria, depth="deep")
    
    # Generate report
    report = agent.generate_grant_report(results, format="markdown")
    print("\n" + report)


async def example_generate_queries():
    """Example: Just generate search queries without executing."""
    print("\n" + "=" * 60)
    print("EXAMPLE 3: Generate Search Queries")
    print("=" * 60)
    
    agent = GrantResearchAgent()
    
    criteria = GrantSearchCriteria(
        keywords=["healthcare", "mental health", "wellness"],
        organization_type="nonprofit",
        sector="healthcare",
        location="California"
    )
    
    queries = agent.generate_search_strategies(criteria)
    
    from search_operators import UnifiedSearchOperatorGenerator
    output = UnifiedSearchOperatorGenerator.format_for_display(queries)
    print(output)


async def main():
    """Run all examples."""
    # Check for API keys
    if not os.getenv("TAVILY_API_KEY"):
        print("WARNING: TAVILY_API_KEY not set. Search functionality will be limited.")
        print("Set it in your .env file or environment variables.")
        print("\nRunning query generation example only...\n")
        await example_generate_queries()
        return
    
    if not os.getenv("ANTHROPIC_API_KEY"):
        print("WARNING: ANTHROPIC_API_KEY not set. Deep research will not work.")
        print("Set it in your .env file or environment variables.")
        print("\nRunning basic examples only...\n")
        await example_basic_search()
        await example_generate_queries()
        return
    
    # Run all examples
    await example_basic_search()
    await example_deep_research()
    await example_generate_queries()


if __name__ == "__main__":
    asyncio.run(main())
