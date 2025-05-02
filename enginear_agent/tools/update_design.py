from google.adk import Agent
from google.adk.tools.agent_tool import AgentTool

from enginear_agent.entity import UpdateDesignOutput
from enginear_agent.instruction import update_design_instruction
from enginear_agent.settngs import Settings

update_design_agent = Agent(
    name="update_design_agent",
    model=Settings.model,
    instruction=update_design_instruction,
    output_schema=UpdateDesignOutput
)

update_design_tool = AgentTool(agent=update_design_agent)
