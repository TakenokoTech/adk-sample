from google.adk import Agent
from google.adk.tools.agent_tool import AgentTool

from enginear_agent.entity import UpdatePlanOutput
from enginear_agent.instruction import update_plan_instruction
from enginear_agent.settngs import Settings

update_plan_agent = Agent(
    name="update_plan_agent",
    model=Settings.model,
    instruction=update_plan_instruction,
    output_schema=UpdatePlanOutput
)

update_plan_tool = AgentTool(agent=update_plan_agent)
