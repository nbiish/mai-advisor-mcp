"""Grant research agent using deep agent architecture."""
import os
from typing import Literal, List, Dict, Any, Optional
from tavily import TavilyClient
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

from search_operators import (
    GrantSearchCriteria,
    UnifiedSearchOperatorGenerator,
    SearchEngine
)


class GrantResearchAgent:
    """
    AI-powered grant research agent that uses deep research techniques
    to find and analyze grant opportunities.
    
    Uses OpenRouter for LLM access (Google Gemini 2.5 Flash via OpenRouter).
    """
    
    def __init__(
        self,
        tavily_api_key: Optional[str] = None,
        openrouter_api_key: Optional[str] = None,
        model_name: str = "google/gemini-2.0-flash-thinking-exp:free"
    ):
        """Initialize the grant research agent."""
        self.tavily_client = TavilyClient(
            api_key=tavily_api_key or os.environ.get("TAVILY_API_KEY")
        )
        self.model = ChatOpenAI(
            model=model_name,
            api_key=openrouter_api_key or os.environ.get("OPENROUTER_API_KEY"),
            base_url="https://openrouter.ai/api/v1",
            temperature=0.3
        )
        self.search_generator = UnifiedSearchOperatorGenerator()
    
    def internet_search(
        self,
        query: str,
        max_results: int = 10,
        topic: Literal["general", "news", "finance"] = "general",
        include_raw_content: bool = True,
    ) -> Dict[str, Any]:
        """
        Run a web search using Tavily.
        
        Args:
            query: Search query string
            max_results: Maximum number of results to return
            topic: Search topic category
            include_raw_content: Whether to include full page content
        
        Returns:
            Search results from Tavily
        """
        return self.tavily_client.search(
            query,
            max_results=max_results,
            include_raw_content=include_raw_content,
            topic=topic,
        )
    
    def generate_search_strategies(
        self,
        criteria: GrantSearchCriteria
    ) -> Dict[SearchEngine, List[str]]:
        """
        Generate advanced search queries for multiple search engines.
        
        Args:
            criteria: Grant search criteria
        
        Returns:
            Dictionary mapping search engines to query lists
        """
        return self.search_generator.generate_queries(criteria)
    
    async def research_grants(
        self,
        criteria: GrantSearchCriteria,
        depth: Literal["basic", "deep"] = "deep"
    ) -> Dict[str, Any]:
        """
        Conduct comprehensive grant research using AI-guided search.
        
        Args:
            criteria: Grant search criteria
            depth: Research depth (basic or deep)
        
        Returns:
            Research results with grant opportunities and analysis
        """
        # Generate search strategies
        search_queries = self.generate_search_strategies(criteria)
        
        # Execute searches
        all_results = []
        for engine, queries in search_queries.items():
            for query in queries[:2]:  # Limit to 2 queries per engine for efficiency
                try:
                    results = self.internet_search(
                        query,
                        max_results=5,
                        include_raw_content=True
                    )
                    all_results.append({
                        "engine": engine.value,
                        "query": query,
                        "results": results
                    })
                except Exception as e:
                    print(f"Search failed for {engine.value}: {e}")
        
        if depth == "basic":
            return {
                "criteria": criteria,
                "search_results": all_results,
                "total_results": sum(len(r.get("results", {}).get("results", [])) for r in all_results)
            }
        
        # Deep research: Use AI to analyze and synthesize results
        return await self._deep_analysis(criteria, all_results)
    
    async def _deep_analysis(
        self,
        criteria: GrantSearchCriteria,
        search_results: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        Perform deep analysis of search results using AI.
        
        Args:
            criteria: Original search criteria
            search_results: Raw search results from multiple engines
        
        Returns:
            Analyzed and synthesized grant opportunities
        """
        # Prepare context for AI analysis
        context = self._prepare_analysis_context(criteria, search_results)
        
        system_prompt = """You are an expert grant research analyst. Your job is to:

1. Analyze grant opportunities from search results
2. Identify the most relevant and promising grants
3. Extract key information: deadline, amount, eligibility, requirements
4. Assess fit with the user's criteria
5. Provide strategic recommendations

Be thorough, accurate, and prioritize actionable information."""

        user_prompt = f"""Analyze these grant search results based on the following criteria:

SEARCH CRITERIA:
- Keywords: {', '.join(criteria.keywords)}
- Organization Type: {criteria.organization_type or 'Any'}
- Sector: {criteria.sector or 'Any'}
- Location: {criteria.location or 'Any'}
- Funding Range: ${criteria.funding_range_min or 0:,} - ${criteria.funding_range_max or 'unlimited':,}

SEARCH RESULTS:
{context}

Please provide:
1. Top 5-10 most relevant grant opportunities
2. For each grant:
   - Grant name and funder
   - Funding amount
   - Deadline
   - Eligibility requirements
   - Application requirements
   - Why it's a good fit
3. Overall recommendations and next steps
4. Any red flags or concerns

Format as a structured report."""

        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=user_prompt)
        ]
        
        response = self.model.invoke(messages)
        
        return {
            "criteria": criteria,
            "analysis": response.content,
            "total_sources_searched": len(search_results),
            "raw_results": search_results
        }
    
    def _prepare_analysis_context(
        self,
        criteria: GrantSearchCriteria,
        search_results: List[Dict[str, Any]]
    ) -> str:
        """Prepare search results context for AI analysis."""
        context_parts = []
        
        for i, result_set in enumerate(search_results[:10], 1):  # Limit to 10 result sets
            engine = result_set.get("engine", "unknown")
            query = result_set.get("query", "")
            results = result_set.get("results", {}).get("results", [])
            
            context_parts.append(f"\n--- Search {i} ({engine}) ---")
            context_parts.append(f"Query: {query}\n")
            
            for j, result in enumerate(results[:3], 1):  # Top 3 results per search
                title = result.get("title", "No title")
                url = result.get("url", "")
                content = result.get("content", "")[:500]  # First 500 chars
                
                context_parts.append(f"\nResult {i}.{j}: {title}")
                context_parts.append(f"URL: {url}")
                context_parts.append(f"Content: {content}...")
        
        return "\n".join(context_parts)
    
    def generate_grant_report(
        self,
        research_results: Dict[str, Any],
        format: Literal["markdown", "json", "text"] = "markdown"
    ) -> str:
        """
        Generate a formatted report from research results.
        
        Args:
            research_results: Results from research_grants()
            format: Output format
        
        Returns:
            Formatted report string
        """
        if format == "json":
            import json
            return json.dumps(research_results, indent=2, default=str)
        
        elif format == "markdown":
            criteria = research_results.get("criteria")
            analysis = research_results.get("analysis", "")
            
            report = f"""# Grant Research Report

## Search Criteria
- **Keywords**: {', '.join(criteria.keywords) if criteria else 'N/A'}
- **Organization Type**: {criteria.organization_type if criteria else 'N/A'}
- **Sector**: {criteria.sector if criteria else 'N/A'}
- **Location**: {criteria.location if criteria else 'N/A'}
- **Funding Range**: ${criteria.funding_range_min or 0:,} - ${criteria.funding_range_max or 'unlimited':,}

## Analysis

{analysis}

---
*Generated by MAI Advisor MCP - AI-Powered Grant Research*
"""
            return report
        
        else:  # text format
            return str(research_results.get("analysis", "No analysis available"))


# System prompt for the grant assistant agent
GRANT_ASSISTANT_SYSTEM_PROMPT = """You are an expert grant finder and funding advisor. Your role is to help users:

1. **Discover Grant Opportunities**: Find relevant grants, fellowships, and funding sources
2. **Generate Search Strategies**: Create advanced search queries for Google, Bing, and DuckDuckGo
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
Generate advanced search engine queries optimized for:
- Google (with advanced operators)
- Bing (with Bing-specific syntax)
- DuckDuckGo (privacy-focused queries)

### `internet_search`
Run direct web searches for grant information.

## Best Practices

- Always clarify user's organization type and sector
- Ask about funding range and location if not specified
- Generate multiple search strategies for comprehensive coverage
- Analyze results for relevance and feasibility
- Provide actionable next steps

Be thorough, accurate, and user-focused in your recommendations."""
