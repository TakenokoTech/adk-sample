from google.adk import Agent
from google.adk.tools.agent_tool import AgentTool

from enginear_agent.entity import EvaluateOutput
from enginear_agent.instruction import evaluate_task_instruction
from enginear_agent.settngs import Settings

evaluate_task_agent = Agent(
    name="evaluate_task_agent",
    model=Settings.model,
    instruction=evaluate_task_instruction,
    output_schema=EvaluateOutput
)

evaluate_task_tool = AgentTool(agent=evaluate_task_agent)
