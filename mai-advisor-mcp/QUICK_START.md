# MAI Advisor - Quick Reference Card

## 🚀 Fast Start Commands

### Launch the App

```bash
# Interactive menu (recommended)
./start.sh

# Direct Gradio launch
python app_workflow.py

# Direct MCP server launch
python src/server_mcp.py

# Run tests
python test_mcp_server.py

# Setup Claude Desktop
python setup_claude_config.py
```

---

## 📂 Output Files (Per Run)

| Directory | File Pattern | Purpose |
|-----------|-------------|---------|
| `grant_dorks/` | `TIMESTAMP_TOPIC.json` | Search queries for 3 engines |
| `advisors_output/` | `financial.TIMESTAMP.md` | Budget & fiscal strategy |
| `advisors_output/` | `grant.TIMESTAMP.md` | Proposal & funder strategy |
| `advisors_output/` | `research.TIMESTAMP.md` | Evidence & evaluation strategy |
| `orchestrator_output/` | `grant-plan-and-overview.TIMESTAMP.md` | Comprehensive strategic plan |
| `agent-instructions/` | `agent-todo.TIMESTAMP.md` | AI browser agent tasks (8K words) |

**Total:** 6 files per workflow run

---

## 🎯 MCP Tools (Claude Desktop)

| Tool | Purpose | Required | Optional |
|------|---------|----------|----------|
| `generate_grant_strategy` | Full workflow | `topic` | `location` |
| `generate_search_dorks` | Just search queries | `topic` | `location` |
| `get_latest_agent_todo` | Retrieve agent instructions | — | — |
| `get_latest_orchestrator_plan` | Retrieve strategic plan | — | — |

### Example Claude Prompts

```
"Generate a grant strategy for youth STEM education in Phoenix"

"Create search dorks for environmental conservation grants in Portland"

"Show me the latest AI agent instructions"

"What's in the most recent grant plan?"
```

---

## 🌐 Gradio Interface Tabs

1. **Welcome** - System overview & getting started
2. **Grant Strategy Workflow** - Main interface (inputs + run)
3. **Search Dorks** - View/download search queries
4. **Expert Frameworks** - View 3 advisor outputs
5. **Grant Plan** - View orchestrated strategic plan
6. **AI Agent TODO** - View browser agent instructions

---

## 🔧 Claude Desktop Setup

### macOS

```bash
# Run auto-config
python setup_claude_config.py

# Restart Claude
killall Claude && open -a Claude

# Or manually edit:
# ~/Library/Application Support/Claude/claude_desktop_config.json
```

### Windows

```bash
# Run auto-config
python setup_claude_config.py

# Restart Claude Desktop
# Then manually check:
# %APPDATA%\Claude\claude_desktop_config.json
```

### Linux

```bash
# Run auto-config
python setup_claude_config.py

# Restart Claude
# Check config at:
# ~/.config/Claude/claude_desktop_config.json
```

---

## 📊 Typical Workflow

### For Humans (Manual)

1. Run `./start.sh` → Option 1 (Gradio)
2. Enter grant topic + location
3. Click "Generate Complete Grant Strategy"
4. Wait 30-60 seconds
5. Download files from tabs
6. Use search dorks manually in Google/Bing/DuckDuckGo
7. Read expert frameworks for guidance
8. Follow orchestrator plan

**Time Investment:** 30 min - 2 hours (reading + execution)

### For AI Agents (Automated)

1. Generate strategy (same as above)
2. Provide `agent-todo.TIMESTAMP.md` to AI assistant
3. AI executes 90-day workflow:
   - Week 1-2: Discovers 15-25 grants
   - Week 1-2: Submits 3-5 quick-win applications
   - Week 3-6: Completes 4-6 high-priority applications
   - Week 7-12: Handles medium-priority + follow-ups
4. Human approves all submissions
5. Track outcomes

**Time Investment:** 5-10 hours (oversight + approval)
**AI Time:** 90 days autonomous execution

### Via Claude Desktop (Integrated)

1. Setup MCP server (one-time): `python setup_claude_config.py`
2. Chat with Claude: "Generate grant strategy for [topic]"
3. Claude invokes MAI Advisor tools automatically
4. Review results in Claude chat
5. Files saved locally in output directories
6. Continue conversation with Claude using generated context

**Time Investment:** 5 minutes + conversation time

---

## 🧪 Testing Checklist

### Quick Test (1 minute)

```bash
python test_mcp_server.py
# Skip full strategy test when prompted
```

Verifies:
- ✅ MCP server loads
- ✅ Tools registered (4)
- ✅ Resources registered (3)
- ✅ Dork generation works

### Full Test (5 minutes)

```bash
python test_mcp_server.py
# Approve full strategy test when prompted
```

Verifies everything above PLUS:
- ✅ Complete workflow execution
- ✅ All 6 files created
- ✅ AI models responding
- ✅ File retrieval functions

### Manual Gradio Test

```bash
./start.sh → Option 1
# Enter test data, generate strategy
# Verify all tabs populate
# Download files
```

### Manual Claude Test

```bash
# After setup_claude_config.py
# In Claude Desktop:
# Type: "Use mai-advisor to generate a grant strategy for test project"
# Verify: Tool appears, executes, files created
```

---

## 🐛 Troubleshooting

### "Module not found" errors

```bash
# Ensure venv is activated
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate     # Windows

# Reinstall dependencies
pip install -r requirements.txt
```

### MCP server not appearing in Claude

1. Check config file exists and is valid JSON
2. Verify Python path in config is correct
3. Restart Claude Desktop completely (quit + relaunch)
4. Check Claude logs: `~/Library/Logs/Claude/` (macOS)

### Gradio app won't start

```bash
# Check port 7860 is available
lsof -i :7860  # macOS/Linux
netstat -ano | findstr :7860  # Windows

# Kill existing process or use different port
# Edit app_workflow.py: app.launch(server_port=7861)
```

### Empty or missing output files

1. Check environment variables (`.env` file)
2. Verify API keys are valid
3. Check terminal for error messages
4. Ensure output directories have write permissions

---

## 📞 Getting Help

### Documentation Files

- `README.md` - Main project overview
- `README_DEPLOY.md` - Deployment guide (both modes)
- `README_HF_SPACE.md` - HuggingFace Space submission
- `IMPLEMENTATION_COMPLETE.md` - Technical details
- `AGENTS.md` - Code guidelines

### Example Code

- `examples/` - Working examples of components
- `test_mcp_server.py` - MCP server usage examples
- `app_workflow.py` - Gradio interface reference

### Common Questions

**Q: Can I use this without Claude/Anthropic API?**
A: No, the expert advisors require Claude API. You'll need an API key.

**Q: Can I customize the expert advisors?**
A: Yes! Edit `src/grant_agent.py` and modify the system prompts.

**Q: Can I add more search engines?**
A: Yes! Edit `src/dork_generator.py` and add new engine methods.

**Q: How much does it cost to run?**
A: ~$0.50-$2.00 per complete strategy (Claude API tokens).

**Q: Can I deploy to Heroku/AWS/etc?**
A: Yes! It's just Python + Gradio. Works anywhere Python runs.

---

## 🎯 Project Links

- **GitHub:** [YOUR_REPO_URL]
- **HuggingFace Space:** [YOUR_SPACE_URL]
- **Demo Video:** [YOUR_VIDEO_URL]
- **Issues:** [YOUR_ISSUES_URL]

---

## 📋 File Size Reference

| Output Type | Typical Size | Read Time |
|-------------|--------------|-----------|
| Search Dorks | 1-2 KB | 1 min |
| Financial Framework | 5-8 KB | 10 min |
| Grant Framework | 5-8 KB | 10 min |
| Research Framework | 5-8 KB | 10 min |
| Orchestrator Plan | 10-15 KB | 20 min |
| AI Agent TODO | 30-40 KB | 60 min |

**Total per run:** ~60-85 KB across 6 files

---

## ⚡ Performance Benchmarks

| Operation | Time | Notes |
|-----------|------|-------|
| Dork generation only | ~2s | No AI calls |
| Single expert framework | ~8-12s | 1 Claude API call |
| Complete strategy | ~30-60s | 5 Claude API calls |
| MCP tool invocation | +5-10s | Overhead from Claude Desktop |
| File retrieval | <1s | Local disk read |

---

## 🔒 Security Notes

### API Keys

```bash
# Never commit .env file
# Store in .env (gitignored):
ANTHROPIC_API_KEY=your_key_here

# Or use environment variables:
export ANTHROPIC_API_KEY=your_key_here
```

### Sensitive Data

- ❌ Don't include EIN in prompts (AI might log)
- ❌ Don't include bank details in prompts
- ✅ Do include: mission, programs, impact metrics
- ✅ Do review all AI-generated content

### AI Agent Execution

- ⚠️ Always approve before agent submits applications
- ⚠️ Review all AI-generated narratives
- ⚠️ Verify facts and figures manually
- ⚠️ Use trusted AI services only

---

**Updated:** January 2025
**Version:** 1.0.0
**License:** MIT
