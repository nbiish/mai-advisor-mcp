#!/usr/bin/env python3
"""Demo script to test MAI Advisor workflow end-to-end."""
import json
import sys
sys.path.insert(0, '/Volumes/1tb-sandisk/code-external/mai-advisor-mcp/mai-advisor-mcp')

# Import directly from advisor_tools module (skip __init__.py)
from src.advisor_tools import MAIAdvisorWorkflow, AdvisorQuery


def main():
    """Run a sample workflow to verify functionality."""
    print("🚀 MAI Advisor Workflow Demo\n")
    print("=" * 60)
    
    # Create sample query
    query = AdvisorQuery(
        topic="Indigenous education technology grants",
        context="Pilot project for remote communities",
        organization_type="nonprofit",
        sector="education",
        amount_range={"min": 25000, "max": 250000},
        timeline="Need funding within 6 months",
        specific_questions=["What funders prioritize indigenous-led education?"]
    )
    
    print(f"Query Topic: {query.topic}")
    print(f"Organization: {query.organization_type}")
    print(f"Amount Range: ${query.amount_range['min']:,} - ${query.amount_range['max']:,}")
    print("=" * 60)
    print("\nExecuting workflow...\n")
    
    # Execute workflow
    wf = MAIAdvisorWorkflow()
    result = wf.execute_workflow(query, include_financial_guidance=True)
    
    # Print formatted results
    print("✅ WORKFLOW COMPLETE\n")
    print(json.dumps(result, indent=2, ensure_ascii=False, default=str))


if __name__ == '__main__':
    main()
