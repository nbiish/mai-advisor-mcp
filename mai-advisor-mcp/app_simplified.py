"""
MAI Advisor - Simplified Gradio Interface
Matches MCP tool interface: topic + location only
"""
import gradio as gr
import os
from pathlib import Path
import json
from datetime import datetime

# Add src to path for imports
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from dork_generator import GrantDorkGenerator

# Output directory
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "grant_dorks")
Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)


def find_grants(topic: str, location: str = ""):
    """
    Generate grant search dorks - matches MCP tool interface.
    
    Args:
        topic: Main focus/topic for grants
        location: Optional geographic targeting
        
    Returns:
        Formatted markdown with dorks and instructions
    """
    if not topic or not topic.strip():
        return "❌ **Error:** Please enter a topic for your grant search."
    
    # Generate dorks
    dorks = GrantDorkGenerator.generate_all_dorks(
        topic=topic.strip(),
        location=location.strip() if location else None
    )
    
    # Save to file
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_topic = "".join(c if c.isalnum() or c in (' ', '_') else '_' for c in topic)
    safe_topic = safe_topic.replace(' ', '_')[:50]
    filename = f"{timestamp}_{safe_topic}.json"
    filepath = os.path.join(OUTPUT_DIR, filename)
    
    output_data = {
        "generated_at": datetime.now().isoformat(),
        "topic": topic,
        "location": location or "Not specified",
        "dorks": dorks
    }
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)
    
    # Format response
    result = f"""# ✅ Grant Search Dorks Generated!

**Topic:** {topic}  
**Location:** {location or "Not specified"}  
**Saved to:** `{filepath}`

---

## 🔍 Google Dork

Copy and paste this into [Google Search](https://www.google.com/search):

```
{dorks['google']}
```

---

## 🔍 Bing Dork

Copy and paste this into [Bing Search](https://www.bing.com/search):

```
{dorks['bing']}
```

---

## 🔍 DuckDuckGo Dork

Copy and paste this into [DuckDuckGo Search](https://duckduckgo.com):

```
{dorks['duckduckgo']}
```

---

## 📋 How to Use

1. **Copy** one of the search queries above
2. **Paste** it into the corresponding search engine
3. **Press Enter** to see grant opportunities
4. **Review results** and visit relevant grant pages

## 💡 Tips

- Start with Google for comprehensive results
- Try all three engines for maximum coverage
- Look for `.pdf` and `.doc` files in results (often grant applications)
- Check government sites (.gov) and foundation sites (.org) first
- Save promising opportunities to review later

## 📁 Your Dork File

All dorks saved to: `{os.path.basename(filepath)}`

Location: `{OUTPUT_DIR}`
"""
    
    return result


# Create Gradio interface
with gr.Blocks(title="MAI Advisor - Grant Finder", theme=gr.themes.Soft()) as demo:
    gr.Markdown("""
    # 🎯 MAI Advisor - AI-Powered Grant Finder
    
    **Simple Interface. Powerful Results.**
    
    Generate comprehensive search queries (Google dorks) for finding grant opportunities.
    Just enter your topic and location - our expert system handles the rest.
    
    Built for **MCP's 1st Birthday Hackathon** 🎉
    
    ---
    """)
    
    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("### 📝 Your Grant Search")
            
            topic_input = gr.Textbox(
                label="What are you looking for?",
                placeholder="e.g., indigenous education technology, climate sustainability, small business innovation",
                lines=3,
                info="Be as specific or general as you like. Our expert system will analyze and optimize."
            )
            
            location_input = gr.Textbox(
                label="Location (optional)",
                placeholder="e.g., Michigan, Minnesota or California or leave blank for nationwide",
                lines=1,
                info="City, state, country, or comma-separated list. Leave blank for all locations."
            )
            
            search_btn = gr.Button(
                "🔍 Generate Grant Search Queries",
                variant="primary",
                size="lg"
            )
            
            gr.Markdown("""
            ---
            
            ### 💡 Example Topics
            
            - "indigenous tribal healthcare"
            - "education technology STEM"
            - "climate renewable energy"
            - "arts culture community"
            - "small business innovation"
            - "nonprofit capacity building"
            """)
        
        with gr.Column(scale=2):
            output = gr.Markdown(
                label="Generated Search Queries",
                value="👈 Enter your topic and click the button to generate grant search queries."
            )
    
    # Examples
    gr.Markdown("### 🚀 Quick Examples - Click to Try")
    gr.Examples(
        examples=[
            ["indigenous tribal native american grants", "Michigan, Minnesota"],
            ["education technology STEM youth", "California"],
            ["climate change sustainability renewable energy", ""],
            ["small business innovation technology", "New York"],
            ["arts culture creative community", "Pacific Northwest"],
            ["healthcare mental health wellness", "Texas"],
        ],
        inputs=[topic_input, location_input],
        label="Try these examples"
    )
    
    # Footer
    gr.Markdown("""
    ---
    
    ## 🚀 About MAI Advisor MCP
    
    This tool is part of the **MAI Advisor MCP** (Model Context Protocol) server - an AI-powered grant finder
    built for MCP's 1st Birthday Hackathon (Nov 14-30, 2025).
    
    ### What Makes This Special?
    
    - ✨ **Expert Analysis**: Automatic keyword expansion and optimization
    - 🔍 **Comprehensive Dorks**: Extensive intext/inurl variations covering all grant terminology
    - 🌐 **Multi-Engine**: Optimized queries for Google, Bing, and DuckDuckGo
    - 💾 **Auto-Save**: All queries saved to JSON files for easy sharing
    - 🎯 **Production-Ready**: Based on real non-profit grant search patterns
    
    ### Links
    
    - **[GitHub Repository](https://github.com/nbiish/mai-advisor-mcp)**
    - **[MCP Integration Guide](https://github.com/nbiish/mai-advisor-mcp/blob/main/mai-advisor-mcp/README.md)**
    
    ### MCP Server
    
    This interface is also available as an MCP tool that integrates directly with Claude Desktop and other MCP clients.
    
    **Single Tool Interface:**
    - `find_grants(topic, location)` - That's it!
    - Automatic dork generation
    - Saves to configured output folder
    - Perfect for AI assistants
    
    ---
    
    **Built with:** Python, Gradio, MCP Protocol, and expert grant-finding knowledge
    
    *Dorks are saved to: `{OUTPUT_DIR}`*
    """.format(OUTPUT_DIR=OUTPUT_DIR))
    
    # Connect button
    search_btn.click(
        fn=find_grants,
        inputs=[topic_input, location_input],
        outputs=output
    )


# Launch
if __name__ == "__main__":
    demo.launch()
