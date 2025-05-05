from mcp import ClientSession
from mcp.client.sse import sse_client

async def check():
    async with sse_client("http://0.0.0.0:8000/sse") as streams:
        async with ClientSession(*streams) as session:
            await session.initialize()

            # List avail tool
            # tools = await session.list_tools()
            # print(tools)

            # Call add tool
            result = await session.call_tool("run_query", arguments={"query":" Danh sách tất cả các nghệ sĩ trong cơ sở dữ liệu?t"})
            print(result)




if __name__ == "__main__":
    import asyncio
    asyncio.run(check())