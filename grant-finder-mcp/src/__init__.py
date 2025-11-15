"""MAI Advisor MCP - Main package."""

__version__ = "0.1.0"
__author__ = "nbiish"
__description__ = "AI-powered grant and funding opportunity finder with advanced search capabilities"

from .search_operators import (
    GrantSearchCriteria,
    SearchEngine,
    GoogleSearchOperatorGenerator,
    BingSearchOperatorGenerator,
    DuckDuckGoOperatorGenerator,
    UnifiedSearchOperatorGenerator,
)

from .grant_agent import (
    GrantResearchAgent,
    GRANT_ASSISTANT_SYSTEM_PROMPT,
)

__all__ = [
    "GrantSearchCriteria",
    "SearchEngine",
    "GoogleSearchOperatorGenerator",
    "BingSearchOperatorGenerator",
    "DuckDuckGoOperatorGenerator",
    "UnifiedSearchOperatorGenerator",
    "GrantResearchAgent",
    "GRANT_ASSISTANT_SYSTEM_PROMPT",
]
