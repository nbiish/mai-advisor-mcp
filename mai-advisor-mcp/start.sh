#!/bin/bash

# MAI Advisor Quick Start Script
# Helps launch the app in different modes

set -e

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo ""
echo "╔══════════════════════════════════════════════════════════╗"
echo "║                                                          ║"
echo "║            MAI ADVISOR - GRANT PLANNING SYSTEM           ║"
echo "║                                                          ║"
echo "╚══════════════════════════════════════════════════════════╝"
echo ""

# Function to check if virtual environment exists
check_venv() {
    if [ ! -d ".venv" ]; then
        echo -e "${YELLOW}⚠️  Virtual environment not found${NC}"
        echo ""
        echo "Creating virtual environment..."
        python3 -m venv .venv
        echo -e "${GREEN}✓ Virtual environment created${NC}"
        echo ""
        echo "Installing dependencies..."
        source .venv/bin/activate
        pip install -q --upgrade pip
        pip install -q -r requirements.txt
        echo -e "${GREEN}✓ Dependencies installed${NC}"
        echo ""
    else
        echo -e "${GREEN}✓ Virtual environment found${NC}"
    fi
}

# Function to activate virtual environment
activate_venv() {
    if [ -f ".venv/bin/activate" ]; then
        source .venv/bin/activate
        echo -e "${GREEN}✓ Virtual environment activated${NC}"
    elif [ -f ".venv/Scripts/activate" ]; then
        source .venv/Scripts/activate
        echo -e "${GREEN}✓ Virtual environment activated${NC}"
    else
        echo -e "${YELLOW}⚠️  Could not find venv activation script${NC}"
        exit 1
    fi
}

# Function to run Gradio web app
run_gradio() {
    echo ""
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${BLUE}  Starting Gradio Web Interface${NC}"
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""
    echo "  🌐 Web interface will launch at: http://localhost:7860"
    echo ""
    echo "  📝 Use the web UI to:"
    echo "     • Generate grant strategies"
    echo "     • View expert frameworks"
    echo "     • Download AI agent instructions"
    echo ""
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""
    echo "Press Ctrl+C to stop the server"
    echo ""
    python app_workflow.py
}

# Function to run MCP server
run_mcp() {
    echo ""
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${BLUE}  Starting MCP Server (stdio mode)${NC}"
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""
    echo "  🔌 MCP server is running in stdio mode"
    echo ""
    echo "  📝 This mode is designed for:"
    echo "     • Claude Desktop integration"
    echo "     • Other MCP-compatible clients"
    echo "     • Programmatic access via MCP protocol"
    echo ""
    echo "  ⚠️  This is NOT a web interface!"
    echo "     For web access, use mode 1 (Gradio)"
    echo ""
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""
    echo "Press Ctrl+C to stop the server"
    echo ""
    python src/server_mcp.py
}

# Function to setup Claude Desktop
setup_claude() {
    echo ""
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${BLUE}  Claude Desktop Configuration${NC}"
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""
    python setup_claude_config.py
}

# Function to run tests
run_tests() {
    echo ""
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${BLUE}  Running MCP Server Tests${NC}"
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""
    python test_mcp_server.py
}

# Main menu
show_menu() {
    echo ""
    echo "Choose a mode:"
    echo ""
    echo "  1) 🌐 Gradio Web Interface (default)"
    echo "     Launch the web UI at http://localhost:7860"
    echo ""
    echo "  2) 🔌 MCP Server (stdio mode)"
    echo "     For Claude Desktop / MCP clients"
    echo ""
    echo "  3) ⚙️  Setup Claude Desktop"
    echo "     Configure Claude Desktop to use MAI Advisor"
    echo ""
    echo "  4) 🧪 Run Tests"
    echo "     Test the MCP server functionality"
    echo ""
    echo "  5) 🚪 Exit"
    echo ""
    echo -n "Enter choice [1-5]: "
}

# Check and activate venv
check_venv
activate_venv
echo ""

# Main loop
while true; do
    show_menu
    read choice
    
    case $choice in
        1)
            run_gradio
            ;;
        2)
            run_mcp
            ;;
        3)
            setup_claude
            ;;
        4)
            run_tests
            ;;
        5)
            echo ""
            echo -e "${GREEN}Goodbye!${NC}"
            echo ""
            exit 0
            ;;
        "")
            # Default to Gradio
            run_gradio
            ;;
        *)
            echo ""
            echo -e "${YELLOW}Invalid choice. Please enter 1-5.${NC}"
            ;;
    esac
    
    echo ""
    echo -e "${YELLOW}Press Enter to return to menu...${NC}"
    read
done
