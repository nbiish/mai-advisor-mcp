# Hugging Face Space Upload Plan

This checklist keeps the MCP hackathon submission tidy and ensures we only ship the assets required for the public Space at [https://huggingface.co/spaces/nbiish/mai-advisor-mcp](https://huggingface.co/spaces/nbiish/mai-advisor-mcp).

## 1. Prepare a Clean Payload

1. Work from `huggingface_space_deploy/` (already trimmed for Spaces).
2. Keep **only** the following items when syncing to Hugging Face:
   - `README.md`
   - `app_workflow.py`
   - `requirements.txt`
   - `.env.example`
   - `LICENSE`
   - `src/` (all helper modules used by the Gradio app)
3. Explicitly **exclude** generated artifacts and local tooling directories:
   - `advisors_output/`
   - `agent-instructions/`
   - `grant_dorks/`
   - `orchestrator_output/`
   - `advisors_output.zip` or any other exports (e.g., `mai_advisor_export_*.zip`)
   - `.venv/`, `.configs/`, `examples/`, and any crash-course markdowns used for testing
4. Confirm `.gitignore` already blocks `.env`, `.venv`, logs, and agent workspaces so no secrets leak during packaging.

## 2. Update Metadata Before Upload

1. Edit `huggingface_space_deploy/README.md`:
   - Fill in the **demo video link** and **social post link** placeholders.
   - Double-check the `tags` list contains both hackathon tracks.
   - Mention the transcript path (`docs/hackathon/TRANSCRIPT_PRACTICE.md`) in the narrative so judges can follow along.
2. Verify `requirements.txt` pins to Gradio `5.49.1` to match the front matter (`sdk_version`).
3. Run `python -m pip install -r requirements.txt` locally to ensure the list is valid before uploading.

## 3. Push to Hugging Face

Option A – **Git workflow** (recommended for repeat updates):

```bash
cd huggingface_space_deploy
huggingface-cli login  # if not already authenticated
huggingface-cli repo clone nbiish/mai-advisor-mcp --type space --space-sdk gradio
rsync -av --delete README.md app_workflow.py requirements.txt .env.example LICENSE src/ ../mai-advisor-mcp/
cd ../mai-advisor-mcp
git status  # verify only desired files changed
git commit -am "Deploy clean MAI Advisor payload"
git push
```

Option B – **Web upload** (one-off):

1. Zip only the allowed files: `zip -r mai-advisor-space.zip README.md app_workflow.py requirements.txt .env.example LICENSE src`.
2. Drag the archive into the Hugging Face Space Files tab.
3. Delete any pre-existing generated content from the Space if it slipped in earlier.

## 4. Configure Secrets & Build Settings

1. In the Space **Settings → Variables**, add the required API keys:
   - `OPENROUTER_API_KEY`
   - `ANTHROPIC_API_KEY` (optional if using Claude calls)
   - `TAVILY_API_KEY` (optional for research helper)
2. Confirm the front matter specifies `sdk: gradio`, `sdk_version: 5.49.1`, and `app_file: app_workflow.py`.
3. Trigger a rebuild by clicking **Restart this Space** once secrets are saved.

## 5. Validate the Deployment

1. Open the public Space URL in an incognito window.
2. Run one full workflow (topic + location) and ensure all six tabs render content plus downloadable files.
3. Spot-check Space logs for missing dependency errors.
4. Capture screenshots or screen recording snippets for the demo video and social posts.
5. If everything looks good, lock in the Space link for the submission form and README.
