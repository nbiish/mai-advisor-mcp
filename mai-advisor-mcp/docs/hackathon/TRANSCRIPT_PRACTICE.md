# MAI Advisor - Demo Transcript & Practice Script

**Target Audience:** Non-profit stakeholders / Hackathon Judges
**Goal:** Demonstrate how MAI Advisor solves the grant seeking capacity problem.

---

## 1. Introduction (0:00 - 1:00)

**Speaker:**
"Hi everyone. I'm Nbiish, and I'm excited to present **MAI Advisor**, a Multi-Agent Intelligence system designed to democratize grant seeking for small non-profits.

We all know the problem: Small organizations do incredible work but often lack the capacity to chase funding. They don't have dedicated grant writers, and they can't afford to spend months writing proposals that might not get funded.

MAI Advisor changes that. It transforms a process that usually takes weeks into a workflow that takes minutes, generating a complete strategic foundation for 10 to 15 grant applications."

---

## 2. The Gradio Interface & Workflow (1:00 - 2:30)

**(Action: Open the Gradio App in the browser)**

**Speaker:**
"Let's look at the system in action. This is the MAI Advisor interface. It's designed to be incredibly simple because we know non-profit leaders are busy.

I'm going to enter a real-world example. Let's say we are a non-profit working on **[Insert Topic, e.g., 'Indigenous Food Sovereignty']** in **[Insert Location, e.g., 'Northern Ontario']**.

I just type that in here:

* **Topic:** Indigenous Food Sovereignty
* **Location:** Northern Ontario

And I click **'Generate Grant Strategy'**.

Behind the scenes, the system is orchestrating a team of AI experts. It's not just writing text; it's thinking like a Development Director, a Financial Planner, and a Researcher."

---

## 3. Reviewing the Outputs (2:30 - 4:00)

> (Action: Show the generated tabs/files)

**Speaker:**
"In about 30 seconds, we get six comprehensive strategic documents. Let's walk through them.

First, the **Search Dorks**. These are advanced search queries tailored for Google, Bing, and DuckDuckGo. Instead of guessing what to search for, the system gives us the exact strings to find hidden opportunities.

Next, the **Financial Strategy**. This isn't just a budget; it's a sustainability plan. It outlines cost structures, potential funding mixes, and fiscal management practices specific to our topic.

Then we have the **Grant Writing Framework**. This gives us our core narratives, problem statements, and impact metrics. It's 80% of the writing done before we even open a grant application.

And finally, the **Research Plan**. This ensures our program is evidence-based, which funders love."

---

## 4. MCP Server Integration (4:00 - 6:00)

> (Action: Switch to Claude Desktop view)

**Speaker:**
"Now, this is where it gets really exciting for the 'Building MCP' track. MAI Advisor isn't just a web app; it's a fully compliant **Model Context Protocol (MCP) Server**.

Here I am in **Claude Desktop**. I have the MAI Advisor server connected.

I can ask Claude: *'Find grant opportunities for Indigenous programs in Michigan using the MAI Advisor tools.'*

Claude can now directly access the specialized tools we built:

1. `generate_dorks`
2. `get_financial_plan`
3. `get_research_plan`

It calls the tool locally, retrieves the structured strategy, and then uses its own intelligence to refine it. This brings the power of our specialized grant knowledge directly into the user's daily AI workflow."

---

## 5. Autonomous Agent Workflow (6:00 - 8:00)

> (Action: Show the 'Agent Instructions' output or a terminal running the agent)

**Speaker:**
"For the 'MCP in Action' track, we've taken it a step further. We've generated detailed **Autonomous Agent Instructions**.

This is an 8,000-word execution plan designed for an AI Browser Agent. It tells the agent exactly how to:

1. Navigate foundation websites.
2. Verify eligibility criteria.
3. Extract contact information.
4. Draft initial outreach emails.

It turns the 'search' phase into an automated background task, allowing the human to focus on building relationships."



---

## 6. Hugging Face Space Deployment & Clean Packaging (8:00 - 9:00)

**(Action: Show [https://huggingface.co/spaces/nbiish/mai-advisor-mcp](https://huggingface.co/spaces/nbiish/mai-advisor-mcp) in the browser and the `huggingface_space_deploy/` directory in VS Code)**

**Speaker:**
"After validating the workflow, I packaged the entire experience for the hackathon Space. The dedicated `huggingface_space_deploy` folder keeps only what the Space needs to build reliably:

* `README.md` with the required front matter, track tags, demo/social placeholders, and architecture story.
* `app_workflow.py`, which points directly at a trimmed `src/` package.
* `requirements.txt`, `.env.example`, and the MIT `LICENSE`.

I want judges to see only the polished app, so I excluded all generated artifacts—`advisors_output`, `grant_dorks`, `agent-instructions`, `orchestrator_output`, and any timestamped reports or local `.venv` files stay in the repo but out of the Space upload. During the video I scroll through the Space build logs to show the clean install, then run a sample prompt to confirm the UI renders, the tabs load, and downloads work without dragging along our huge history of test files."

---

## 7. Conclusion (9:00 - 10:00)

**Speaker:**
"To wrap up, MAI Advisor is more than just a tool; it's a capacity multiplier.

For a small non-profit, this system means the difference between *hoping* for funding and *securing* it. We're using the Model Context Protocol to bridge the gap between advanced AI capabilities and the people who need them most.

Thank you for watching."
