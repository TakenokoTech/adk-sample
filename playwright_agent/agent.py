# npx @playwright/mcp@latest --port 8931
from contextlib import AsyncExitStack

from google.adk import Agent
from google.adk.models.lite_llm import LiteLlm
from google.adk.tools.mcp_tool import MCPToolset
from google.adk.tools.mcp_tool.mcp_session_manager import SseServerParams


async def create_agent():
    common_exit_stack = AsyncExitStack()
    tools, exit_stack = await MCPToolset.from_server(
        connection_params=SseServerParams(url="http://localhost:8931/sse")
    )
    agent = Agent(
        name="playwright_agent",
        # model="gemini-2.0-flash-lite",
        model=LiteLlm(model="ollama_chat/llama3.2"),
        description="ブラウザで検索を行うエージェント",
        instruction="""
        あなたは、ウェブスクレイピングを行うエージェントです。
        また、取得した内容を要約します。
        検索にはGoogle（https://www.google.com/search）もしくは
        Yahoo JAPAN（https://search.yahoo.co.jp/search）を用います。
        """,
        tools=[*tools],
    )
    return agent, common_exit_stack


root_agent = create_agent()
