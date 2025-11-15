"""
MAI Advisor MCP - Hugging Face Space Demo
AI-Powered Grant and Funding Opportunity Finder

This is a demo interface for the MAI Advisor MCP server.
For the full MCP server implementation, see the src/ directory.
"""

import gradio as gr
import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from search_operators import (
    GrantSearchCriteria,
    UnifiedSearchOperatorGenerator,
    SearchEngine
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
            funding_range_min=int(funding_min) if funding_min else None,
            funding_range_max=int(funding_max) if funding_max else None
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
        output = generator.format_for_display(queries)
        
        return output
        
    except Exception as e:
        return f"❌ Error: {str(e)}"


# Create Gradio interface
with gr.Blocks(title="MAI Advisor MCP - Grant Finder", theme=gr.themes.Soft()) as demo:
    gr.Markdown("""
    # 🎯 MAI Advisor MCP - Grant Finder
    
    **AI-Powered Grant and Funding Opportunity Search**
    
    Generate optimized search queries for Google, Bing, and DuckDuckGo to find grant opportunities.
    This tool creates advanced search operators tailored to your specific needs.
    
    ---
    """)
    
    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("### 📝 Search Criteria")
            
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
                    label="Min Funding ($)",
                    value=None,
                    precision=0
                )
                funding_max_input = gr.Number(
                    label="Max Funding ($)",
                    value=None,
                    precision=0
                )
            
            engines_input = gr.CheckboxGroup(
                label="Search Engines",
                choices=["Google", "Bing", "DuckDuckGo"],
                value=["Google", "Bing", "DuckDuckGo"]
            )
            
            generate_btn = gr.Button("🔍 Generate Search Queries", variant="primary", size="lg")
        
        with gr.Column(scale=2):
            gr.Markdown("### 📊 Generated Search Queries")
            output = gr.Textbox(
                label="Copy and paste these queries into search engines",
                lines=25,
                max_lines=30,
                show_copy_button=True
            )
    
    # Examples
    gr.Markdown("### 💡 Example Searches")
    
    with gr.Row():
        gr.Examples(
            examples=[
                ["education, technology, STEM", "nonprofit", "education", "California", 25000, 250000, ["Google", "Bing"]],
                ["climate, sustainability, renewable energy", "nonprofit", "environmental", "", 50000, 500000, ["Google", "DuckDuckGo"]],
                ["small business, innovation", "business", "technology", "New York", 10000, 100000, ["Google", "Bing"]],
                ["arts, culture, creative", "nonprofit", "arts", "", None, 50000, ["Google", "DuckDuckGo"]],
            ],
            inputs=[keywords_input, org_type_input, sector_input, location_input, 
                   funding_min_input, funding_max_input, engines_input],
        )
    
    # Footer
    gr.Markdown("""
    ---
    
    ### 🚀 About MAI Advisor MCP
    
    This is a demo of the **MAI Advisor MCP** (Model Context Protocol) server - an AI-powered grant finder
    built for the MCP's 1st Birthday Hackathon.
    
    **Features:**
    - Multi-engine search operator generation (Google, Bing, DuckDuckGo)
    - AI-powered deep research capabilities
    - Full MCP server integration for Claude Desktop
    - Advanced filtering by organization type, sector, location, funding range
    
    **Links:**
    - [GitHub Repository](https://github.com/nbiish/mai-advisor-mcp)
    - [Full Documentation](https://github.com/nbiish/mai-advisor-mcp/blob/main/grant-finder-mcp/README.md)
    - [Quick Start Guide](https://github.com/nbiish/mai-advisor-mcp/blob/main/grant-finder-mcp/QUICKSTART.md)
    
    **Built with:** MCP, LangChain, Claude AI, and Tavily Search
    
    *For the complete MCP server with AI research capabilities, see the repository.*
    """)
    
    # Connect button to function
    generate_btn.click(
        fn=generate_search_queries,
        inputs=[keywords_input, org_type_input, sector_input, location_input,
               funding_min_input, funding_max_input, engines_input],
        outputs=output
    )

# Launch the app
if __name__ == "__main__":
    demo.launch()
