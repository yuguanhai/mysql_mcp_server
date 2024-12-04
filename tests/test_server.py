# tests/test_server.py
import pytest
from mysql_mcp_server.server import app

def test_server_initialization():
    """Test that the server initializes correctly."""
    assert app.name == "mysql_mcp_server"

@pytest.mark.asyncio
async def test_list_tools():
    """Test that list_tools returns expected tools."""
    tools = await app.list_tools()
    assert len(tools) == 1
    assert tools[0].name == "execute_sql"