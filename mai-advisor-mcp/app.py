"""
MAI Advisor MCP - Hugging Face Space Demo
AI-Powered Grant and Funding Opportunity Finder

This is a demo interface for the MAI Advisor MCP server.
For the full MCP server implementation, see the src/ directory.
"""

import gradio as gr
import sys
import os
import json

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from search_operators import (
    GrantSearchCriteria,
    UnifiedSearchOperatorGenerator,
    SearchEngine
)
from advisor_tools import (
    MAIAdvisorWorkflow,
    AdvisorQuery,
    FinancialAdvisor
)

def generate_search_queries(
    keywords_text,
    org_type,
    sector,
    location,
    funding_min,
    funding_max,
    search_engines
):
    """Generate optimized search queries for grant finding."""
    try:
        # Parse keywords
        keywords = [k.strip() for k in keywords_text.split(',') if k.strip()]
        if not keywords:
            return "❌ Please enter at least one keyword"
        
        # Create criteria
        criteria = GrantSearchCriteria(
            keywords=keywords,
            organization_type=org_type if org_type != "Any" else None,
            sector=sector if sector != "Any" else None,
            location=location if location else None,
            amount_min=int(funding_min) if funding_min else None,
            amount_max=int(funding_max) if funding_max else None
        )
        
        # Parse engines
        engine_map = {
            "Google": SearchEngine.GOOGLE,
            "Bing": SearchEngine.BING,
            "DuckDuckGo": SearchEngine.DUCKDUCKGO
        }
        engines = [engine_map[e] for e in search_engines]
        
        # Generate queries
        generator = UnifiedSearchOperatorGenerator()
        queries = generator.generate_queries(criteria, engines)
        
        # Format output
        result = generator.format_for_display(queries)
        
        return result
        
    except ValueError as ve:
        return f"❌ Validation Error: {str(ve)}"
    except KeyError as ke:
        return f"❌ Configuration Error: {str(ke)}"
    except Exception as e:
        return f"❌ Error: {str(e)}"


def run_full_workflow(
    topic,
    context,
    org_type,
    sector,
    amount_min,
    amount_max,
    timeline,
    include_financial
):
    """Run the complete MAI Advisor workflow."""
    try:
        # Build amount range
        amount_range = None
        if amount_min or amount_max:
            amount_range = {}
            if amount_min:
                amount_range["min"] = int(amount_min)
            if amount_max:
                amount_range["max"] = int(amount_max)
        
        # Create query
        query = AdvisorQuery(
            topic=topic,
            context=context if context else None,
            organization_type=org_type if org_type != "Any" else None,
            sector=sector if sector != "Any" else None,
            amount_range=amount_range,
            timeline=timeline if timeline else None
        )
        
        # Execute workflow
        workflow = MAIAdvisorWorkflow()
        result = workflow.execute_workflow(query, include_financial_guidance=include_financial)
        
        # Format output
        output = "# 🎯 MAI Advisor Workflow Results\n\n"
        
        # Expert Analysis
        output += "## 📊 Expert Analysis\n\n"
        output += f"**Request Summary:**\n{result['expert_analysis']['request_summary']}\n\n"
        
        output += "**Strategic Approach:**\n"
        strategy = result['expert_analysis']['strategic_approach']
        output += f"- Primary Focus: {', '.join(strategy['primary_focus'])}\n"
        output += f"- Search Priorities: {', '.join(strategy['search_priorities'])}\n"
        output += f"- Recommended Sources: {', '.join(strategy['recommended_sources'])}\n\n"
        
        # Search Dorks
        output += "## 🔍 Ready-to-Use Search Queries\n\n"
        dorks = result['search_dorks']['dorks']
        
        if dorks.get('google'):
            output += "### Google Queries\n"
            for i, query in enumerate(dorks['google'], 1):
                output += f"{i}. `{query}`\n\n"
        
        if dorks.get('bing'):
            output += "### Bing Queries\n"
            for i, query in enumerate(dorks['bing'], 1):
                output += f"{i}. `{query}`\n\n"
        
        if dorks.get('duckduckgo'):
            output += "### DuckDuckGo Queries\n"
            for i, query in enumerate(dorks['duckduckgo'], 1):
                output += f"{i}. `{query}`\n\n"
        
        # Financial Guidance
        if include_financial and result.get('financial_guidance'):
            output += "## 💰 Financial Guidance\n\n"
            fg = result['financial_guidance']
            output += f"**Stage:** {fg['process_stage']}\n\n"
            
            output += "**Recommendations:**\n"
            for rec in fg['recommendations']:
                output += f"- {rec}\n"
            output += "\n"
            
            output += "**Budget Considerations:**\n"
            for bc in fg['budget_considerations']:
                output += f"- {bc}\n"
            output += "\n"
            
            output += f"**Timeline:** {fg['timeline_guidance']}\n\n"
            
            output += "**Next Steps:**\n"
            for step in fg['next_steps']:
                output += f"- {step}\n"
            output += "\n"
        
        # Timeline
        output += "## ⏱️ Timeline Estimate\n\n"
        output += result['expert_analysis']['timeline_estimate']
        
        return output
        
    except ValueError as ve:
        return f"❌ Validation Error: {str(ve)}"
    except KeyError as ke:
        return f"❌ Configuration Error: {str(ke)}"
    except Exception as e:
        return f"❌ Unexpected Error: {str(e)}\n\nPlease try again or simplify your query."


def get_financial_advice(stage, amount_min, amount_max, org_type):
    """Get financial guidance for a specific stage."""
    try:
        # Build amount range
        amount_range = None
        if amount_min or amount_max:
            amount_range = {}
            if amount_min:
                amount_range["min"] = int(amount_min)
            if amount_max:
                amount_range["max"] = int(amount_max)
        
        advisor = FinancialAdvisor()
        guidance = advisor.provide_guidance(
            stage=stage.lower(),
            amount_range=amount_range,
            organization_type=org_type if org_type != "Any" else None
        )
        
        # Format output
        output = f"# 💰 Financial Guidance: {guidance.process_stage}\n\n"
        
        output += "## Recommendations\n"
        for rec in guidance.recommendations:
            output += f"- {rec}\n"
        output += "\n"
        
        output += "## Budget Considerations\n"
        for bc in guidance.budget_considerations:
            output += f"- {bc}\n"
        output += "\n"
        
        output += f"## Timeline\n{guidance.timeline_guidance}\n\n"
        
        if guidance.risk_assessment:
            output += f"## Risk Assessment\n{guidance.risk_assessment}\n\n"
        
        output += "## Next Steps\n"
        for step in guidance.next_steps:
            output += f"- {step}\n"
        
        return output
        
    except ValueError as ve:
        return f"❌ Validation Error: {str(ve)}"
    except KeyError as ke:
        return f"❌ Configuration Error: {str(ke)}"
    except Exception as e:
        return f"❌ Error: {str(e)}"


# Create Gradio interface
with gr.Blocks(title="MAI Advisor MCP - Grant Finder", theme=gr.themes.Soft()) as demo:
    gr.Markdown("""
    # 🎯 MAI Advisor MCP - AI-Powered Grant Finder
    
    **Built for MCP's 1st Birthday Hackathon**
    
    Generate search queries, get expert analysis, and receive financial guidance for grant opportunities.
    
    ---
    """)
    
    with gr.Tabs():
        # Tab 1: Full Workflow
        with gr.TabItem("🚀 Full Workflow"):
            gr.Markdown("""
            ### Complete Grant Research Workflow
            Get expert analysis, research tasks, search queries, and financial guidance all in one place.
            """)
            
            with gr.Row():
                with gr.Column(scale=1):
                    wf_topic = gr.Textbox(
                        label="Topic / Grant Focus",
                        placeholder="e.g., Indigenous education technology",
                        lines=2
                    )
                    
                    wf_context = gr.Textbox(
                        label="Additional Context (optional)",
                        placeholder="e.g., Pilot project for remote communities",
                        lines=2
                    )
                    
                    wf_org_type = gr.Dropdown(
                        label="Organization Type",
                        choices=["Any", "nonprofit", "business", "university", "individual"],
                        value="nonprofit"
                    )
                    
                    wf_sector = gr.Dropdown(
                        label="Sector",
                        choices=["Any", "education", "healthcare", "technology", "arts", 
                                "environmental", "research", "community development"],
                        value="education"
                    )
                    
                    with gr.Row():
                        wf_amount_min = gr.Number(
                            label="Min Amount ($)",
                            value=25000,
                            precision=0
                        )
                        wf_amount_max = gr.Number(
                            label="Max Amount ($)",
                            value=250000,
                            precision=0
                        )
                    
                    wf_timeline = gr.Textbox(
                        label="Timeline / Urgency",
                        placeholder="e.g., Need funding within 6 months"
                    )
                    
                    wf_include_financial = gr.Checkbox(
                        label="Include Financial Guidance",
                        value=True
                    )
                    
                    wf_run_btn = gr.Button("🚀 Run Full Workflow", variant="primary", size="lg")
                
                with gr.Column(scale=2):
                    wf_output = gr.Markdown(label="Results")
            
            wf_run_btn.click(
                fn=run_full_workflow,
                inputs=[wf_topic, wf_context, wf_org_type, wf_sector, 
                       wf_amount_min, wf_amount_max, wf_timeline, wf_include_financial],
                outputs=wf_output
            )
        
        # Tab 2: Search Query Generator
        with gr.TabItem("🔍 Search Queries"):
            gr.Markdown("""
            ### Generate Optimized Search Queries
            Create advanced search operators for Google, Bing, and DuckDuckGo.
            """)
            
            with gr.Row():
                with gr.Column(scale=1):
                    keywords_input = gr.Textbox(
                        label="Keywords (comma-separated)",
                        placeholder="e.g., education, technology, STEM",
                        lines=2
                    )
                    
                    org_type_input = gr.Dropdown(
                        label="Organization Type",
                        choices=["Any", "nonprofit", "business", "university", "individual"],
                        value="Any"
                    )
                    
                    sector_input = gr.Dropdown(
                        label="Sector",
                        choices=["Any", "education", "healthcare", "technology", "arts", 
                                "environmental", "research", "community development"],
                        value="Any"
                    )
                    
                    location_input = gr.Textbox(
                        label="Location (optional)",
                        placeholder="e.g., California, New York"
                    )
                    
                    with gr.Row():
                        funding_min_input = gr.Number(
                            label="Min Amount ($)",
                            value=None,
                            precision=0
                        )
                        funding_max_input = gr.Number(
                            label="Max Amount ($)",
                            value=None,
                            precision=0
                        )
                    
                    engines_input = gr.CheckboxGroup(
                        label="Search Engines",
                        choices=["Google", "Bing", "DuckDuckGo"],
                        value=["Google", "Bing", "DuckDuckGo"]
                    )
                    
                    generate_btn = gr.Button("🔍 Generate Queries", variant="primary", size="lg")
                
                with gr.Column(scale=2):
                    sq_output = gr.Textbox(
                        label="Copy and paste these queries into search engines",
                        lines=20,
                        max_lines=25,
                        show_copy_button=True
                    )
            
            generate_btn.click(
                fn=generate_search_queries,
                inputs=[keywords_input, org_type_input, sector_input, location_input,
                       funding_min_input, funding_max_input, engines_input],
                outputs=sq_output
            )
            
            # Examples
            gr.Markdown("### 💡 Example Searches")
            gr.Examples(
                examples=[
                    ["education, technology, STEM", "nonprofit", "education", "California", 25000, 250000, ["Google", "Bing"]],
                    ["climate, sustainability", "nonprofit", "environmental", "", 50000, 500000, ["Google", "DuckDuckGo"]],
                    ["small business, innovation", "business", "technology", "New York", 10000, 100000, ["Google"]],
                ],
                inputs=[keywords_input, org_type_input, sector_input, location_input, 
                       funding_min_input, funding_max_input, engines_input],
            )
        
        # Tab 3: Financial Guidance
        with gr.TabItem("💰 Financial Guidance"):
            gr.Markdown("""
            ### Get Expert Financial Advice
            Receive stage-specific guidance for grant seeking and management.
            """)
            
            with gr.Row():
                with gr.Column(scale=1):
                    fg_stage = gr.Dropdown(
                        label="Process Stage",
                        choices=["Research", "Planning", "Application", "Management", "General"],
                        value="Research"
                    )
                    
                    fg_org_type = gr.Dropdown(
                        label="Organization Type",
                        choices=["Any", "nonprofit", "business", "university"],
                        value="nonprofit"
                    )
                    
                    with gr.Row():
                        fg_amount_min = gr.Number(
                            label="Min Amount ($)",
                            value=None,
                            precision=0
                        )
                        fg_amount_max = gr.Number(
                            label="Max Amount ($)",
                            value=None,
                            precision=0
                        )
                    
                    fg_btn = gr.Button("💰 Get Financial Guidance", variant="primary", size="lg")
                
                with gr.Column(scale=2):
                    fg_output = gr.Markdown(label="Financial Guidance")
            
            fg_btn.click(
                fn=get_financial_advice,
                inputs=[fg_stage, fg_amount_min, fg_amount_max, fg_org_type],
                outputs=fg_output
            )
    
    # Footer
    gr.Markdown("""
    ---
    
    ### 🚀 About MAI Advisor MCP
    
    This demo showcases the **MAI Advisor MCP** (Model Context Protocol) server - an AI-powered grant finder
    built for the MCP's 1st Birthday Hackathon (Nov 14-30, 2025).
    
    **Features:**
    - 🎯 Complete workflow from research to application
    - 🔍 Multi-engine search operator generation
    - 💰 Expert financial guidance at every stage
    - 🤖 MCP server integration for Claude Desktop
    
    **Links:**
    - [GitHub Repository](https://github.com/nbiish/mai-advisor-mcp)
    - [Documentation](https://github.com/nbiish/mai-advisor-mcp/blob/main/mai-advisor-mcp/README.md)
    
    **Built with:** MCP, Python, Gradio, and AI-powered research tools
    """)

# Launch the app
if __name__ == "__main__":
    demo.launch()
