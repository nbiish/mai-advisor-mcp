"""Search operator generators for different search engines."""
from typing import List, Dict, Optional
from dataclasses import dataclass
from enum import Enum


class SearchEngine(Enum):
    """Supported search engines."""
    GOOGLE = "google"
    BING = "bing"
    DUCKDUCKGO = "duckduckgo"


@dataclass
class GrantSearchCriteria:
    """Criteria for grant searches."""
    keywords: List[str]
    organization_type: Optional[str] = None  # nonprofit, business, individual, etc.
    funding_range_min: Optional[int] = None
    funding_range_max: Optional[int] = None
    location: Optional[str] = None
    sector: Optional[str] = None  # education, healthcare, technology, etc.
    deadline_months: Optional[int] = None  # grants due within X months
    exclude_terms: Optional[List[str]] = None


class GoogleSearchOperatorGenerator:
    """Generate advanced Google search operators for grant finding."""
    
    @staticmethod
    def generate_query(criteria: GrantSearchCriteria) -> str:
        """
        Generate Google search query with advanced operators.
        
        Google operators:
        - "exact phrase": exact match
        - site:domain.com: search within domain
        - intitle:term: term in title
        - inurl:term: term in URL
        - filetype:pdf: specific file type
        - OR: logical OR
        - -term: exclude term
        - *: wildcard
        - AROUND(n): words within n words of each other
        """
        query_parts = []
        
        # Core grant keywords with exact phrase matching
        base_terms = [f'"{keyword}"' for keyword in criteria.keywords]
        query_parts.append(" OR ".join(base_terms))
        
        # Add grant-related terms
        grant_terms = ['grant', 'funding', 'fellowship', 'scholarship', 'award']
        query_parts.append(f"({' OR '.join(grant_terms)})")
        
        # Organization type filtering
        if criteria.organization_type:
            query_parts.append(f'"{criteria.organization_type}"')
        
        # Sector specification
        if criteria.sector:
            query_parts.append(f'"{criteria.sector}"')
        
        # Location targeting
        if criteria.location:
            query_parts.append(f'"{criteria.location}"')
        
        # Funding range (approximate with keywords)
        if criteria.funding_range_min or criteria.funding_range_max:
            funding_terms = []
            if criteria.funding_range_min and criteria.funding_range_min >= 100000:
                funding_terms.append('"six figures" OR "$100,000+"')
            if criteria.funding_range_max and criteria.funding_range_max <= 50000:
                funding_terms.append('"small grant" OR "seed funding"')
            if funding_terms:
                query_parts.append(f"({' OR '.join(funding_terms)})")
        
        # Deadline proximity
        if criteria.deadline_months:
            deadline_terms = [
                '"deadline"',
                '"apply by" OR "applications due"'
            ]
            query_parts.append(f"({' OR '.join(deadline_terms)})")
        
        # Exclude terms
        if criteria.exclude_terms:
            for term in criteria.exclude_terms:
                query_parts.append(f'-"{term}"')
        
        # Common grant announcement sites
        trusted_sites = [
            'site:grants.gov',
            'site:nsf.gov',
            'site:nih.gov',
            'site:ed.gov',
            'site:candid.org',
            'site:foundationcenter.org'
        ]
        query_parts.append(f"({' OR '.join(trusted_sites)})")
        
        # File types for grant announcements
        query_parts.append('(filetype:pdf OR filetype:doc OR filetype:docx)')
        
        return " ".join(query_parts)
    
    @staticmethod
    def generate_multiple_queries(criteria: GrantSearchCriteria) -> List[str]:
        """Generate multiple search variations for comprehensive results."""
        queries = []
        
        # Main query
        queries.append(GoogleSearchOperatorGenerator.generate_query(criteria))
        
        # Variation 1: Focus on RFPs (Request for Proposals)
        rfp_query = f"({' OR '.join(criteria.keywords)}) (RFP OR \"Request for Proposals\" OR \"Call for Applications\")"
        queries.append(rfp_query)
        
        # Variation 2: Focus on open opportunities
        open_query = f"({' OR '.join(criteria.keywords)}) (\"now accepting\" OR \"currently open\" OR \"accepting applications\")"
        queries.append(open_query)
        
        # Variation 3: Recent announcements
        recent_query = f"({' OR '.join(criteria.keywords)}) grant announcement (inurl:2024 OR inurl:2025)"
        queries.append(recent_query)
        
        return queries


class BingSearchOperatorGenerator:
    """Generate advanced Bing search operators for grant finding."""
    
    @staticmethod
    def generate_query(criteria: GrantSearchCriteria) -> str:
        """
        Generate Bing search query with advanced operators.
        
        Bing operators:
        - "exact phrase": exact match
        - site:domain.com: search within domain
        - intitle:term: term in title
        - inbody:term: term in body
        - filetype:pdf: specific file type
        - OR: logical OR
        - NOT term: exclude term
        - contains:term: page contains term
        - loc:location: geographic location
        """
        query_parts = []
        
        # Core keywords
        base_terms = [f'"{keyword}"' for keyword in criteria.keywords]
        query_parts.append(f"({' OR '.join(base_terms)})")
        
        # Grant terminology
        grant_terms = 'intitle:(grant OR funding OR fellowship OR scholarship)'
        query_parts.append(grant_terms)
        
        # Organization type
        if criteria.organization_type:
            query_parts.append(f'"{criteria.organization_type}"')
        
        # Sector
        if criteria.sector:
            query_parts.append(f'inbody:"{criteria.sector}"')
        
        # Location with Bing's location operator
        if criteria.location:
            query_parts.append(f'loc:"{criteria.location}"')
        
        # Funding information
        if criteria.funding_range_min or criteria.funding_range_max:
            query_parts.append('contains:("funding amount" OR "award amount" OR "grant size")')
        
        # Deadline information
        if criteria.deadline_months:
            query_parts.append('contains:("deadline" OR "apply by")')
        
        # Exclude terms
        if criteria.exclude_terms:
            for term in criteria.exclude_terms:
                query_parts.append(f'NOT "{term}"')
        
        # Trusted grant sources
        trusted_domains = ' OR '.join([
            'site:grants.gov',
            'site:nsf.gov',
            'site:nih.gov',
            'site:ed.gov'
        ])
        query_parts.append(f"({trusted_domains})")
        
        # File types
        query_parts.append('(filetype:pdf OR filetype:doc)')
        
        return " ".join(query_parts)
    
    @staticmethod
    def generate_date_restricted_query(criteria: GrantSearchCriteria, months: int = 6) -> str:
        """Generate Bing query restricted to recent publications."""
        base_query = BingSearchOperatorGenerator.generate_query(criteria)
        # Bing doesn't have a built-in date operator like Google, so we add date keywords
        return f'{base_query} ("2024" OR "2025") inurl:(2024 OR 2025)'


class DuckDuckGoOperatorGenerator:
    """Generate DuckDuckGo search operators for grant finding."""
    
    @staticmethod
    def generate_query(criteria: GrantSearchCriteria) -> str:
        """
        Generate DuckDuckGo search query with advanced operators.
        
        DuckDuckGo operators (more limited than Google/Bing):
        - "exact phrase": exact match
        - site:domain.com: search within domain
        - intitle:term: term in title
        - -term: exclude term
        - filetype:pdf: specific file type
        """
        query_parts = []
        
        # Core keywords with exact matching
        base_terms = [f'"{keyword}"' for keyword in criteria.keywords]
        query_parts.append(" ".join(base_terms))
        
        # Grant-related terms in title
        query_parts.append('intitle:grant OR intitle:funding OR intitle:fellowship')
        
        # Organization type
        if criteria.organization_type:
            query_parts.append(f'"{criteria.organization_type}"')
        
        # Sector
        if criteria.sector:
            query_parts.append(f'"{criteria.sector}"')
        
        # Location
        if criteria.location:
            query_parts.append(f'"{criteria.location}"')
        
        # Funding range indicators
        if criteria.funding_range_min and criteria.funding_range_min >= 100000:
            query_parts.append('"large grant" OR "$100,000"')
        elif criteria.funding_range_max and criteria.funding_range_max <= 25000:
            query_parts.append('"small grant" OR "micro grant"')
        
        # Deadline
        if criteria.deadline_months:
            query_parts.append('"deadline" "applications"')
        
        # Exclude terms
        if criteria.exclude_terms:
            for term in criteria.exclude_terms:
                query_parts.append(f'-"{term}"')
        
        # Trusted sites (DDG has good site: support)
        query_parts.append('(site:grants.gov OR site:nsf.gov OR site:nih.gov)')
        
        # File type
        query_parts.append('filetype:pdf')
        
        return " ".join(query_parts)
    
    @staticmethod
    def generate_privacy_focused_query(criteria: GrantSearchCriteria) -> str:
        """Generate a simpler query optimized for DuckDuckGo's privacy-focused approach."""
        # DuckDuckGo works better with simpler queries
        keywords = " ".join(criteria.keywords)
        grant_type = criteria.sector if criteria.sector else "general"
        location = criteria.location if criteria.location else ""
        
        query = f'"{keywords}" grant funding {grant_type} {location} site:grants.gov OR site:nsf.gov'
        return query.strip()


class UnifiedSearchOperatorGenerator:
    """Unified interface for generating search operators across all engines."""
    
    @staticmethod
    def generate_queries(
        criteria: GrantSearchCriteria,
        engines: Optional[List[SearchEngine]] = None
    ) -> Dict[SearchEngine, List[str]]:
        """
        Generate search queries for specified engines.
        
        Args:
            criteria: Grant search criteria
            engines: List of search engines (defaults to all)
        
        Returns:
            Dictionary mapping engine to list of query variations
        """
        if engines is None:
            engines = list(SearchEngine)
        
        results = {}
        
        for engine in engines:
            if engine == SearchEngine.GOOGLE:
                results[engine] = GoogleSearchOperatorGenerator.generate_multiple_queries(criteria)
            elif engine == SearchEngine.BING:
                results[engine] = [
                    BingSearchOperatorGenerator.generate_query(criteria),
                    BingSearchOperatorGenerator.generate_date_restricted_query(criteria)
                ]
            elif engine == SearchEngine.DUCKDUCKGO:
                results[engine] = [
                    DuckDuckGoOperatorGenerator.generate_query(criteria),
                    DuckDuckGoOperatorGenerator.generate_privacy_focused_query(criteria)
                ]
        
        return results
    
    @staticmethod
    def format_for_display(queries: Dict[SearchEngine, List[str]]) -> str:
        """Format generated queries for human-readable display."""
        output = []
        output.append("=== GENERATED GRANT SEARCH QUERIES ===\n")
        
        for engine, query_list in queries.items():
            output.append(f"\n## {engine.value.upper()} Search Queries")
            output.append("-" * 50)
            for i, query in enumerate(query_list, 1):
                output.append(f"\nQuery {i}:")
                output.append(f"  {query}\n")
        
        return "\n".join(output)
