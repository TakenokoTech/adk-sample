from google.adk.agents import Agent

from multi_tool_agent.tools.get_current_time import get_current_time
from multi_tool_agent.tools.get_weather import get_weather

root_agent = Agent(
    name="weather_time_agent",
    model="gemini-2.0-flash-exp",
    description="都市の時間と天気に関する質問に答えるエージェント",
    instruction="あなたは都市の時間や天気に関するユーザーの質問に答えることができる親切なエージェントです",
    tools=[get_weather, get_current_time],
)
