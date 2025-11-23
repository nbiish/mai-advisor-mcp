# 🏆 MCP 1st Birthday Hackathon: Best-To-Do Strategy

This document is an extensive review of the steps required to win the **MCP 1st Birthday Hackathon** (Tracks: *MCP in Action* & *Building MCP*).

## 🚨 Critical Action Items

### 1. Hugging Face Space Configuration

* **Secrets Management:** Ensure your Space has the following secrets set in the Settings tab:
  * `TAVILY_API_KEY` (Required for the Agent)
  * `OPENROUTER_API_KEY` (Required for the LLM)
* **Dependencies:** Verify `requirements.txt` includes `mcp`, `tavily-python`, `langchain-openai`.
* **App File:** Ensure `app_workflow.py` is the entry point.

### 2. "Real" vs. "Simulated" Mode

* **Current State:** `app_workflow.py` uses `simulate_expert_plan` for the text generation to ensure speed/reliability during the demo.
* **Recommendation:** For the video, this is fine. However, for the **MCP Server** demo (Section 4 of transcript), ensure you are showing **real tool calls** in Claude Desktop. The judges will want to see the actual `generate_dorks` tool working, not just a static response.

### 3. Submission Metadata (The "Tags")

* **File:** `README.md` (YAML Frontmatter)
* **Required Tags:**
  * `mcp-in-action-track-enterprise`
  * `building-mcp-track-enterprise`
* **Why:** If these tags are missing or typoed, your submission will not be indexed by the judges.

### 4. The "Mukwa Miikana" Integration

* **Authenticity:** Use the real data for Mukwa Miikana in your demo.
  * **Topic:** "Indigenous Environmental Sovereignty" or "Protecting the Great Lakes"
  * **Location:** "Bemidji, MN" or "Upper Peninsula, MI"
* **Impact:** This specific use case (helping a grassroots Indigenous org) is a strong narrative for the "Enterprise/Social Impact" angle.

---

## 🎬 Video Recording Strategy (Checklist)

**Goal:** A single 5-10 minute video that covers BOTH tracks.

* [ ] **0:00 - 1:00: The Hook (Face Camera)**
  * "We are solving the capacity gap for non-profits like Mukwa Miikana."
* [ ] **1:00 - 4:00: The Gradio App (Screen Share)**
  * Show the inputs.
  * Show the *speed* of generation (even if simulated, emphasize the *structure*).
  * Open the "Agent Instructions" file and scroll through it to show the depth (8,000 words).
* [ ] **4:00 - 6:00: The MCP Server (Claude Desktop)**
  * **CRITICAL:** This is the "Building MCP" track evidence.
  * Show the "mcp" icon in Claude.
  * Run the prompt: *"Find grant dorks for Indigenous youth programs."*
  * **Pause** to let the viewer see the "Using tool..." animation.
* [ ] **6:00 - 8:00: The "Agent" (Terminal/Code)**
  * Show the `grant_agent.py` code briefly to prove it's real.
  * If possible, run a small script in the terminal that uses the agent to find *one* live result.

---

## 📝 Final Polish

1. **Linting:** Run `yamllint` on your `README.md` to ensure the frontmatter is valid.
2. **Links:** Ensure the "Demo Video" link in `README.md` is clickable and public.
3. **Socials:** Post the Twitter/LinkedIn content *before* the deadline and link it in the README.
