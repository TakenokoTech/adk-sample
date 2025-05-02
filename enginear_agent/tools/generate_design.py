from google.adk import Agent
from google.adk.tools.agent_tool import AgentTool

from enginear_agent.entity import GenerateDesignOutput
from enginear_agent.instruction import generate_design_instruction
from enginear_agent.settngs import Settings

generate_design_agent = Agent(
    name="generate_design_agent",
    model=Settings.model,
    instruction=generate_design_instruction,
    output_schema=GenerateDesignOutput
)

generate_design_tool = AgentTool(agent=generate_design_agent)
