"""
Enhanced Gradio App for MAI Advisor - Hugging Face Space
Dual-window interface for viewing advisor outputs and final orchestrator plans
"""
import gradio as gr
import json
from pathlib import Path
from datetime import datetime
import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from dork_generator import GrantDorkGenerator
from output_manager import output_manager, AdvisorOutput, OrchestratorOutput


def find_grants(topic: str, location: str = ""):
    """Generate grant search dorks."""
    if not topic or not topic.strip():
        return "❌ **Error:** Please enter a topic for your grant search."
    
    # Generate dorks
    dorks = GrantDorkGenerator.generate_all_dorks(
        topic=topic.strip(),
        location=location.strip() if location else None
    )
    
    # Save using output manager
    filepath = output_manager.save_dorks(topic.strip(), location.strip() if location else None, dorks)
    
    # Format response
    result = f"""# ✅ Grant Search Dorks Generated!

**Topic:** {topic}  
**Location:** {location or "Not specified"}  
**Saved to:** `{Path(filepath).name}`

---

## 🔍 Google Dork

```
{dorks['google']}
```

---

## 🔍 Bing Dork

```
{dorks['bing']}
```

---

## 🔍 DuckDuckGo Dork

```
{dorks['duckduckgo']}
```
"""
    
    return result


def simulate_advisor_analysis(topic: str, advisor_type: str = "financial"):
    """Simulate advisor analysis and save output."""
    if not topic or not topic.strip():
        return "❌ Please enter a topic.", ""
    
    # Simulate advisor analysis
    if advisor_type == "financial":
        analysis = {
            "budget_analysis": {
                "estimated_project_cost": "$50,000 - $150,000",
                "funding_gap": "$75,000",
                "sustainability_score": "7/10"
            },
            "revenue_streams": [
                "Grant funding (primary)",
                "Program fees (supplemental)",
                "Partnerships (in-kind)"
            ],
            "cost_breakdown": {
                "personnel": "60%",
                "operations": "25%",
                "program_delivery": "15%"
            }
        }
        recommendations = [
            "Seek multi-year grants for sustainability",
            "Develop diversified funding strategy",
            "Build 3-month operating reserve",
            "Track metrics for future grant applications"
        ]
    elif advisor_type == "grant":
        analysis = {
            "identified_opportunities": [
                "Federal STEM Education Grants",
                "State Community Development Funds",
                "Foundation Capacity Building Grants"
            ],
            "eligibility_assessment": "Strong fit for 501(c)(3) organizations",
            "competition_level": "Moderate to High",
            "success_probability": "65-75%"
        }
        recommendations = [
            "Prioritize federal grants with longer timelines",
            "Build relationships with program officers",
            "Develop compelling impact narratives",
            "Create grant calendar for strategic planning"
        ]
    else:  # research
        analysis = {
            "market_research": {
                "target_population": "Underserved communities",
                "geographic_focus": "Regional with expansion potential",
                "competitive_landscape": "Limited direct competitors"
            },
            "trends": [
                "Increasing foundation interest in topic area",
                "Federal funding priorities align with mission",
                "Growing evidence base supports approach"
            ]
        }
        recommendations = [
            "Conduct needs assessment survey",
            "Document community partnerships",
            "Gather preliminary impact data",
            "Review successful grant proposals in field"
        ]
    
    # Create advisor output
    output = AdvisorOutput(
        advisor_type=advisor_type,
        timestamp=datetime.now().isoformat(),
        topic=topic,
        analysis=analysis,
        recommendations=recommendations,
        metadata={
            "version": "1.0",
            "simulated": True,
            "model": "demo"
        }
    )
    
    # Save output
    filepath = output_manager.save_advisor_output(output)
    
    summary = f"""# ✅ {advisor_type.title()} Advisor Analysis Complete

**Topic:** {topic}  
**Saved to:** `{Path(filepath).name}`

## Recommendations

{chr(10).join(f'{i+1}. {rec}' for i, rec in enumerate(recommendations))}
"""
    
    detail = f"""## Detailed Analysis

```json
{json.dumps(analysis, indent=2)}
```
"""
    
    return summary, detail


def orchestrate_plan(topic: str):
    """Read all advisor outputs and generate final synthesized plan."""
    if not topic or not topic.strip():
        return "❌ Please enter a topic.", ""
    
    # Read advisor outputs for this topic
    advisor_outputs = output_manager.read_advisor_outputs(topic=topic)
    
    if not advisor_outputs:
        return f"""❌ No advisor reports found for topic: "{topic}"

Please run the advisor analyses first in the "Advisor Analyses" tab.
""", ""
    
    # Synthesize plan (in production, this would use orchestration with Gemini/Perplexity)
    business_plan = {
        "mission": f"Deliver impactful {topic} programs to underserved communities",
        "goals": [
            "Secure $100K+ in grant funding within 12 months",
            "Serve 500+ beneficiaries in year one",
            "Build sustainable revenue model by year two"
        ],
        "strategies": [
            "Multi-faceted grant application approach",
            "Community partnership development",
            "Evidence-based program delivery"
        ]
    }
    
    grant_strategy = {
        "priority_grants": [
            "Federal STEM Education - Due Q2 2026",
            "State Community Development - Rolling",
            "Foundation Capacity Building - Due Q4 2026"
        ],
        "application_timeline": "6-month preparation, 3-month submission cycle",
        "success_factors": [
            "Strong community partnerships",
            "Documented need and impact",
            "Sustainable financial model"
        ]
    }
    
    financial_projections = {
        "year_1": {"revenue": "$75,000", "expenses": "$65,000", "surplus": "$10,000"},
        "year_2": {"revenue": "$150,000", "expenses": "$135,000", "surplus": "$15,000"},
        "year_3": {"revenue": "$225,000", "expenses": "$195,000", "surplus": "$30,000"}
    }
    
    implementation_timeline = [
        {"phase": "Month 1-2", "activities": "Finalize grant calendar, gather documentation"},
        {"phase": "Month 3-4", "activities": "Submit first grant applications"},
        {"phase": "Month 5-6", "activities": "Follow up, prepare for site visits"},
        {"phase": "Month 7-12", "activities": "Award notifications, program launch"}
    ]
    
    risk_assessment = {
        "high_risks": ["Grant funding delays", "Key staff turnover"],
        "medium_risks": ["Budget overruns", "Partnership challenges"],
        "mitigation": [
            "Maintain 3-month operating reserve",
            "Diversify funding sources",
            "Build strong governance structure"
        ]
    }
    
    success_metrics = [
        "Grant success rate: 30%+ of applications funded",
        "Cost per beneficiary: <$200",
        "Stakeholder satisfaction: 85%+",
        "Financial sustainability: Positive cash flow by month 12"
    ]
    
    # Create orchestrator output
    output = OrchestratorOutput(
        timestamp=datetime.now().isoformat(),
        topic=topic,
        executive_summary=f"Comprehensive business and grant plan for {topic} initiative, "
                         f"synthesized from {len(advisor_outputs)} advisor reports.",
        business_plan=business_plan,
        grant_strategy=grant_strategy,
        financial_projections=financial_projections,
        implementation_timeline=implementation_timeline,
        risk_assessment=risk_assessment,
        success_metrics=success_metrics,
        source_reports=[f"report_{i}.json" for i in range(len(advisor_outputs))]
    )
    
    # Save orchestrator output
    filepath = output_manager.save_orchestrator_output(output)
    
    summary = f"""# 🎯 Final Business & Grant Plan

**Topic:** {topic}  
**Saved to:** `{Path(filepath).name}`  
**Based on:** {len(advisor_outputs)} advisor reports

## Executive Summary

{output.executive_summary}

## Success Metrics

{chr(10).join(f'- {metric}' for metric in success_metrics)}
"""
    
    detail = f"""## Business Plan

```json
{json.dumps(business_plan, indent=2)}
```

## Grant Strategy

```json
{json.dumps(grant_strategy, indent=2)}
```

## Financial Projections

```json
{json.dumps(financial_projections, indent=2)}
```

## Implementation Timeline

{chr(10).join(f"**{item['phase']}:** {item['activities']}" for item in implementation_timeline)}

## Risk Assessment

```json
{json.dumps(risk_assessment, indent=2)}
```
"""
    
    return summary, detail


def view_advisor_files():
    """List all advisor output files with metadata."""
    files = output_manager.list_advisor_files()
    
    if not files:
        return "No advisor reports found.", ""
    
    file_list = "# 📁 Advisor Reports\n\n"
    for f in files:
        file_list += f"**{f['filename']}**\n"
        file_list += f"- Size: {f['size_kb']} KB\n"
        file_list += f"- Modified: {f['modified']}\n\n"
    
    latest_file = files[0]['path'] if files else None
    latest_content = ""
    
    if latest_file:
        try:
            with open(latest_file, 'r', encoding='utf-8') as file:
                data = json.load(file)
            latest_content = f"```json\n{json.dumps(data, indent=2)}\n```"
        except Exception:
            latest_content = "Error loading file content"
    
    return file_list, latest_content


def view_orchestrator_files():
    """List all orchestrator output files with metadata."""
    files = output_manager.list_orchestrator_files()
    
    if not files:
        return "No final plans found.", ""
    
    file_list = "# 📊 Final Business & Grant Plans\n\n"
    for f in files:
        file_list += f"**{f['filename']}**\n"
        file_list += f"- Size: {f['size_kb']} KB\n"
        file_list += f"- Modified: {f['modified']}\n\n"
    
    latest_file = files[0]['path'] if files else None
    latest_content = ""
    
    if latest_file:
        try:
            with open(latest_file, 'r', encoding='utf-8') as file:
                data = json.load(file)
            latest_content = f"```json\n{json.dumps(data, indent=2)}\n```"
        except Exception:
            latest_content = "Error loading file content"
    
    return file_list, latest_content


# Create Gradio interface with dual windows
with gr.Blocks(title="MAI Advisor", theme=gr.themes.Soft()) as demo:
    gr.Markdown("""
    # 🎯 MAI Advisor - AI-Powered Grant Finding & Business Planning
    
    **Complete Workflow:**
    1. 🔍 Generate grant search dorks
    2. 👥 Run advisor analyses (Financial, Grant, Research)
    3. 🎯 Generate final synthesized business & grant plan
    4. 📂 View all outputs in organized dual-window viewers
    """)
    
    with gr.Tabs():
        # Tab 1: Grant Dork Generation
        with gr.Tab("🔍 Grant Search"):
            with gr.Row():
                with gr.Column():
                    topic_input = gr.Textbox(
                        label="Topic/Focus Area",
                        placeholder="e.g., indigenous education technology",
                        lines=2
                    )
                    location_input = gr.Textbox(
                        label="Location (comma-separated)",
                        placeholder="e.g., Michigan, Minnesota",
                        lines=1
                    )
                    generate_btn = gr.Button("🔍 Generate Dorks", variant="primary")
                
                with gr.Column():
                    dorks_output = gr.Markdown()
            
            generate_btn.click(
                fn=find_grants,
                inputs=[topic_input, location_input],
                outputs=dorks_output
            )
        
        # Tab 2: Advisor Analyses
        with gr.Tab("👥 Advisor Analyses"):
            with gr.Row():
                with gr.Column(scale=1):
                    advisor_topic = gr.Textbox(
                        label="Topic/Project",
                        placeholder="e.g., community health initiative",
                        lines=2
                    )
                    advisor_type = gr.Radio(
                        choices=["financial", "grant", "research"],
                        label="Advisor Type",
                        value="financial"
                    )
                    analyze_btn = gr.Button("▶️ Run Analysis", variant="primary")
                
                with gr.Column(scale=2):
                    gr.Markdown("### Summary")
                    advisor_summary = gr.Markdown()
                
                with gr.Column(scale=2):
                    gr.Markdown("### Details")
                    advisor_details = gr.Markdown()
            
            analyze_btn.click(
                fn=simulate_advisor_analysis,
                inputs=[advisor_topic, advisor_type],
                outputs=[advisor_summary, advisor_details]
            )
        
        # Tab 3: Final Orchestrated Plan
        with gr.Tab("🎯 Final Plan"):
            with gr.Row():
                with gr.Column(scale=1):
                    plan_topic = gr.Textbox(
                        label="Topic (must match advisor analyses)",
                        placeholder="e.g., community health initiative",
                        lines=2
                    )
                    orchestrate_btn = gr.Button("🎯 Generate Plan", variant="primary")
                
                with gr.Column(scale=2):
                    gr.Markdown("### Executive Summary")
                    plan_summary = gr.Markdown()
                
                with gr.Column(scale=2):
                    gr.Markdown("### Detailed Plan")
                    plan_details = gr.Markdown()
            
            orchestrate_btn.click(
                fn=orchestrate_plan,
                inputs=[plan_topic],
                outputs=[plan_summary, plan_details]
            )
        
        # Tab 4: View Advisor Outputs (Dual Window)
        with gr.Tab("📂 Advisor Reports"):
            gr.Markdown("### Dual-Window Viewer: Advisor Outputs")
            
            with gr.Row():
                refresh_advisors = gr.Button("🔄 Refresh", variant="secondary")
            
            with gr.Row():
                with gr.Column(scale=1):
                    gr.Markdown("#### File List")
                    advisor_file_list = gr.Markdown()
                
                with gr.Column(scale=2):
                    gr.Markdown("#### Latest File Content")
                    advisor_file_content = gr.Markdown()
            
            refresh_advisors.click(
                fn=view_advisor_files,
                outputs=[advisor_file_list, advisor_file_content]
            )
            
            # Auto-load on tab open
            demo.load(
                fn=view_advisor_files,
                outputs=[advisor_file_list, advisor_file_content]
            )
        
        # Tab 5: View Orchestrator Outputs (Dual Window)
        with gr.Tab("📊 Final Plans"):
            gr.Markdown("### Dual-Window Viewer: Final Plans")
            
            with gr.Row():
                refresh_plans = gr.Button("🔄 Refresh", variant="secondary")
            
            with gr.Row():
                with gr.Column(scale=1):
                    gr.Markdown("#### File List")
                    plan_file_list = gr.Markdown()
                
                with gr.Column(scale=2):
                    gr.Markdown("#### Latest File Content")
                    plan_file_content = gr.Markdown()
            
            refresh_plans.click(
                fn=view_orchestrator_files,
                outputs=[plan_file_list, plan_file_content]
            )
            
            # Auto-load on tab open
            demo.load(
                fn=view_orchestrator_files,
                outputs=[plan_file_list, plan_file_content]
            )
    
    gr.Markdown("""
    ---
    ### 📁 Output Directory Structure
    
    - **`advisors_output/`** - Individual advisor reports (financial, grant, research)
    - **`orchestrator_output/`** - Final synthesized business & grant plans
    - **`grant_dorks/`** - Generated search dorks
    
    All outputs are JSON files accessible via MCP server and viewable in dual-window interface.
    """)


if __name__ == "__main__":
    demo.launch()
