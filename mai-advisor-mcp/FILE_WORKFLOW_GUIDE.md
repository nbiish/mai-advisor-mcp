# File-Based Workflow Guide

## Overview

MAI Advisor uses a structured file-based workflow for both MCP server and Hugging Face Space deployments. All outputs are organized into dedicated directories for easy inspection and orchestration.

## Directory Structure

```
mai-advisor-mcp/
├── advisors_output/          # Individual advisor reports
│   ├── 20251115_120000_financial_topic.json
│   ├── 20251115_120100_grant_topic.json
│   └── 20251115_120200_research_topic.json
├── orchestrator_output/      # Final synthesized plans
│   └── 20251115_120300_plan_topic.json
└── grant_dorks/              # Generated search dorks
    └── 20251115_120400_dorks_topic.json
```

## Workflow Process

### 1. Advisor Analysis Phase

Each advisor (financial, grant, research) analyzes the topic and saves structured output:

```python
from src.output_manager import output_manager, AdvisorOutput

# Financial Advisor generates analysis
output = AdvisorOutput(
    advisor_type="financial",
    timestamp=datetime.now().isoformat(),
    topic="community health initiative",
    analysis={
        "budget_analysis": {...},
        "revenue_streams": [...],
        "cost_breakdown": {...}
    },
    recommendations=[...],
    metadata={...}
)

# Save to advisors_output/
filepath = output_manager.save_advisor_output(output)
```

**Output Location:** `advisors_output/YYYYMMDD_HHMMSS_<advisor_type>_<topic>.json`

### 2. Orchestration Phase

The orchestrator reads all advisor outputs and synthesizes a final plan:

```python
from src.output_manager import output_manager, OrchestratorOutput

# Read all advisor reports for topic
advisor_outputs = output_manager.read_advisor_outputs(topic="community health")

# Synthesize final plan (using Gemini/Perplexity orchestration)
output = OrchestratorOutput(
    timestamp=datetime.now().isoformat(),
    topic="community health initiative",
    executive_summary="...",
    business_plan={...},
    grant_strategy={...},
    financial_projections={...},
    implementation_timeline=[...],
    risk_assessment={...},
    success_metrics=[...],
    source_reports=[list of advisor report filenames]
)

# Save to orchestrator_output/
filepath = output_manager.save_orchestrator_output(output)
```

**Output Location:** `orchestrator_output/YYYYMMDD_HHMMSS_plan_<topic>.json`

### 3. Grant Dork Generation

Search dorks are saved separately:

```python
from src.output_manager import output_manager

# Generate and save dorks
filepath = output_manager.save_dorks(
    topic="indigenous education",
    location="Michigan, Minnesota",
    dorks={
        "google": "...",
        "bing": "...",
        "duckduckgo": "..."
    }
)
```

**Output Location:** `grant_dorks/YYYYMMDD_HHMMSS_dorks_<topic>.json`

## MCP Server Integration

### Using find_grants Tool

```json
{
  "name": "find_grants",
  "arguments": {
    "topic": "indigenous education technology",
    "location": "Michigan, Minnesota"
  }
}
```

**What Happens:**
1. Dorks generated for Google, Bing, DuckDuckGo
2. Saved to `grant_dorks/` directory
3. MCP response includes file path and dork content

### Future: Multi-Advisor Workflow (Coming Soon)

```json
{
  "name": "run_advisor_analysis",
  "arguments": {
    "topic": "community health initiative",
    "advisor_type": "financial"
  }
}
```

```json
{
  "name": "generate_final_plan",
  "arguments": {
    "topic": "community health initiative"
  }
}
```

## Hugging Face Space Interface

### Dual-Window Viewers

The Gradio app provides two dual-window interfaces:

#### Advisor Reports Viewer
- **Left Window:** List of all advisor reports with metadata
- **Right Window:** Content of selected/latest report

#### Final Plans Viewer
- **Left Window:** List of all orchestrator outputs with metadata
- **Right Window:** Content of selected/latest plan

### Using the Interface

1. **Grant Search Tab**
   - Enter topic and location
   - Generate dorks
   - View in single window

2. **Advisor Analyses Tab**
   - Enter topic
   - Select advisor type (financial/grant/research)
   - Run analysis
   - View summary and details in dual windows

3. **Final Plan Tab**
   - Enter topic (must match advisor analyses)
   - Generate final plan
   - View executive summary and detailed plan in dual windows

4. **Advisor Reports Tab**
   - Click "Refresh" to load file list
   - Left window shows all reports
   - Right window shows latest report content

5. **Final Plans Tab**
   - Click "Refresh" to load file list
   - Left window shows all plans
   - Right window shows latest plan content

## Output Manager API

### Save Operations

```python
from src.output_manager import output_manager

# Save advisor output
filepath = output_manager.save_advisor_output(advisor_output)

# Save orchestrator output
filepath = output_manager.save_orchestrator_output(orchestrator_output)

# Save dorks
filepath = output_manager.save_dorks(topic, location, dorks)
```

### Read Operations

```python
# Read advisor outputs for topic
advisor_outputs = output_manager.read_advisor_outputs(topic="health")

# Read latest N advisor outputs
advisor_outputs = output_manager.read_latest_advisor_outputs(limit=10)

# Read orchestrator outputs
orchestrator_outputs = output_manager.read_orchestrator_outputs(limit=10)

# Get all outputs for a session/topic
session_data = output_manager.get_session_outputs(topic="health")
```

### List Operations

```python
# List advisor files with metadata
advisor_files = output_manager.list_advisor_files()
# Returns: [{"path": "...", "filename": "...", "size_kb": ..., "modified": "..."}]

# List orchestrator files with metadata
plan_files = output_manager.list_orchestrator_files()
```

## File Format

### Advisor Output Format

```json
{
  "advisor_type": "financial",
  "timestamp": "2025-11-15T12:00:00",
  "topic": "community health initiative",
  "analysis": {
    "budget_analysis": {...},
    "revenue_streams": [...],
    "cost_breakdown": {...}
  },
  "recommendations": [
    "Recommendation 1",
    "Recommendation 2"
  ],
  "metadata": {
    "version": "1.0",
    "model": "gemini-2.0-flash-exp"
  }
}
```

### Orchestrator Output Format

```json
{
  "timestamp": "2025-11-15T12:03:00",
  "topic": "community health initiative",
  "executive_summary": "...",
  "business_plan": {...},
  "grant_strategy": {...},
  "financial_projections": {...},
  "implementation_timeline": [...],
  "risk_assessment": {...},
  "success_metrics": [...],
  "source_reports": [
    "20251115_120000_financial_topic.json",
    "20251115_120100_grant_topic.json",
    "20251115_120200_research_topic.json"
  ]
}
```

### Dork Output Format

```json
{
  "generated_at": "2025-11-15T12:04:00",
  "topic": "indigenous education",
  "location": "Michigan, Minnesota",
  "dorks": {
    "google": "(...extensive dork...)",
    "bing": "(...)",
    "duckduckgo": "(...)"
  }
}
```

## Best Practices

### 1. Topic Consistency
- Use the same topic string across all advisor analyses
- This ensures the orchestrator can find and synthesize all reports

### 2. File Management
- Files are timestamped and never overwritten
- Use `cleanup_old_files()` to remove old files:
  ```python
  removed = output_manager.cleanup_old_files(days=30)
  ```

### 3. Error Handling
- All read operations handle missing/corrupted files gracefully
- Check return values for empty lists

### 4. Inspection
- All files are JSON for easy inspection
- Use any text editor or `jq` command:
  ```bash
  cat advisors_output/latest.json | jq '.'
  ```

## Deployment

### As MCP Server

```bash
# Run server
python src/server_simplified.py

# Configure in Claude Desktop
{
  "mcpServers": {
    "mai-advisor": {
      "command": "python",
      "args": ["/path/to/src/server_simplified.py"]
    }
  }
}
```

### As Hugging Face Space

```bash
# Run Gradio app
python app_enhanced.py

# Or deploy to HF Space
# Upload app_enhanced.py and set as main app file
```

## Future Enhancements

1. **Real-time Collaboration**
   - WebSocket updates when new files added
   - Multi-user session management

2. **Advanced Filtering**
   - Search files by date range
   - Filter by advisor type
   - Full-text search across outputs

3. **Export Options**
   - PDF generation from plans
   - Markdown export
   - Email delivery

4. **Integration with Perplexity/Gemini MCPs**
   - Automatic orchestration using mcp_orchestrate_agents
   - CEO & Board deliberation on plans
   - Financial experts review

## Troubleshooting

### Files Not Appearing in UI
- Click "Refresh" button
- Check file permissions
- Verify directory paths

### Orchestrator Can't Find Advisor Reports
- Ensure topic string matches exactly
- Check advisors_output/ directory exists
- Verify JSON files are valid

### Large File Sizes
- Use cleanup_old_files() regularly
- Consider archiving old sessions
- Implement pagination in viewers

---

**Last Updated:** November 15, 2025  
**Status:** Production Ready for MCP Server & HF Space
