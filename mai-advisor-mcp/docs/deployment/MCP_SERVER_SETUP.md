# MAI Advisor - MCP Server Setup Guide

This guide explains how to use MAI Advisor as a Model Context Protocol (MCP) server. This allows AI assistants (like Claude Desktop, Cursor, etc.) to directly access the grant planning tools.

## 🚀 Overview

When running as an MCP server, MAI Advisor exposes the following tools to your AI assistant:

1. **`generate_grant_strategy`**: Generates a complete grant planning strategy.
   * **Inputs**:
     * `topic` (string): The grant focus area (e.g., "youth STEM education").
     * `location` (string, optional): Geographic location (e.g., "Phoenix, AZ").
   * **Outputs**: Creates comprehensive strategic plans, search dorks, and agent instructions.

2. **`generate_search_dorks`**: Generates optimized search queries only.
   * **Inputs**: `topic`, `location`.

## ⚙️ Configuration

The MCP server is configured using environment variables. You can set these in your MCP client configuration (e.g., `claude_desktop_config.json`).

### Required Environment Variables

* **`OPENROUTER_API_KEY`**: Your OpenRouter API key. This is required for the expert advisors to generate content using the Google Gemini 2.5 Flash model.
  * Get a key at: [openrouter.ai/keys](https://openrouter.ai/keys)

### Optional Environment Variables

* **`MAI_ADVISOR_OUTPUT_DIR`**: The directory where all generated files will be saved.
  * **Default**: The root directory of the repository.
  * **Recommendation**: Set this to a dedicated folder (absolute path) so you can easily find the outputs.

## 💻 Installation & Usage

### Option 1: Local Python Installation (Recommended)

If you have the repository cloned locally:

1. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

2. **Configure Claude Desktop**:
   Edit your `~/Library/Application Support/Claude/claude_desktop_config.json` (macOS) or `%APPDATA%\Claude\claude_desktop_config.json` (Windows):

   ```json
   {
     "mcpServers": {
       "mai-advisor": {
         "command": "python",
         "args": ["/ABSOLUTE/PATH/TO/mai-advisor-mcp/src/server_mcp.py"],
         "env": {
           "OPENROUTER_API_KEY": "sk-or-v1-...",
           "MAI_ADVISOR_OUTPUT_DIR": "/ABSOLUTE/PATH/TO/OUTPUT/FOLDER"
         }
       }
     }
   }
   ```

3. **Restart Claude Desktop**. The tools should now be available.

### Option 2: Hugging Face Spaces (Remote)

If you are deploying this to a Hugging Face Space, you can use the generic "Hugging Face MCP Server" to connect to it, or run the MCP server directly if supported by your environment.

**Note**: For the most reliable experience with file outputs, we recommend Option 1 (Local), as the server needs to write files to your local filesystem for you to access them easily.

## 📝 How to Use with AI

Once connected, you can ask your AI assistant:

> "Generate a grant strategy for a community health initiative in Seattle."

The AI will:

1. Call the `generate_grant_strategy` tool with your topic and location.
2. The MCP server will run the workflow (generating dorks, expert plans, and final strategy).
3. The files will be saved to your `MAI_ADVISOR_OUTPUT_DIR`.
4. The AI will confirm the files have been created and provide a summary.

## 📂 Output Structure

The server will create the following structure in your output directory:

```text
MAI_ADVISOR_OUTPUT_DIR/
├── grant_dorks/          # Search queries
├── advisors_output/      # Expert strategic plans
├── orchestrator_output/  # Final grant plan
└── agent-instructions/   # AI agent todo lists
```
