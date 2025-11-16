#!/usr/bin/env python3
"""
Test script for MAI Advisor MCP Server

This script tests the MCP server functionality locally before deploying
to Claude Desktop or other MCP clients.

Usage:
    python test_mcp_server.py
"""

import asyncio
import json
from pathlib import Path
import sys

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from server_mcp import app


async def test_list_tools():
    """Test that all tools are properly registered."""
    print("\n" + "="*60)
    print("TEST: List Available Tools")
    print("="*60)
    
    tools = await app.list_tools()
    
    print(f"\n✓ Found {len(tools)} tools:\n")
    for i, tool in enumerate(tools, 1):
        print(f"{i}. {tool.name}")
        print(f"   Description: {tool.description[:100]}...")
        print(f"   Required params: {tool.inputSchema.get('required', [])}")
        print()
    
    assert len(tools) == 4, f"Expected 4 tools, found {len(tools)}"
    print("✓ Tool list test PASSED\n")


async def test_list_resources():
    """Test that all resources are properly registered."""
    print("\n" + "="*60)
    print("TEST: List Available Resources")
    print("="*60)
    
    resources = await app.list_resources()
    
    print(f"\n✓ Found {len(resources)} resources:\n")
    for i, resource in enumerate(resources, 1):
        print(f"{i}. {resource.name}")
        print(f"   URI: {resource.uri}")
        print(f"   Type: {resource.mimeType}")
        print()
    
    assert len(resources) == 3, f"Expected 3 resources, found {len(resources)}"
    print("✓ Resource list test PASSED\n")


async def test_read_resource():
    """Test reading a resource."""
    print("\n" + "="*60)
    print("TEST: Read Resource Content")
    print("="*60)
    
    from pydantic import AnyUrl
    
    uri = AnyUrl("mai://guide/getting-started")
    content = await app.read_resource(uri)
    
    print(f"\n✓ Retrieved resource: mai://guide/getting-started")
    print(f"   Content length: {len(content)} characters")
    print(f"   Preview: {content[:200]}...")
    print()
    
    assert len(content) > 100, "Resource content too short"
    assert "MAI Advisor" in content, "Resource content missing expected text"
    print("✓ Resource read test PASSED\n")


async def test_generate_dorks():
    """Test search dork generation."""
    print("\n" + "="*60)
    print("TEST: Generate Search Dorks")
    print("="*60)
    
    result = await app.call_tool(
        "generate_search_dorks",
        {
            "topic": "youth STEM education",
            "location": "Phoenix, Arizona"
        }
    )
    
    content = result[0].text
    print(f"\n✓ Generated dorks successfully")
    print(f"   Response length: {len(content)} characters")
    print(f"\n--- Sample Output ---")
    print(content[:500])
    print("...\n")
    
    assert "Google" in content, "Missing Google dorks"
    assert "Bing" in content, "Missing Bing dorks"
    assert "DuckDuckGo" in content, "Missing DuckDuckGo dorks"
    print("✓ Dork generation test PASSED\n")


async def test_generate_full_strategy():
    """Test full grant strategy generation."""
    print("\n" + "="*60)
    print("TEST: Generate Complete Grant Strategy")
    print("="*60)
    print("\n⚠️  This test generates actual files and may take 30-60 seconds...")
    print("    (Uses AI models for expert frameworks and orchestration)")
    
    # Ask for confirmation
    response = input("\nProceed with full strategy test? [y/N]: ").strip().lower()
    if response != 'y':
        print("\n⊘ Skipping full strategy test")
        return
    
    print("\n🔄 Generating strategy...")
    
    result = await app.call_tool(
        "generate_grant_strategy",
        {
            "topic": "community health initiative",
            "location": "Seattle"
        }
    )
    
    content = result[0].text
    print(f"\n✓ Strategy generated successfully")
    print(f"\n--- Output ---")
    print(content)
    print()
    
    # Verify files were created
    assert Path("grant_dorks").exists(), "grant_dorks directory not created"
    assert Path("advisors_output").exists(), "advisors_output directory not created"
    assert Path("orchestrator_output").exists(), "orchestrator_output directory not created"
    assert Path("agent-instructions").exists(), "agent-instructions directory not created"
    
    print("✓ Full strategy test PASSED\n")
    print("✓ All output directories created successfully")


async def test_get_latest_files():
    """Test retrieving latest generated files."""
    print("\n" + "="*60)
    print("TEST: Retrieve Latest Generated Files")
    print("="*60)
    
    # Check if files exist
    if not Path("agent-instructions").exists():
        print("\n⊘ Skipping - no files generated yet (run full strategy test first)")
        return
    
    # Test get_latest_agent_todo
    print("\n🔄 Retrieving latest agent todo...")
    result = await app.call_tool("get_latest_agent_todo", {})
    content = result[0].text
    print(f"✓ Retrieved agent todo ({len(content)} characters)")
    
    # Test get_latest_orchestrator_plan
    print("\n🔄 Retrieving latest orchestrator plan...")
    result = await app.call_tool("get_latest_orchestrator_plan", {})
    content = result[0].text
    print(f"✓ Retrieved orchestrator plan ({len(content)} characters)")
    
    print("\n✓ File retrieval test PASSED\n")


async def run_all_tests():
    """Run all test suites."""
    print("\n")
    print("╔" + "="*58 + "╗")
    print("║" + " "*10 + "MAI ADVISOR MCP SERVER TEST SUITE" + " "*15 + "║")
    print("╚" + "="*58 + "╝")
    
    try:
        await test_list_tools()
        await test_list_resources()
        await test_read_resource()
        await test_generate_dorks()
        await test_generate_full_strategy()
        await test_get_latest_files()
        
        print("\n" + "="*60)
        print("✅ ALL TESTS PASSED")
        print("="*60)
        print("\nMCP Server is ready for deployment!")
        print("\nNext steps:")
        print("1. Configure Claude Desktop (see README_DEPLOY.md)")
        print("2. Test with Claude Desktop client")
        print("3. Deploy to HuggingFace Space (optional)")
        print()
        
    except Exception as e:
        print("\n" + "="*60)
        print("❌ TEST FAILED")
        print("="*60)
        print(f"\nError: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(run_all_tests())
