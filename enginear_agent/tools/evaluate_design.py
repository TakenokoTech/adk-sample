from google.adk import Agent
from google.adk.tools.agent_tool import AgentTool

from enginear_agent.entity import EvaluateOutput
from enginear_agent.instruction import evaluate_design_instruction
from enginear_agent.settngs import Settings

evaluate_design_agent = Agent(
    name="evaluate_design_agent",
    model=Settings.model,
    instruction=evaluate_design_instruction,
    output_schema=EvaluateOutput
)

evaluate_design_tool = AgentTool(agent=evaluate_design_agent)
