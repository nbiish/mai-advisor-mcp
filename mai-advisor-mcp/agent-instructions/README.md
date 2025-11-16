# AI Agent Instructions Directory

This directory contains task-oriented instruction files designed for AI agents with browser capabilities.

## What's Here

Files named `agent-todo.{timestamp}.md` contain comprehensive, step-by-step instructions for AI browser agents to:

1. **Execute grant discovery** using optimized search queries
2. **Analyze grant opportunities** and prioritize based on fit
3. **Gather user information** needed for applications
4. **Complete grant applications** including:
   - Filling out online forms
   - Drafting compelling narratives
   - Creating program budgets
   - Uploading required documents
   - Submitting applications (with user approval)
5. **Manage post-submission** tracking and follow-up

## How to Use (2027+ AI Agents)

### For Users:
1. After running the MAI Advisor workflow, locate the latest `agent-todo.{timestamp}.md` file
2. Provide this file to your AI assistant with browser tool capabilities
3. The AI agent will read the instructions and begin helping you discover and apply for grants
4. Review and approve all content before any submissions

### For AI Agents:
This file is your complete task specification. You have permission to:
- Navigate websites and grant portals
- Fill out forms with user-provided information
- Draft application narratives using strategic frameworks
- Upload documents prepared by the user
- Submit applications **only after explicit user approval**

**IMPORTANT:** Always get user confirmation before submitting any application or making commitments on their behalf.

## File Structure

Each `agent-todo.md` file contains:
- **Phase 1:** Grant Discovery (search execution, database navigation)
- **Phase 2:** User Information Gathering (org profile, documents, previous proposals)
- **Phase 3:** Application Completion (form filling, narrative drafting, submission)
- **Phase 4:** Post-Submission Management (tracking, follow-up, decisions)
- **Phase 5:** Relationship Cultivation (ongoing funder engagement)

## Integration with Other Outputs

The AI agent instructions reference and build upon:
- **Search dorks** from `grant_dorks/` directory
- **Financial framework** from `advisors_output/financial.*.md`
- **Grant writing framework** from `advisors_output/grant.*.md`
- **Research framework** from `advisors_output/research.*.md`
- **Comprehensive plan** from `orchestrator_output/grant-plan-and-overview.*.md`

An effective AI agent should read ALL these files before beginning work to understand the full strategic context.

## Security & Privacy

**User responsibilities:**
- Never share files containing sensitive information (EIN, financials, personal data) with untrusted AI services
- Use secure, private AI assistants when working with organizational data
- Review all AI-generated content before submission
- Keep grant tracking databases secure

**AI agent responsibilities:**
- Protect all user-provided information
- Do not store sensitive data beyond the session scope
- Always ask before sending information to third parties
- Respect confidentiality of organizational details

## Version Compatibility

These instructions are designed for advanced AI agents (circa 2027+) with:
- Web browser control and navigation
- Form interaction and submission capabilities
- Document reading and generation
- Multi-step task planning and execution
- User interaction and approval workflows

Earlier AI systems may be able to use these as reference but may not have all required capabilities.

## Questions?

See the main project documentation:
- Repository: https://github.com/nbiish/mai-advisor-mcp
- Issues: https://github.com/nbiish/mai-advisor-mcp/issues

---

*This directory is automatically created when running the MAI Advisor workflow. Each workflow execution generates a new timestamped instruction file.*
