"""Expert Advisor and Financial Guidance Tools for MCP."""
from typing import Dict, List, Optional, Any
from dataclasses import dataclass
from enum import Enum


class AdvisorRole(Enum):
    """Types of expert advisors."""
    GRANT_EXPERT = "grant_expert"
    FINANCIAL_ADVISOR = "financial_advisor"
    RESEARCH_COORDINATOR = "research_coordinator"


@dataclass
class AdvisorQuery:
    """Query structure for expert advisor."""
    topic: str
    context: Optional[str] = None
    organization_type: Optional[str] = None
    sector: Optional[str] = None
    amount_range: Optional[Dict[str, int]] = None
    timeline: Optional[str] = None
    specific_questions: Optional[List[str]] = None


@dataclass
class ResearchTask:
    """Task structure for research crew."""
    task_id: str
    query: str
    search_engines: List[str]
    criteria: Dict[str, Any]
    priority: str = "normal"  # normal, high, urgent
    depth: str = "deep"  # basic, deep


@dataclass
class FinancialGuidance:
    """Financial guidance structure."""
    process_stage: str
    recommendations: List[str]
    budget_considerations: List[str]
    timeline_guidance: str
    next_steps: List[str]
    risk_assessment: Optional[str] = None


class ExpertAdvisor:
    """Expert advisor that formulates strategic queries and coordinates research."""
    
    def __init__(self):
        self.role = AdvisorRole.GRANT_EXPERT
        self.knowledge_base = self._load_knowledge_base()
    
    def _load_knowledge_base(self) -> Dict[str, Any]:
        """Load advisor knowledge base."""
        return {
            "grant_types": [
                "federal_grants",
                "state_grants",
                "foundation_grants",
                "corporate_grants",
                "research_grants",
                "capacity_building",
                "project_grants",
                "operating_grants"
            ],
            "common_requirements": [
                "501(c)(3) status",
                "DUNS number",
                "SAM registration",
                "organizational budget",
                "board composition",
                "financial statements",
                "audit requirements",
                "matching funds"
            ],
            "strategic_considerations": [
                "funding alignment",
                "capacity assessment",
                "sustainability planning",
                "impact measurement",
                "stakeholder engagement"
            ]
        }
    
    def analyze_request(self, query: AdvisorQuery) -> Dict[str, Any]:
        """
        Analyze user request and formulate strategic approach.
        
        Returns comprehensive analysis with:
        - Interpreted needs
        - Strategic recommendations
        - Research tasks to assign to crew
        - Financial considerations
        """
        analysis = {
            "request_summary": self._summarize_request(query),
            "strategic_approach": self._formulate_strategy(query),
            "research_tasks": self._generate_research_tasks(query),
            "financial_scope": self._assess_financial_scope(query),
            "success_criteria": self._define_success_criteria(query),
            "timeline_estimate": self._estimate_timeline(query)
        }
        
        return analysis
    
    def _summarize_request(self, query: AdvisorQuery) -> str:
        """Generate clear summary of user's request."""
        summary_parts = [f"Topic: {query.topic}"]
        
        if query.organization_type:
            summary_parts.append(f"Organization Type: {query.organization_type}")
        if query.sector:
            summary_parts.append(f"Sector: {query.sector}")
        if query.amount_range:
            min_amt = query.amount_range.get("min", "N/A")
            max_amt = query.amount_range.get("max", "N/A")
            summary_parts.append(f"Amount Range: ${min_amt:,} - ${max_amt:,}")
        if query.timeline:
            summary_parts.append(f"Timeline: {query.timeline}")
        
        return " | ".join(summary_parts)
    
    def _formulate_strategy(self, query: AdvisorQuery) -> Dict[str, Any]:
        """Formulate strategic search and research approach."""
        strategy = {
            "primary_focus": [],
            "secondary_focus": [],
            "search_priorities": [],
            "recommended_sources": []
        }
        
        # Determine primary focus based on organization type
        if query.organization_type == "nonprofit":
            strategy["primary_focus"].extend([
                "Foundation grants",
                "Federal/state grants",
                "Corporate giving programs"
            ])
            strategy["recommended_sources"].extend([
                "grants.gov",
                "foundationcenter.org",
                "candid.org"
            ])
        elif query.organization_type == "business":
            strategy["primary_focus"].extend([
                "SBIR/STTR grants",
                "Innovation grants",
                "Economic development grants"
            ])
            strategy["recommended_sources"].extend([
                "sbir.gov",
                "eda.gov",
                "sba.gov"
            ])
        elif query.organization_type == "university":
            strategy["primary_focus"].extend([
                "Research grants",
                "Training grants",
                "Equipment grants"
            ])
            strategy["recommended_sources"].extend([
                "nsf.gov",
                "nih.gov",
                "ed.gov"
            ])
        
        # Add sector-specific priorities
        if query.sector:
            strategy["search_priorities"].append(f"Sector-specific: {query.sector}")
        
        return strategy
    
    def _generate_research_tasks(self, query: AdvisorQuery) -> List[ResearchTask]:
        """Generate specific research tasks for the crew."""
        tasks = []
        
        # Task 1: Broad landscape scan
        tasks.append(ResearchTask(
            task_id="task_001_landscape",
            query=f"Current grant opportunities in {query.topic}",
            search_engines=["google", "bing", "duckduckgo"],
            criteria={
                "keywords": [query.topic],
                "organization_type": query.organization_type,
                "sector": query.sector,
                "deadline_months": 6
            },
            priority="high",
            depth="deep"
        ))
        
        # Task 2: Targeted federal/state search
        tasks.append(ResearchTask(
            task_id="task_002_government",
            query=f"Federal and state grants for {query.topic}",
            search_engines=["google"],
            criteria={
                "keywords": [query.topic, "federal", "state"],
                "organization_type": query.organization_type,
                "deadline_months": 12
            },
            priority="high",
            depth="deep"
        ))
        
        # Task 3: Foundation and private sector
        tasks.append(ResearchTask(
            task_id="task_003_foundations",
            query=f"Foundation and corporate grants for {query.topic}",
            search_engines=["google", "duckduckgo"],
            criteria={
                "keywords": [query.topic, "foundation", "corporate giving"],
                "organization_type": query.organization_type,
                "deadline_months": 12
            },
            priority="normal",
            depth="deep"
        ))
        
        return tasks
    
    def _assess_financial_scope(self, query: AdvisorQuery) -> Dict[str, Any]:
        """Assess financial aspects of the request."""
        scope = {
            "amount_range": query.amount_range or {"min": 0, "max": "unlimited"},
            "typical_grant_sizes": self._get_typical_sizes(query),
            "cost_considerations": [],
            "matching_requirements": []
        }
        
        # Add cost considerations
        if query.organization_type == "nonprofit":
            scope["cost_considerations"].extend([
                "Indirect cost rates (typically 10-25%)",
                "Matching funds requirements",
                "Audit requirements for grants >$750,000"
            ])
        
        return scope
    
    def _get_typical_sizes(self, query: AdvisorQuery) -> List[str]:
        """Get typical grant sizes for the context."""
        sizes = []
        
        if query.organization_type == "nonprofit":
            sizes.extend([
                "Small grants: $5,000 - $25,000",
                "Medium grants: $25,000 - $100,000",
                "Large grants: $100,000 - $500,000",
                "Major grants: $500,000+"
            ])
        elif query.organization_type == "business":
            sizes.extend([
                "Seed grants: $10,000 - $50,000",
                "SBIR Phase I: ~$250,000",
                "SBIR Phase II: $1,000,000+",
                "Innovation grants: $50,000 - $500,000"
            ])
        
        return sizes
    
    def _define_success_criteria(self, query: AdvisorQuery) -> List[str]:
        """Define what success looks like for this search."""
        return [
            "Identify 10-15 relevant grant opportunities",
            "Match 70%+ alignment with organizational mission",
            "Balance of short-term (3-6 mo) and long-term (12+ mo) deadlines",
            "Mix of funding sizes to diversify portfolio",
            "Clear eligibility criteria match"
        ]
    
    def _estimate_timeline(self, query: AdvisorQuery) -> str:
        """Estimate timeline for grant search and application process."""
        return """
        Phase 1: Research & Identification (1-2 weeks)
        Phase 2: Detailed Analysis & Selection (1 week)
        Phase 3: Application Preparation (4-8 weeks per grant)
        Phase 4: Submission & Follow-up (ongoing)
        
        Total estimated time: 8-12 weeks for full cycle
        """


class FinancialAdvisor:
    """Financial advisor providing budget and process guidance."""
    
    def __init__(self):
        self.role = AdvisorRole.FINANCIAL_ADVISOR
    
    def provide_guidance(
        self,
        stage: str,
        amount_range: Optional[Dict[str, int]] = None,
        organization_type: Optional[str] = None
    ) -> FinancialGuidance:
        """
        Provide financial guidance for grant seeking process.
        
        Args:
            stage: Current process stage (research, planning, application, management)
            amount_range: Target funding range
            organization_type: Type of organization
        """
        if stage == "research":
            return self._research_stage_guidance(amount_range, organization_type)
        elif stage == "planning":
            return self._planning_stage_guidance(amount_range, organization_type)
        elif stage == "application":
            return self._application_stage_guidance(amount_range, organization_type)
        elif stage == "management":
            return self._management_stage_guidance(amount_range, organization_type)
        else:
            return self._general_guidance(amount_range, organization_type)
    
    def _research_stage_guidance(
        self,
        amount_range: Optional[Dict[str, int]],
        organization_type: Optional[str]
    ) -> FinancialGuidance:
        """Guidance for research stage."""
        return FinancialGuidance(
            process_stage="Research & Discovery",
            recommendations=[
                "Cast a wide net initially - consider all funding sizes",
                "Track application deadlines and requirements",
                "Document eligibility criteria for each opportunity",
                "Note matching fund requirements early",
                "Assess organizational capacity for each grant size"
            ],
            budget_considerations=[
                "Factor in application preparation costs",
                "Consider consultant/grant writer fees if needed",
                "Account for matching fund availability",
                "Budget for required organizational documents (audits, etc.)"
            ],
            timeline_guidance="Allow 2-3 weeks for thorough research phase",
            next_steps=[
                "Create tracking spreadsheet for opportunities",
                "Prioritize based on alignment and feasibility",
                "Assess capacity for multiple simultaneous applications"
            ]
        )
    
    def _planning_stage_guidance(
        self,
        amount_range: Optional[Dict[str, int]],
        organization_type: Optional[str]
    ) -> FinancialGuidance:
        """Guidance for planning stage."""
        recommendations = [
            "Develop detailed project budget with justifications",
            "Identify all cost categories (personnel, equipment, indirect)",
            "Calculate indirect cost rate if applicable",
            "Plan for sustainability beyond grant period"
        ]
        
        budget_considerations = [
            "Direct costs: Personnel, supplies, equipment, travel",
            "Indirect costs: Typically 10-25% of direct costs",
            "Cost sharing: Many grants require 10-25% match",
            "Unallowable costs: Entertainment, lobbying, certain overhead"
        ]
        
        # Add amount-specific guidance
        if amount_range and amount_range.get("max"):
            max_amt = amount_range["max"]
            if max_amt >= 750000:
                budget_considerations.append(
                    "Single Audit required for federal awards >$750,000"
                )
                recommendations.append(
                    "Ensure audit capacity or budget for external auditor"
                )
        
        return FinancialGuidance(
            process_stage="Budget Planning",
            recommendations=recommendations,
            budget_considerations=budget_considerations,
            timeline_guidance="Allow 1-2 weeks for budget development and review",
            risk_assessment="Budget errors are a common reason for rejection - allow time for review",
            next_steps=[
                "Have budget reviewed by finance staff",
                "Get quotes for major equipment/services",
                "Confirm matching fund commitments in writing",
                "Prepare budget narrative explaining all costs"
            ]
        )
    
    def _application_stage_guidance(
        self,
        amount_range: Optional[Dict[str, int]],
        organization_type: Optional[str]
    ) -> FinancialGuidance:
        """Guidance for application stage."""
        return FinancialGuidance(
            process_stage="Application Preparation",
            recommendations=[
                "Double-check all financial calculations",
                "Ensure budget aligns with narrative activities",
                "Include required financial documentation",
                "Have multiple reviewers check budget accuracy",
                "Prepare for questions about budget items"
            ],
            budget_considerations=[
                "Budget must match project narrative exactly",
                "All costs must be reasonable and allocable",
                "Provide clear justification for each line item",
                "Ensure compliance with funder's budget format"
            ],
            timeline_guidance="Allow 1-2 days for final budget review before submission",
            next_steps=[
                "Get CFO/Finance Director sign-off",
                "Prepare supporting budget documentation",
                "Confirm all required financial attachments",
                "Test submission system well before deadline"
            ]
        )
    
    def _management_stage_guidance(
        self,
        amount_range: Optional[Dict[str, int]],
        organization_type: Optional[str]
    ) -> FinancialGuidance:
        """Guidance for grant management stage."""
        return FinancialGuidance(
            process_stage="Grant Management & Compliance",
            recommendations=[
                "Set up separate accounting code for grant funds",
                "Implement expense tracking from day one",
                "Schedule regular budget reviews (monthly minimum)",
                "Monitor spending rate and adjust as needed",
                "Maintain detailed documentation of all expenses"
            ],
            budget_considerations=[
                "Track actual vs. budgeted spending",
                "Get approval before moving funds between categories",
                "Save receipts and documentation for all purchases",
                "Monitor indirect cost calculations",
                "Plan for final financial report requirements"
            ],
            timeline_guidance="Establish monthly review cycle throughout grant period",
            risk_assessment="Non-compliance can result in fund recapture and future ineligibility",
            next_steps=[
                "Create grant management calendar with deadlines",
                "Assign clear financial oversight responsibilities",
                "Set up systems for progress and financial reporting",
                "Schedule regular team check-ins on grant progress"
            ]
        )
    
    def _general_guidance(
        self,
        amount_range: Optional[Dict[str, int]],
        organization_type: Optional[str]
    ) -> FinancialGuidance:
        """General financial guidance."""
        return FinancialGuidance(
            process_stage="General Financial Planning",
            recommendations=[
                "Build organizational capacity for grants management",
                "Develop clear financial policies and procedures",
                "Maintain strong financial records and systems",
                "Consider hiring grant professional for major opportunities",
                "Diversify funding sources - don't rely on single grant"
            ],
            budget_considerations=[
                "Assess true cost of grant seeking (staff time, systems)",
                "Factor in long-term sustainability needs",
                "Consider organizational financial health",
                "Evaluate capacity for financial compliance"
            ],
            timeline_guidance="Ongoing financial planning is critical for success",
            next_steps=[
                "Conduct organizational financial assessment",
                "Develop grant seeking and management policies",
                "Invest in financial management systems/training",
                "Build relationships with finance professionals"
            ]
        )


class ResearchCrewCoordinator:
    """Coordinates research tasks and compiles dorks (search queries)."""
    
    def __init__(self):
        self.role = AdvisorRole.RESEARCH_COORDINATOR
        self.pending_tasks: List[ResearchTask] = []
        self.completed_tasks: List[ResearchTask] = []
    
    def assign_tasks(self, tasks: List[ResearchTask]) -> Dict[str, Any]:
        """Assign research tasks to crew."""
        self.pending_tasks.extend(tasks)
        
        return {
            "status": "tasks_assigned",
            "total_tasks": len(tasks),
            "high_priority": len([t for t in tasks if t.priority == "high"]),
            "task_summary": [
                {
                    "id": task.task_id,
                    "query": task.query,
                    "engines": task.search_engines,
                    "priority": task.priority
                }
                for task in tasks
            ]
        }
    
    def generate_dorks(self, task: ResearchTask) -> Dict[str, List[str]]:
        """
        Generate search engine dorks (advanced queries) for a research task.
        
        Returns dict with engine names as keys and lists of dork strings.
        """
        from .search_operators import (
            GrantSearchCriteria,
            GoogleSearchOperatorGenerator,
            BingSearchOperatorGenerator,
            DuckDuckGoOperatorGenerator
        )
        
        # Convert task criteria to GrantSearchCriteria
        criteria = GrantSearchCriteria(
            keywords=task.criteria.get("keywords", []),
            organization_type=task.criteria.get("organization_type"),
            sector=task.criteria.get("sector"),
            location=task.criteria.get("location"),
            amount_min=task.criteria.get("amount_min"),
            amount_max=task.criteria.get("amount_max"),
            deadline_months=task.criteria.get("deadline_months"),
            exclude_terms=task.criteria.get("exclude_terms")
        )
        
        dorks = {}
        
        # Generate dorks for each requested search engine
        if "google" in [e.lower() for e in task.search_engines]:
            dorks["google"] = [
                GoogleSearchOperatorGenerator.generate_query(criteria)
            ]
        
        if "bing" in [e.lower() for e in task.search_engines]:
            dorks["bing"] = [
                BingSearchOperatorGenerator.generate_query(criteria)
            ]
        
        if "duckduckgo" in [e.lower() for e in task.search_engines]:
            dorks["duckduckgo"] = [
                DuckDuckGoOperatorGenerator.generate_query(criteria)
            ]
        
        return dorks
    
    def compile_all_dorks(self) -> Dict[str, Any]:
        """Compile all dorks from all pending tasks."""
        all_dorks = {
            "google": [],
            "bing": [],
            "duckduckgo": []
        }
        
        task_results = []
        
        for task in self.pending_tasks:
            dorks = self.generate_dorks(task)
            
            # Aggregate dorks
            for engine, queries in dorks.items():
                all_dorks[engine].extend(queries)
            
            task_results.append({
                "task_id": task.task_id,
                "query": task.query,
                "dorks_generated": sum(len(v) for v in dorks.values()),
                "engines": list(dorks.keys())
            })
        
        return {
            "summary": {
                "total_tasks": len(self.pending_tasks),
                "total_dorks": sum(len(v) for v in all_dorks.values()),
                "google_queries": len(all_dorks["google"]),
                "bing_queries": len(all_dorks["bing"]),
                "duckduckgo_queries": len(all_dorks["duckduckgo"])
            },
            "dorks": all_dorks,
            "task_breakdown": task_results
        }


# Main workflow coordinator
class MAIAdvisorWorkflow:
    """Coordinates the complete MAI Advisor workflow."""
    
    def __init__(self):
        self.expert_advisor = ExpertAdvisor()
        self.financial_advisor = FinancialAdvisor()
        self.research_coordinator = ResearchCrewCoordinator()
    
    def execute_workflow(
        self,
        query: AdvisorQuery,
        include_financial_guidance: bool = True
    ) -> Dict[str, Any]:
        """
        Execute complete workflow:
        1. Expert advisor analyzes request
        2. Generate research tasks
        3. Financial advisor provides guidance
        4. Research coordinator generates dorks
        """
        # Step 1: Expert analysis
        analysis = self.expert_advisor.analyze_request(query)
        
        # Step 2: Assign tasks to research crew
        task_assignment = self.research_coordinator.assign_tasks(
            analysis["research_tasks"]
        )
        
        # Step 3: Generate all dorks
        dorks_compilation = self.research_coordinator.compile_all_dorks()
        
        # Step 4: Financial guidance
        financial_guidance = None
        if include_financial_guidance:
            financial_guidance = self.financial_advisor.provide_guidance(
                stage="research",
                amount_range=query.amount_range,
                organization_type=query.organization_type
            )
        
        return {
            "workflow_status": "complete",
            "expert_analysis": analysis,
            "research_tasks": task_assignment,
            "search_dorks": dorks_compilation,
            "financial_guidance": financial_guidance.__dict__ if financial_guidance else None
        }
