#!/bin/bash

# Sanitize settings.json files - Remove API keys and personal paths
# This script is used locally before committing configuration files

set -e

echo "🧹 Sanitizing settings.json files..."

# Check if jq is installed
if ! command -v jq &> /dev/null; then
    echo "❌ jq is required but not installed."
    echo "Install it with: brew install jq"
    exit 1
fi

# Find and process all settings.json files in .configs
find mai-advisor-mcp/.configs -name "settings.json" -type f | while read -r file; do
    echo "Processing: $file"
    
    # Create backup
    cp "$file" "$file.backup"
    
    # Sanitize using jq
    jq 'walk(
      if type == "object" then
        # Remove API keys
        if has("BRAVE_API_KEY") then .BRAVE_API_KEY = "YOUR_BRAVE_API_KEY_HERE" else . end |
        if has("TAVILY_API_KEY") then .TAVILY_API_KEY = "YOUR_TAVILY_API_KEY_HERE" else . end |
        # Replace absolute paths with placeholders
        if has("cwd") and (.cwd | startswith("/Volumes/") or startswith("/Users/")) then 
          .cwd = "/path/to/your/mcp/servers" 
        else . end |
        if has("MEMORY_FILE_PATH") and (.MEMORY_FILE_PATH | startswith("/Volumes/") or startswith("/Users/")) then 
          .MEMORY_FILE_PATH = "/path/to/your/memory/memories.jsonl" 
        else . end
      else . end
    ) | walk(
      if type == "array" then
        map(if type == "string" and contains("tavilyApiKey=") then
          sub("tavilyApiKey=[^&\"\\s]+"; "tavilyApiKey=YOUR_TAVILY_API_KEY_HERE")
        else . end)
      else . end
    ) | walk(
      if type == "string" then
        # Replace any remaining API key patterns
        gsub("BSA[a-zA-Z0-9]{27}"; "YOUR_BRAVE_API_KEY_HERE") |
        gsub("tvly-[a-zA-Z0-9-]{30,}"; "YOUR_TAVILY_API_KEY_HERE")
      else . end
    )' "$file" > "$file.tmp" && mv "$file.tmp" "$file"
    
    echo "✓ Sanitized: $file (backup saved as $file.backup)"
done

echo ""
echo "✅ Sanitization complete!"
echo ""
echo "Review the changes and commit:"
echo "  git diff mai-advisor-mcp/.configs/"
echo "  git add mai-advisor-mcp/.configs/"
echo "  git commit -m '🔒 chore: sanitize settings.json'"
