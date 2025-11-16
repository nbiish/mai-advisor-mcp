#!/usr/bin/env zsh
# Launch MAI Advisor MCP Gradio app reliably from repo root
set -euo pipefail

ROOT_DIR=${0:A:h}
APP_DIR="$ROOT_DIR/mai-advisor-mcp"

if [[ ! -d "$APP_DIR" ]]; then
  echo "❌ Could not find app directory at $APP_DIR" >&2
  exit 1
fi

cd "$APP_DIR"

# Activate venv if present
if [[ -f "venv/bin/activate" ]]; then
  echo "🔧 Activating virtual environment..."
  source venv/bin/activate
else
  echo "ℹ️ No venv found at $APP_DIR/venv; using current Python."
fi

echo "🚀 Starting Gradio app..."
exec python app.py
