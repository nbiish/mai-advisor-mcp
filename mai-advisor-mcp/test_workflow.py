#!/usr/bin/env python3
"""
Test file-based workflow system.
Verifies OutputManager, file structure, and workflow integration.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from output_manager import output_manager, AdvisorOutput, OrchestratorOutput
from datetime import datetime
from pathlib import Path


def test_output_manager():
    """Test OutputManager functionality."""
    
    print("=" * 80)
    print("TESTING OUTPUT MANAGER")
    print("=" * 80)
    
    # Test 1: Directory creation
    print("\n1. Testing directory structure...")
    assert output_manager.advisors_dir.exists(), "advisors_output/ not created"
    assert output_manager.orchestrator_dir.exists(), "orchestrator_output/ not created"
    assert output_manager.dorks_dir.exists(), "grant_dorks/ not created"
    print("✓ All directories exist")
    
    # Test 2: Save advisor output
    print("\n2. Testing advisor output save...")
    advisor_output = AdvisorOutput(
        advisor_type="financial",
        timestamp=datetime.now().isoformat(),
        topic="test project",
        analysis={"test": "data"},
        recommendations=["rec 1", "rec 2"],
        metadata={"version": "test"}
    )
    
    filepath = output_manager.save_advisor_output(advisor_output)
    assert Path(filepath).exists(), f"File not created: {filepath}"
    print(f"✓ Advisor output saved: {Path(filepath).name}")
    
    # Test 3: Save orchestrator output
    print("\n3. Testing orchestrator output save...")
    orchestrator_output = OrchestratorOutput(
        timestamp=datetime.now().isoformat(),
        topic="test project",
        executive_summary="Test summary",
        business_plan={"test": "plan"},
        grant_strategy={"test": "strategy"},
        financial_projections={"test": "projections"},
        implementation_timeline=[{"phase": "test", "activities": "testing"}],
        risk_assessment={"test": "risks"},
        success_metrics=["metric 1"],
        source_reports=["test.json"]
    )
    
    filepath = output_manager.save_orchestrator_output(orchestrator_output)
    assert Path(filepath).exists(), f"File not created: {filepath}"
    print(f"✓ Orchestrator output saved: {Path(filepath).name}")
    
    # Test 4: Save dorks
    print("\n4. Testing dork save...")
    dorks = {
        "google": "test google dork",
        "bing": "test bing dork",
        "duckduckgo": "test ddg dork"
    }
    
    filepath = output_manager.save_dorks("test topic", "Michigan", dorks)
    assert Path(filepath).exists(), f"File not created: {filepath}"
    print(f"✓ Dorks saved: {Path(filepath).name}")
    
    # Test 5: Read advisor outputs
    print("\n5. Testing read advisor outputs...")
    advisor_outputs = output_manager.read_advisor_outputs(topic="test project")
    assert len(advisor_outputs) > 0, "No advisor outputs found"
    print(f"✓ Found {len(advisor_outputs)} advisor output(s)")
    
    # Test 6: Read orchestrator outputs
    print("\n6. Testing read orchestrator outputs...")
    orchestrator_outputs = output_manager.read_orchestrator_outputs()
    assert len(orchestrator_outputs) > 0, "No orchestrator outputs found"
    print(f"✓ Found {len(orchestrator_outputs)} orchestrator output(s)")
    
    # Test 7: List files
    print("\n7. Testing list operations...")
    advisor_files = output_manager.list_advisor_files()
    orchestrator_files = output_manager.list_orchestrator_files()
    print(f"✓ Advisor files: {len(advisor_files)}")
    print(f"✓ Orchestrator files: {len(orchestrator_files)}")
    
    # Test 8: Get session outputs
    print("\n8. Testing session outputs...")
    session = output_manager.get_session_outputs(topic="test project")
    print(f"✓ Session data:")
    print(f"  - Topic: {session['topic']}")
    print(f"  - Advisor reports: {session['total_advisors']}")
    print(f"  - Final plans: {session['total_plans']}")
    
    print("\n" + "=" * 80)
    print("✅ ALL TESTS PASSED")
    print("=" * 80)
    
    return True


def test_workflow_simulation():
    """Simulate complete workflow."""
    
    print("\n\n" + "=" * 80)
    print("SIMULATING COMPLETE WORKFLOW")
    print("=" * 80)
    
    topic = "community health initiative"
    
    # Step 1: Financial Advisor
    print(f"\n📊 Step 1: Financial Advisor analyzes '{topic}'...")
    financial_output = AdvisorOutput(
        advisor_type="financial",
        timestamp=datetime.now().isoformat(),
        topic=topic,
        analysis={
            "budget": "$100,000",
            "funding_gap": "$75,000"
        },
        recommendations=[
            "Seek grant funding",
            "Build financial reserves"
        ],
        metadata={"version": "1.0"}
    )
    f_path = output_manager.save_advisor_output(financial_output)
    print(f"✓ Saved: {Path(f_path).name}")
    
    # Step 2: Grant Advisor
    print(f"\n🎯 Step 2: Grant Advisor analyzes '{topic}'...")
    grant_output = AdvisorOutput(
        advisor_type="grant",
        timestamp=datetime.now().isoformat(),
        topic=topic,
        analysis={
            "opportunities": ["Federal grants", "State grants"],
            "success_rate": "65%"
        },
        recommendations=[
            "Apply to federal programs",
            "Build local partnerships"
        ],
        metadata={"version": "1.0"}
    )
    g_path = output_manager.save_advisor_output(grant_output)
    print(f"✓ Saved: {Path(g_path).name}")
    
    # Step 3: Research Advisor
    print(f"\n🔬 Step 3: Research Advisor analyzes '{topic}'...")
    research_output = AdvisorOutput(
        advisor_type="research",
        timestamp=datetime.now().isoformat(),
        topic=topic,
        analysis={
            "market_size": "Large",
            "competition": "Moderate"
        },
        recommendations=[
            "Conduct needs assessment",
            "Document impact"
        ],
        metadata={"version": "1.0"}
    )
    r_path = output_manager.save_advisor_output(research_output)
    print(f"✓ Saved: {Path(r_path).name}")
    
    # Step 4: Orchestrator reads and synthesizes
    print(f"\n🎯 Step 4: Orchestrator reads all advisor reports for '{topic}'...")
    advisor_reports = output_manager.read_advisor_outputs(topic=topic)
    print(f"✓ Found {len(advisor_reports)} advisor reports")
    
    print(f"\n🎯 Step 5: Orchestrator synthesizes final plan...")
    final_plan = OrchestratorOutput(
        timestamp=datetime.now().isoformat(),
        topic=topic,
        executive_summary=f"Comprehensive plan based on {len(advisor_reports)} advisor reports",
        business_plan={"mission": "Serve community health needs"},
        grant_strategy={"approach": "Multi-source funding"},
        financial_projections={"year_1": "$75,000"},
        implementation_timeline=[
            {"phase": "Q1", "activities": "Prepare applications"},
            {"phase": "Q2", "activities": "Submit grants"}
        ],
        risk_assessment={"risks": ["Funding delays"]},
        success_metrics=["30% grant success rate"],
        source_reports=[Path(f_path).name, Path(g_path).name, Path(r_path).name]
    )
    plan_path = output_manager.save_orchestrator_output(final_plan)
    print(f"✓ Saved: {Path(plan_path).name}")
    
    print("\n" + "=" * 80)
    print("✅ WORKFLOW SIMULATION COMPLETE")
    print("=" * 80)
    print("\n📁 Output Files:")
    print(f"  - Advisor Reports: {output_manager.advisors_dir}")
    print(f"  - Final Plans: {output_manager.orchestrator_dir}")
    print("\n🔍 You can now view these files in:")
    print("  - app_enhanced.py (Gradio UI)")
    print("  - Any text editor or JSON viewer")
    
    return True


if __name__ == "__main__":
    try:
        # Run tests
        test_output_manager()
        test_workflow_simulation()
        
        print("\n" + "=" * 80)
        print("🎉 ALL TESTS PASSED - SYSTEM READY")
        print("=" * 80)
        print("\nNext steps:")
        print("1. Run Gradio app: python app_enhanced.py")
        print("2. View outputs in dual-window interface")
        print("3. Deploy to Hugging Face Space or use as MCP server")
        
        exit(0)
    except Exception as e:
        print(f"\n❌ TEST FAILED: {e}")
        import traceback
        traceback.print_exc()
        exit(1)
