from typing import Any
from mcp.server.fastmcp import FastMCP
from crewai_tools import NL2SQLTool

# Khởi tạo FastMCP server cho nhóm 'sql'
mcp = FastMCP("sql")

# Tạo tool xử lý NL2SQL với kết nối PostgreSQL
nl2sql = NL2SQLTool(db_uri="postgresql://sandro:24122004@localhost:5432/test_tool")

@mcp.tool()
async def run_query(query: str) -> Any:
    """Chuyển natural language thành SQL và thực thi"""
    print(f"Query nhận được: {query}")
    try:
        result = nl2sql.run(query)
    except Exception as e:
        result = {"error": str(e)}
    return result


if __name__ == "__main__":
    print("Starting FastMCP server...")
    mcp.run(transport="sse")  