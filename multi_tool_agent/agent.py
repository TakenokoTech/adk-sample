from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

from multi_tool_agent.tools.get_weather import get_weather

# model = "gemini-2.0-flash-exp"
# model = LiteLlm(model="ollama_chat/gemma3:4b")
# model = LiteLlm(model="ollama_chat/deepseek-r1")
model = LiteLlm(model="ollama_chat/llama3.2")
# model = LiteLlm(model="ollama/mistral-small3.1")
# litellm._turn_on_debug()

root_agent = Agent(
    name="weather_time_agent",
    model=model,
    description="都市の時間と天気に関する質問に答えるエージェント",
    instruction="あなたは都市の時間や天気に関するユーザーの質問に答えることができる親切なエージェントです",
    # description="An agent that answers questions about the time and weather in a city",
    # instruction="You are a helpful agent who can answer users' questions about the time and weather in their city.",
    tools=[
        get_weather,
        # get_current_time
        # playwright_tool
    ],
)
