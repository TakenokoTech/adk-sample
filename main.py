import asyncio

from dotenv import load_dotenv

from multi_tool_agent.tools.call_agent_async import call_agent_async

load_dotenv()


async def run_conversation():
    await call_agent_async("東京の天気を教えて?")
    await call_agent_async("大阪は?")


if __name__ == "__main__":
    asyncio.run(run_conversation())
