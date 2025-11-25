# 🎂 MCP 1st Birthday Hackathon - Complete Submission Guide

**Hackathon:** MCP's 1st Birthday - Hosted by Anthropic and Gradio  
**Dates:** November 14-30, 2025  
**Deadline:** November 30, 2025, 11:59 PM UTC  
**Total Registrations:** 6,500+  
**Prize Pool:** $21,000 USD + $4.2M in API Credits  

---

## 📋 TABLE OF CONTENTS

1. [Hackathon Overview](#-hackathon-overview)
2. [Track Requirements](#-track-requirements)
3. [Required Tags](#-required-tags-critical)
4. [Submission Checklist](#-submission-checklist)
5. [README.md Template](#-readmemd-template)
6. [Demo Video Script](#-demo-video-script---hugging-face-space)
7. [BoltAI/Raycast MCP Demo Script](#-boltairaycast-mcp-demo-script)
8. [Social Media Templates](#-social-media-templates)
9. [Judging Criteria](#-judging-criteria)
10. [Timeline](#-timeline)
11. [Resources](#-resources)

---

## 🎯 HACKATHON OVERVIEW

### Two Main Tracks

| Track | Description | Prize Pool |
|-------|-------------|------------|
| **🔧 Track 1: Building MCP** | Build MCP servers that extend LLM capabilities | $1,500 + Claude API credits |
| **🤖 Track 2: MCP in Action** | Create AI agent Gradio apps using MCP tools | $4,000 per category |

### Three Categories Per Track

| Category | Track 1 Tag | Track 2 Tag |
|----------|-------------|-------------|
| **Enterprise** | `building-mcp-track-enterprise` | `mcp-in-action-track-enterprise` |
| **Consumer** | `building-mcp-track-consumer` | `mcp-in-action-track-consumer` |
| **Creative** | `building-mcp-track-creative` | `mcp-in-action-track-creative` |

### Additional Tags (Optional but Recommended)

| Tag | Purpose |
|-----|---------|
| `mcp-server` | Marks your Space as an MCP server (discoverable at hf.co/spaces?filter=mcp-server) |
| `gradio` | Standard Gradio app tag |
| `agents` | AI agent functionality |

---

## 🏷️ REQUIRED TAGS (CRITICAL)

### For MAI Advisor Submission (Both Tracks, Enterprise Category)

```yaml
tags:
  - mcp-in-action-track-enterprise
  - building-mcp-track-enterprise
  - mcp-server
```

### Tag Format Rules

✅ **CORRECT:**
```yaml
tags:
  - mcp-in-action-track-enterprise
  - building-mcp-track-enterprise
```

❌ **WRONG:**
```yaml
tags:
  - "mcp-in-action-track-enterprise"  # No quotes needed
  - MCP-IN-ACTION-TRACK-ENTERPRISE    # Must be lowercase
  - mcp_in_action_track_enterprise    # Must use hyphens, not underscores
```

---

## ✅ SUBMISSION CHECKLIST

### Phase 1: Pre-Submission (Complete Before Recording)

#### Organization Membership
- [ ] Requested to join MCP-1st-Birthday organization on HuggingFace
- [ ] Membership approved
- [ ] Can create Spaces in the organization

#### Code Preparation
- [ ] All code working locally
- [ ] Gradio app runs without errors
- [ ] MCP server tested with Claude Desktop / BoltAI / Raycast
- [ ] All dependencies in `requirements.txt`
- [ ] No hardcoded API keys (use environment variables)
- [ ] `.env.example` file created (NOT actual `.env`)

#### HuggingFace Space Setup
- [ ] Space created in MCP-1st-Birthday organization
- [ ] Space name: `mai-advisor-mcp` or similar
- [ ] Visibility: Public
- [ ] SDK: Gradio
- [ ] SDK Version: 5.49.1

### Phase 2: README.md Requirements

#### Frontmatter (YAML Header) - REQUIRED
```yaml
---
title: MAI Advisor - AI Grant Planning System
emoji: 🎯
colorFrom: blue
colorTo: green
sdk: gradio
sdk_version: 5.49.1
app_file: app_workflow.py
pinned: false
license: mit
short_description: Complete grant planning system with AI browser agent integration and native MCP server.
tags:
  - mcp-in-action-track-enterprise
  - building-mcp-track-enterprise
  - mcp-server
---
```

#### Required Sections
- [ ] **Demo Video Link** - YouTube/Loom/Vimeo (5-10 minutes)
- [ ] **Social Media Post Link** - Twitter/X or LinkedIn
- [ ] **Team Members** - HuggingFace usernames
- [ ] **Problem Statement** - What problem does it solve?
- [ ] **Solution Overview** - How does it work?
- [ ] **Architecture Diagram** - Visual system design
- [ ] **Key Features** - Bullet points
- [ ] **How to Use** - Step-by-step instructions
- [ ] **Technical Details** - Stack, implementation
- [ ] **Impact Metrics** - Measurable outcomes
- [ ] **Hackathon Compliance** - Track requirements met
- [ ] **License** - MIT or similar

### Phase 3: Demo Video Requirements

#### Content Checklist (5-10 minutes)
- [ ] **Introduction** (0:00-1:00) - What is MAI Advisor?
- [ ] **Gradio Demo** (1:00-4:00) - Web interface walkthrough
- [ ] **MCP Server Demo** (4:00-7:00) - Claude Desktop/BoltAI/Raycast
- [ ] **AI Agent Workflow** (7:00-9:00) - Autonomous execution plan
- [ ] **Impact & Wrap-up** (9:00-10:00) - Metrics and call-to-action

#### Technical Requirements
- [ ] 1080p resolution minimum
- [ ] Clear audio (use good microphone)
- [ ] Screen recording software (OBS, Loom, QuickTime)
- [ ] Captions/subtitles (recommended)

### Phase 4: Social Media Post

#### Required Elements
- [ ] Project description
- [ ] Demo video link
- [ ] HuggingFace Space link
- [ ] Hackathon hashtags: #MCPHackathon #Gradio #AI #Agents #MCP
- [ ] Tag @huggingface @AnthropicAI

### Phase 5: Final Verification

- [ ] Space loads without errors
- [ ] All tabs functional
- [ ] File downloads work
- [ ] Demo video accessible (unlisted or public)
- [ ] Social media post published
- [ ] All links in README verified
- [ ] Tags correct in Space README
- [ ] No placeholder text remaining

---

## 📝 README.md TEMPLATE

```markdown
---
title: MAI Advisor - AI Grant Planning System
emoji: 🎯
colorFrom: blue
colorTo: green
sdk: gradio
sdk_version: 5.49.1
app_file: app_workflow.py
pinned: false
license: mit
short_description: Complete grant planning system with AI browser agent integration and native MCP server.
tags:
  - mcp-in-action-track-enterprise
  - building-mcp-track-enterprise
  - mcp-server
---

# 🎯 MAI Advisor - Multi-Agent Intelligence Grant Planning System

**🏆 MCP 1st Birthday Hackathon Submission**
- **Tracks:** MCP in Action (Enterprise) + Building MCP (Enterprise)
- **Team:** nbiish
- **Demo Video:** [🎥 WATCH HERE](YOUR_VIDEO_LINK)
- **Social Post:** [📱 VIEW POST](YOUR_SOCIAL_LINK)

---

## 📹 Demo Video

[![Demo Video](VIDEO_THUMBNAIL_URL)](YOUR_VIDEO_LINK)

**Video Highlights:**
- ✅ Gradio web interface (0:00-4:00)
- ✅ MCP server with BoltAI/Raycast (4:00-7:00)
- ✅ AI agent workflow (7:00-9:00)
- ✅ Real-world impact (9:00-10:00)

---

## 🚀 What This System Does

[Your detailed description here]

---

## 🏗️ Architecture

[Your architecture diagram here]

---

## ✨ Key Features

[Your features list here]

---

## 📊 Impact Metrics

| Metric | Before | After | Improvement |
|--------|--------|-------|-------------|
| Applications/year | 2-3 | 10-15 | 400% increase |
| Time to strategy | Weeks | 30 seconds | 99.9% faster |

---

## 🔧 How to Use

### Option 1: Web Interface
[Instructions]

### Option 2: MCP Server (BoltAI/Raycast)
[Instructions]

---

## 📊 Hackathon Compliance

✅ Published in MCP-1st-Birthday organization
✅ Correct track tags in README
✅ Demo video included
✅ Social media post published
✅ Original work created during hackathon period

---

## 📜 License

MIT License - see [LICENSE](LICENSE)

---

**Built with ❤️ for the MCP 1st Birthday Hackathon**
```

---

## 🎬 DEMO VIDEO SCRIPT - HUGGING FACE SPACE

### Scene 1: Introduction (0:00 - 1:00)

**[VISUAL: Title card with MAI Advisor logo]**

> "Hey everyone! I'm Nbiish, and welcome to my submission for the MCP 1st Birthday Hackathon.
>
> I built MAI Advisor - a Multi-Agent Intelligence system that transforms how small nonprofits approach grant seeking.
>
> Here's the problem: Small organizations do incredible work, but they typically only submit 2 to 3 grant applications per year. They don't have dedicated grant writers, and each proposal takes months to complete.
>
> MAI Advisor changes that completely. It generates a comprehensive grant strategy in under 60 seconds - giving nonprofits the foundation for 10 to 15 applications in just 90 days.
>
> Let me show you how it works."

---

### Scene 2: Gradio Web Interface Demo (1:00 - 4:00)

**[VISUAL: Open HuggingFace Space in browser]**

> "This is the MAI Advisor interface running on Hugging Face Spaces. It's designed to be incredibly simple because we know nonprofit leaders are busy.
>
> Let me walk you through a real example. I'll enter a grant topic - let's say 'Indigenous wellness and traditional medicine programs' - and a location, 'Michigan'.
>
> **[TYPE: Topic and location]**
>
> Now I click 'Generate Complete Grant Strategy'.
>
> **[CLICK: Generate button]**
>
> Behind the scenes, the system is orchestrating three AI expert advisors:
> - A Financial Expert for budget and sustainability planning
> - A Grant Writing Expert for proposal frameworks
> - A Research Expert for evidence-based design
>
> **[WAIT: Show loading/progress]**
>
> And in about 30 seconds... we have six comprehensive outputs.
>
> **[NAVIGATE: Through each tab]**
>
> First, the Search Dorks tab - these are optimized search queries for Google, Bing, and DuckDuckGo. Instead of guessing what to search, you get exact strings to find hidden opportunities.
>
> Next, the Expert Frameworks - here's the Financial Strategy with budget planning and sustainability recommendations. The Grant Writing Framework gives us core narratives and impact metrics. And the Research Plan ensures our program is evidence-based.
>
> Then we have the Orchestrated Grant Plan - this synthesizes everything into a comprehensive 90-day roadmap.
>
> And finally, the AI Agent TODO - this is an 8,000-plus word execution plan designed for autonomous AI assistants with browser capabilities.
>
> **[CLICK: Download buttons]**
>
> You can download any of these files directly. Let me grab the agent instructions..."

---

### Scene 3: MCP Server Integration (4:00 - 7:00)

**[VISUAL: Switch to BoltAI or Raycast]**

> "Now here's where it gets really exciting for the Building MCP track.
>
> MAI Advisor isn't just a web app - it's a fully compliant Model Context Protocol server. This means you can integrate it directly into your AI workflow.
>
> **[SHOW: MCP configuration]**
>
> I have MAI Advisor configured as an MCP server in BoltAI [or Raycast]. Let me show you the configuration - it's just pointing to our server script with the required environment variables.
>
> **[OPEN: BoltAI/Raycast]**
>
> Now I can ask: 'Generate a grant strategy for community health programs in Seattle using MAI Advisor.'
>
> **[TYPE: The prompt]**
>
> Watch what happens - the AI recognizes the MAI Advisor tools and calls them directly:
>
> **[SHOW: Tool invocation]**
>
> - `generate_grant_strategy` - runs the full workflow
> - `generate_search_dorks` - creates optimized search queries
> - `get_latest_agent_todo` - retrieves the AI agent instructions
> - `get_latest_orchestrator_plan` - gets the strategic plan
>
> **[SHOW: Results]**
>
> The results come back structured and ready to use. I can now have a conversation about the strategy, ask follow-up questions, or refine specific sections.
>
> This brings specialized grant planning knowledge directly into your daily AI workflow - whether you're using Claude Desktop, BoltAI, Raycast, or any other MCP-compatible client."

---

### Scene 4: AI Agent Workflow (7:00 - 9:00)

**[VISUAL: Open agent-todo.md file]**

> "For the MCP in Action track, we've taken it even further with autonomous agent instructions.
>
> **[SCROLL: Through the document]**
>
> This 8,000-word document is designed for AI assistants with browser capabilities - like Claude with computer use, or custom LangChain agents.
>
> It breaks down a complete 90-day execution plan into four phases:
>
> **Phase 1: Discovery** - The agent searches for opportunities, validates eligibility, and builds a prioritized list.
>
> **Phase 2: Quick Wins** - Submit 3 to 5 applications with short deadlines and high alignment.
>
> **Phase 3: High Priority** - 4 to 6 larger applications with significant funding potential.
>
> **Phase 4: Medium Priority** - Remaining opportunities plus relationship cultivation.
>
> **[HIGHLIGHT: Approval checkpoints]**
>
> Notice these human approval checkpoints throughout. The agent does the research and drafting, but a human reviews and approves every submission. This is responsible AI in action.
>
> **[SHOW: Expected outcomes]**
>
> The expected result? 10 to 15 grant applications submitted in 90 days - compared to the typical 2 to 3 per year."

---

### Scene 5: Impact & Wrap-up (9:00 - 10:00)

**[VISUAL: Impact metrics screen]**

> "Let's talk impact. The numbers speak for themselves:
>
> - **400% increase** in grant applications
> - **99.9% time reduction** for initial strategy
> - **$200K to $500K** in potential funding unlocked per organization
>
> **[SHOW: Innovation highlights]**
>
> This is the first grant planning MCP server. It features a unique three-expert architecture, demonstrates responsible autonomous agent design, and shows how AI can create real social impact.
>
> **[SHOW: Links and CTAs]**
>
> You can try MAI Advisor right now:
> - Visit the HuggingFace Space for the web interface
> - Clone the repo to run locally
> - Configure it as an MCP server in your favorite AI client
>
> All links are in the description below.
>
> Thanks for watching, and let's help nonprofits secure the funding they need to change the world.
>
> **[FADE: To logo and links]**"

---

## 🔌 BOLTAI/RAYCAST MCP DEMO SCRIPT

### Setup Demonstration (For Video)

> "Let me show you how to set up MAI Advisor as an MCP server in [BoltAI/Raycast].
>
> **[SHOW: Configuration file or settings]**
>
> First, we need to configure the MCP server. Here's the configuration:
>
> ```json
> {
>   "mcpServers": {
>     "mai-advisor": {
>       "command": "python",
>       "args": ["/path/to/src/server_mcp.py"],
>       "env": {
>         "OPENROUTER_API_KEY": "your-key-here",
>         "MAI_ADVISOR_OUTPUT_DIR": "/path/to/output"
>       }
>     }
>   }
> }
> ```
>
> **[SAVE: Configuration]**
>
> After saving, restart [BoltAI/Raycast] to load the new server.
>
> **[RESTART: Application]**
>
> Now let's verify it's connected. I'll ask: 'What MAI Advisor tools are available?'
>
> **[SHOW: Tool list]**
>
> Perfect - we can see all four tools:
> 1. `generate_grant_strategy` - Full workflow
> 2. `generate_search_dorks` - Search queries only
> 3. `get_latest_agent_todo` - AI agent instructions
> 4. `get_latest_orchestrator_plan` - Strategic plan
>
> And three resources:
> 1. `mai://guide/getting-started`
> 2. `mai://guide/ai-agent-integration`
> 3. `mai://guide/expert-frameworks`
>
> Now let's run a real query..."

### Live Demo Prompts

**Prompt 1: Full Strategy Generation**
> "Generate a complete grant strategy for youth STEM education programs in Phoenix, Arizona"

**Prompt 2: Search Dorks Only**
> "Create search dorks for finding environmental justice grants in California"

**Prompt 3: Retrieve Latest Plan**
> "Show me the most recent grant strategy plan"

**Prompt 4: Get Agent Instructions**
> "Retrieve the AI agent execution instructions from the last strategy"

---

## 📱 SOCIAL MEDIA TEMPLATES

### Twitter/X Post

```
🎯 Just launched MAI Advisor for #MCPHackathon!

AI-powered grant planning that helps nonprofits go from 2-3 apps/year to 10-15 in 90 days 🚀

✨ 3 AI expert advisors
🔧 Native MCP server for BoltAI/Raycast
🤖 8,000+ word autonomous agent workflow
📊 Real measurable impact

🎥 Demo: [VIDEO_LINK]
🌐 Try it: [HF_SPACE_LINK]

Built with @Gradio @AnthropicAI MCP

#AI #Agents #Nonprofit #MCP #Gradio6

@huggingface
```

### LinkedIn Post

```
🎯 Excited to share my MCP 1st Birthday Hackathon submission!

I built MAI Advisor - a comprehensive AI-powered grant planning system that transforms how nonprofits secure funding.

THE PROBLEM:
Small nonprofits struggle with grant seeking:
• Limited capacity (no dedicated grant writers)
• 2-3 applications per year (vs. needed 10-15)
• Months per proposal
• $100K-$200K funding gap annually

THE SOLUTION:
MAI Advisor generates complete grant strategies in 30-60 seconds:
✅ Optimized search queries for grant discovery
✅ 3 AI expert advisors (Financial, Grant Writing, Research)
✅ Comprehensive strategic roadmap
✅ 8,000+ word AI agent execution plan

THE INNOVATION:
• First grant planning MCP server
• Dual deployment (Web + MCP for BoltAI/Raycast)
• Three-expert architecture
• Autonomous browser agent workflow
• Real measurable impact

REAL IMPACT:
📈 10-15 applications in 90 days (vs. 2-3)
⚡ 30 seconds to strategy (vs. months)
💰 $200K-$500K potential funding unlocked

🎥 Watch demo: [VIDEO_LINK]
🌐 Try it live: [HF_SPACE_LINK]

#AI #MachineLearning #Nonprofit #GrantWriting #MCP #Gradio #Agents #SocialImpact
```

---

## 🏆 JUDGING CRITERIA

Projects will be evaluated on:

| Criteria | Weight | What Judges Look For |
|----------|--------|---------------------|
| **Completeness** | High | HF Space + Social post + Documentation + Demo video |
| **Design/UI-UX** | High | Polished, intuitive, easy-to-use interface |
| **Functionality** | High | Uses Gradio 6, MCP tools, agentic features |
| **Creativity** | Medium | Novel approach, unique architecture |
| **Documentation** | Medium | Clear README, video walkthrough |
| **Real-world Impact** | Medium | Measurable outcomes, practical use case |

### Community Choice Award Based On:
- Likes on HuggingFace Space
- Social media engagement
- Community feedback

---

## 📅 TIMELINE

### Hackathon Period
| Date | Event |
|------|-------|
| Nov 14, 2025 | Hackathon opens |
| Nov 25, 2025 | **TODAY** - 5 days remaining |
| Nov 30, 2025 | Submissions close (11:59 PM UTC) |

### Post-Hackathon
| Date | Event |
|------|-------|
| Dec 1-14, 2025 | Judging period |
| Dec 15, 2025 | Winners announced |

---

## 📚 RESOURCES

### Official Links
- **Hackathon Page:** https://huggingface.co/MCP-1st-Birthday
- **Registration:** https://huggingface.co/spaces/MCP-1st-Birthday/gradio-hackathon-registration-winter25
- **Discord:** https://discord.gg/fveShqytyh (Channel: `agents-mcp-hackathon-winter25🏆`)

### Documentation
- **MCP Specification:** https://modelcontextprotocol.io
- **Gradio MCP Guide:** https://www.gradio.app/guides/building-mcp-server-with-gradio
- **HuggingFace Spaces:** https://huggingface.co/docs/hub/spaces

### Sample Submissions
- **Multi-track example:** https://huggingface.co/spaces/ysharma/sample1-hackathon-space-submission
- **Enterprise example:** https://huggingface.co/spaces/ysharma/sample2-hackathon-space-submission

---

## 🎯 QUICK REFERENCE: WHAT TO DO TODAY

### Immediate Actions
1. [ ] Verify README.md has correct tags
2. [ ] Record demo video (10 min max)
3. [ ] Upload video to YouTube/Loom
4. [ ] Publish social media post
5. [ ] Update README with video and social links
6. [ ] Push to HuggingFace Space
7. [ ] Test Space end-to-end
8. [ ] Verify in MCP-1st-Birthday organization

### Final Checks
- [ ] Space URL works: `https://huggingface.co/spaces/MCP-1st-Birthday/mai-advisor-mcp`
- [ ] Demo video plays
- [ ] Social post is public
- [ ] All tabs functional
- [ ] Downloads work
- [ ] No error messages

---

**⏰ DEADLINE: November 30, 2025, 11:59 PM UTC**

**You've got this! 🚀**

