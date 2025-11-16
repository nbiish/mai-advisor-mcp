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

from .advisor_tools import (
    MAIAdvisorWorkflow,
    AdvisorQuery,
    ResearchTask,
    FinancialGuidance,
    ExpertAdvisor,
    FinancialAdvisor,
    ResearchCrewCoordinator,
)

# Optional import - only load if dependencies are available
try:
    from .grant_agent import (
        GrantResearchAgent,
        GRANT_ASSISTANT_SYSTEM_PROMPT,
    )
    _GRANT_AGENT_AVAILABLE = True
except ImportError:
    _GRANT_AGENT_AVAILABLE = False
    GrantResearchAgent = None
    GRANT_ASSISTANT_SYSTEM_PROMPT = None

__all__ = [
    "GrantSearchCriteria",
    "SearchEngine",
    "GoogleSearchOperatorGenerator",
    "BingSearchOperatorGenerator",
    "DuckDuckGoOperatorGenerator",
    "UnifiedSearchOperatorGenerator",
    "MAIAdvisorWorkflow",
    "AdvisorQuery",
    "ResearchTask",
    "FinancialGuidance",
    "ExpertAdvisor",
    "FinancialAdvisor",
    "ResearchCrewCoordinator",
]

if _GRANT_AGENT_AVAILABLE:
    __all__.extend([
        "GrantResearchAgent",
        "GRANT_ASSISTANT_SYSTEM_PROMPT",
    ])
