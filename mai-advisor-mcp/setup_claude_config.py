#!/usr/bin/env python3
"""
Claude Desktop Configuration Helper for MAI Advisor MCP Server

This script generates the proper configuration for Claude Desktop to use
the MAI Advisor MCP server.

Usage:
    python setup_claude_config.py
"""

import json
import os
import platform
from pathlib import Path


def get_claude_config_path():
    """Get the Claude Desktop configuration file path for current OS."""
    system = platform.system()
    
    if system == "Darwin":  # macOS
        return Path.home() / "Library" / "Application Support" / "Claude" / "claude_desktop_config.json"
    elif system == "Windows":
        return Path(os.getenv("APPDATA")) / "Claude" / "claude_desktop_config.json"
    elif system == "Linux":
        return Path.home() / ".config" / "Claude" / "claude_desktop_config.json"
    else:
        raise OSError(f"Unsupported operating system: {system}")


def get_project_path():
    """Get the absolute path to the MAI Advisor project."""
    # This script is in mai-advisor-mcp/mai-advisor-mcp/
    script_path = Path(__file__).resolve()
    project_path = script_path.parent
    return project_path


def create_mcp_config():
    """Create the MCP server configuration for MAI Advisor."""
    project_path = get_project_path()
    server_script = project_path / "src" / "server_mcp.py"
    
    if not server_script.exists():
        raise FileNotFoundError(f"MCP server script not found at: {server_script}")
    
    config = {
        "mai-advisor": {
            "command": "python",
            "args": [str(server_script)],
            "env": {
                "PYTHONPATH": str(project_path)
            }
        }
    }
    
    return config


def update_claude_config():
    """Update or create Claude Desktop configuration."""
    config_path = get_claude_config_path()
    
    print("\n" + "="*60)
    print("MAI ADVISOR - CLAUDE DESKTOP CONFIGURATION")
    print("="*60)
    print(f"\nClaude config file: {config_path}")
    
    # Create directory if it doesn't exist
    config_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Load existing config or create new
    if config_path.exists():
        print("\n✓ Found existing Claude config")
        with open(config_path, 'r') as f:
            try:
                existing_config = json.load(f)
            except json.JSONDecodeError:
                print("⚠️  Warning: Existing config file is invalid JSON")
                existing_config = {}
    else:
        print("\n⊕ Creating new Claude config")
        existing_config = {}
    
    # Ensure mcpServers key exists
    if "mcpServers" not in existing_config:
        existing_config["mcpServers"] = {}
    
    # Add MAI Advisor server config
    mai_config = create_mcp_config()
    existing_config["mcpServers"].update(mai_config)
    
    # Write updated config
    with open(config_path, 'w') as f:
        json.dump(existing_config, f, indent=2)
    
    print("\n✓ Configuration updated successfully")
    print("\nMCP Server Configuration:")
    print(json.dumps(mai_config, indent=2))
    
    print("\n" + "="*60)
    print("NEXT STEPS")
    print("="*60)
    print("""
1. Restart Claude Desktop completely:
   - Quit Claude Desktop (⌘Q on macOS, Alt+F4 on Windows)
   - Wait 5 seconds
   - Relaunch Claude Desktop

2. Verify the server appears:
   - Start a new conversation in Claude
   - Type "@" to see available MCP tools
   - Look for "mai-advisor" in the list

3. Test the integration:
   - Try: "Generate grant strategy for youth STEM education in Seattle"
   - Claude should use the mai-advisor tools automatically

4. Available Tools:
   - generate_grant_strategy
   - generate_search_dorks
   - get_latest_agent_todo
   - get_latest_orchestrator_plan

5. Available Resources:
   - mai://guide/getting-started
   - mai://guide/ai-agent-integration
   - mai://guide/expert-frameworks

If you encounter issues, check the Claude Desktop logs:
""")
    
    system = platform.system()
    if system == "Darwin":
        print("  macOS: ~/Library/Logs/Claude/")
    elif system == "Windows":
        print("  Windows: %APPDATA%\\Claude\\logs\\")
    elif system == "Linux":
        print("  Linux: ~/.config/Claude/logs/")
    
    print("\n✅ Setup complete!")
    print("="*60)
    print()


def show_manual_config():
    """Show manual configuration instructions."""
    project_path = get_project_path()
    server_script = project_path / "src" / "server_mcp.py"
    
    print("\n" + "="*60)
    print("MANUAL CONFIGURATION (if automatic setup fails)")
    print("="*60)
    
    config_path = get_claude_config_path()
    
    manual_config = {
        "mcpServers": {
            "mai-advisor": {
                "command": "python",
                "args": [str(server_script)],
                "env": {
                    "PYTHONPATH": str(project_path)
                }
            }
        }
    }
    
    print(f"""
1. Open this file in a text editor:
   {config_path}

2. Add this configuration:

{json.dumps(manual_config, indent=2)}

3. Save the file

4. Restart Claude Desktop

That's it!
""")


if __name__ == "__main__":
    try:
        update_claude_config()
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("\nShowing manual configuration instructions...\n")
        show_manual_config()
