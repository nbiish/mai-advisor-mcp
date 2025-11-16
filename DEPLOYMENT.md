# 🚀 Deployment Guide - Hugging Face Space

## ✅ Git Repository Setup Complete

Your MAI Advisor MCP project is now set up with Git and connected to both GitHub and Hugging Face:

### Remotes Configured
- **GitHub** (origin): https://github.com/nbiish/mai-advisor-mcp.git
- **Hugging Face** (hf): https://huggingface.co/spaces/nbiish/mai-advisor-mcp

### Latest Commit
All files have been committed and pushed to GitHub, including:
- Main MCP server code (src/)
- Gradio demo app (app.py)
- Documentation (README, QUICKSTART, etc.)
- Examples and configuration

---

## 📦 Deploying to Hugging Face Space

Since HTTPS authentication requires a token, here are your options:

### Option 1: Use Hugging Face Web Interface (Recommended)

1. **Go to your Space**: https://huggingface.co/spaces/nbiish/mai-advisor-mcp

2. **Click "Files and versions"** tab

3. **Upload files directly** or use the web editor:
   - Upload `app.py`
   - Upload `requirements.txt`  
   - Create/edit README from `README_HF.md` content

4. **Space will auto-deploy** once files are uploaded

### Option 2: Use Git with Token

1. **Get your Hugging Face token**:
   ```bash
   huggingface-cli login
   ```
   Or get it from: https://huggingface.co/settings/tokens

2. **Update the Git remote** to include your token:
   ```bash
   git remote remove hf
   git remote add hf https://YOUR_USERNAME:YOUR_TOKEN@huggingface.co/spaces/nbiish/mai-advisor-mcp
   ```

3. **Push to Hugging Face**:
   ```bash
   cd /Volumes/1tb-sandisk/code-external/mai-advisor-mcp
   git push hf main
   ```

### Option 3: Use Hugging Face CLI

1. **Upload using the CLI**:
   ```bash
   cd /Volumes/1tb-sandisk/code-external/mai-advisor-mcp/grant-finder-mcp
   
   huggingface-cli upload nbiish/mai-advisor-mcp . --repo-type=space
   ```

---

## 📁 Files for Hugging Face Space

The following files are ready for deployment:

### Required Files
- **`app.py`** - Gradio web interface
- **`requirements.txt`** - Python dependencies (gradio, pydantic)
- **`README.md`** - Copy content from `README_HF.md` (includes Space config in frontmatter)

### Supporting Files
- **`src/search_operators.py`** - Search query generation logic
- **`src/__init__.py`** - Package initialization

### Optional (for full functionality)
- `src/grant_agent.py` - AI research agent (requires API keys)
- `src/server.py` - MCP server (for local use, not in Space)

---

## 🎯 Space Configuration

The README_HF.md file contains frontmatter configuration:

```yaml
---
title: MAI Advisor MCP - Grant Finder
emoji: 🎯
colorFrom: blue
colorTo: green
sdk: gradio
sdk_version: 4.44.0
app_file: app.py
pinned: false
license: mit
tags:
  - mcp
  - model-context-protocol
  - grant-finder
  - ai
  - search
  - funding
---
```

**Copy this to the top of your Space's README.md** (you can edit directly on HF)

---

## 🔍 What the Space Does

The Hugging Face Space provides a **web demo** of the grant search query generator:

1. Users enter search criteria (keywords, org type, sector, location, funding)
2. Select search engines (Google, Bing, DuckDuckGo)
3. Click "Generate Search Queries"
4. Get optimized search queries to copy/paste into search engines

**Note**: The Space demo shows only the query generation feature. For full AI-powered research with Claude, users need to run the MCP server locally (see main README.md).

---

## 🚀 Quick Deploy Steps

### Fastest Method (Web UI):

1. Go to https://huggingface.co/spaces/nbiish/mai-advisor-mcp
2. Click "Files and versions"
3. Click "Add file" → "Create a new file"
4. Create these files:

**README.md**:
```
Copy entire content from grant-finder-mcp/README_HF.md
```

**app.py**:
```
Copy content from grant-finder-mcp/app.py
```

**requirements.txt**:
```
gradio>=4.0.0
pydantic>=2.0.0
```

5. Create `src` folder and upload:
   - `src/__init__.py`
   - `src/search_operators.py`

6. Space will automatically build and deploy!

---

## ✅ Verification

Once deployed, your Space should:
- Show the Gradio interface with search criteria form
- Allow users to generate search queries
- Display formatted queries for Google, Bing, DuckDuckGo
- Include example searches
- Have working documentation links

---

## 🔗 Links

- **Space URL**: https://huggingface.co/spaces/nbiish/mai-advisor-mcp
- **GitHub Repo**: https://github.com/nbiish/mai-advisor-mcp
- **Hackathon**: MCP's 1st Birthday (Nov 14-30, 2025)

---

## 💡 Tips

1. **Start simple**: Upload just app.py, requirements.txt, and README first
2. **Test locally**: Run `python grant-finder-mcp/app.py` to test before deploying
3. **Check logs**: HF Spaces shows build logs if there are errors
4. **Update README**: Make sure the frontmatter is at the very top of README.md

---

**Built with ❤️ for MCP's 1st Birthday Hackathon**
