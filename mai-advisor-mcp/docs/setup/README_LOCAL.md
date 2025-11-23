# Local Development Setup

## Quick Start (with Virtual Environment)

```bash
# 1. Setup virtual environment and install dependencies
./setup_venv.sh

# 2. Activate virtual environment
source venv/bin/activate

# 3. Run the workflow demo
python run_workflow_demo.py

# 4. Or start the Gradio web interface
python app.py
```

## Manual Setup

### Prerequisites
- Python 3.10 or higher
- pip

### Step-by-Step

1. **Create virtual environment**
   ```bash
   python3 -m venv venv
   ```

2. **Activate virtual environment**
   ```bash
   # On macOS/Linux
   source venv/bin/activate
   
   # On Windows
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Test the workflow**
   ```bash
   python run_workflow_demo.py
   ```

## Project Structure

```
mai-advisor-mcp/
├── venv/                    # Virtual environment (excluded from git)
├── src/                     # Source code
│   ├── advisor_tools.py     # Expert advisor & workflow
│   ├── search_operators.py  # Search query generators
│   ├── grant_agent.py       # AI research agent (optional)
│   └── server.py            # MCP server
├── app.py                   # Gradio web interface
├── run_workflow_demo.py     # Workflow test script
├── requirements.txt         # Python dependencies
├── setup_venv.sh           # Setup script
└── README_LOCAL.md          # This file
```

## Development Workflow

### Activate Virtual Environment
Always activate before working:
```bash
source venv/bin/activate
```

### Deactivate Virtual Environment
When done:
```bash
deactivate
```

### Install New Dependencies
```bash
pip install package-name
pip freeze > requirements.txt  # Update requirements
```

### Run Tests
```bash
# Test workflow
python run_workflow_demo.py

# Test Gradio app
python app.py
```

## Hugging Face Space Deployment

The virtual environment is **not** deployed to Hugging Face. HF uses `requirements.txt` to build its own environment.

### Requirements for HF Space
- `requirements.txt` - minimal dependencies
- `app.py` - Gradio interface
- `src/` - source code
- `README_HF.md` - Space configuration

### Deploy to HF
```bash
# Option 1: Using deployment script (requires HF token)
cd ..
./DEPLOY.sh

# Option 2: Manual upload via web interface
# Visit: https://huggingface.co/spaces/nbiish/mai-advisor-mcp
```

## Troubleshooting

### Import Errors
Make sure virtual environment is activated:
```bash
which python
# Should show: .../mai-advisor-mcp/venv/bin/python
```

### Missing Dependencies
Reinstall from requirements:
```bash
pip install -r requirements.txt --force-reinstall
```

### Clean Start
Remove and recreate venv:
```bash
deactivate
rm -rf venv
./setup_venv.sh
```

## Environment Variables (Optional)

For AI research features, create `.env` file:
```bash
ANTHROPIC_API_KEY=your_key_here
TAVILY_API_KEY=your_key_here
```

> **Note:** Basic workflow and search query generation work without API keys.

## What Works Without API Keys
✅ Search query generation (Google, Bing, DuckDuckGo)  
✅ Expert advisor analysis  
✅ Financial guidance  
✅ Research task planning  
✅ Workflow coordination  

## What Requires API Keys
❌ AI-powered deep research (grant_agent.py)  
❌ Automated grant opportunity discovery  
❌ Real-time web search integration  

---

**Built for MCP's 1st Birthday Hackathon** 🎉
