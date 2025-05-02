from google.adk import Agent
from google.adk.tools.agent_tool import AgentTool

from enginear_agent.entity import GeneratePlanOutput
from enginear_agent.instruction import generate_plan_instruction
from enginear_agent.settngs import Settings

generate_plan_agent = Agent(
    name="generate_plan_agent",
    model=Settings.model,
    instruction=generate_plan_instruction,
    output_schema=GeneratePlanOutput
)

generate_plan_tool = AgentTool(agent=generate_plan_agent)
