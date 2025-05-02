from google.adk import Agent
from google.adk.tools.agent_tool import AgentTool

from enginear_agent.entity import UpdateTaskOutput
from enginear_agent.instruction import update_task_instruction
from enginear_agent.settngs import Settings

update_task_agent = Agent(
    name="update_plan_agent",
    model=Settings.model,
    instruction=update_task_instruction,
    output_schema=UpdateTaskOutput
)

update_task_tool = AgentTool(agent=update_task_agent)
