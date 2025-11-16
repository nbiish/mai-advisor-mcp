#!/bin/bash
# MAI Advisor MCP - Quick Setup Script

set -e  # Exit on error

echo "========================================"
echo "MAI Advisor MCP - Quick Setup"
echo "========================================"
echo ""

# Check Python version
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 is not installed"
    echo "Please install Python 3.10 or higher"
    exit 1
fi

PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
echo "✓ Found Python $PYTHON_VERSION"

# Create virtual environment
echo ""
echo "Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip > /dev/null 2>&1

# Install dependencies
echo "Installing dependencies..."
pip install -e . > /dev/null 2>&1

echo ""
echo "✅ Installation complete!"
echo ""
echo "========================================"
echo "Next Steps:"
echo "========================================"
echo ""
echo "1. Copy environment template:"
echo "   cp .env.example .env"
echo ""
echo "2. Edit .env and add your API keys:"
echo "   - ANTHROPIC_API_KEY (required)"
echo "   - TAVILY_API_KEY (required)"
echo "   - Optional: NEBIUS_API_KEY"
echo ""
echo "3. Get API keys from:"
echo "   - Anthropic: https://console.anthropic.com/"
echo "   - Tavily: https://www.tavily.com/"
echo "   - Nebius: https://tokenfactory.nebius.com/"
echo ""
echo "4. Test the installation:"
echo "   source venv/bin/activate"
echo "   python examples/search_operators_example.py"
echo ""
echo "5. Read the guides:"
echo "   - QUICKSTART.md for 5-minute setup"
echo "   - README.md for full documentation"
echo ""
echo "========================================"
echo "🎯 Happy grant hunting!"
echo "========================================"
