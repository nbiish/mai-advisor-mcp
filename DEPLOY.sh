#!/bin/bash
set -e

echo "🚀 MAI Advisor MCP - Hugging Face Space Deployment"
echo "=================================================="
echo ""

# Check if logged in to Hugging Face
if ! huggingface-cli whoami &>/dev/null; then
    echo "❌ Not logged in to Hugging Face CLI"
    echo ""
    echo "Please run:"
    echo "  huggingface-cli login"
    echo ""
    echo "You'll need a WRITE token from:"
    echo "  https://huggingface.co/settings/tokens"
    echo ""
    exit 1
fi

echo "✅ Authenticated as: $(huggingface-cli whoami | grep 'username:' | awk '{print $2}')"
echo ""

# Navigate to project directory
cd "$(dirname "$0")/grant-finder-mcp"

echo "📦 Uploading files to Hugging Face Space..."
echo ""

# Upload all necessary files
hf upload nbiish/mai-advisor-mcp . \
    app.py \
    requirements.txt \
    README_HF.md \
    src/__init__.py \
    src/search_operators.py \
    --repo-type=space

echo ""
echo "✅ Deployment complete!"
echo ""
echo "🌐 Your Space will be available at:"
echo "   https://huggingface.co/spaces/nbiish/mai-advisor-mcp"
echo ""
echo "⏳ Space is building... Check status at the URL above"
echo ""
