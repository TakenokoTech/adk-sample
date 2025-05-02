from google.adk import Agent
from google.adk.tools.agent_tool import AgentTool

from enginear_agent.entity import EvaluateOutput
from enginear_agent.instruction import evaluate_plan_instruction
from enginear_agent.settngs import Settings

evaluate_plan_agent = Agent(
    name="evaluate_plan_agent",
    model=Settings.model,
    instruction=evaluate_plan_instruction,
    output_schema=EvaluateOutput
)

evaluate_plan_tool = AgentTool(agent=evaluate_plan_agent)
