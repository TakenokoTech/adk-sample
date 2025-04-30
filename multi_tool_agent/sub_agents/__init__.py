from google.adk.tools.agent_tool import AgentTool

from playwright_agent.agent import root_agent as playwright_agent

playwright_tool = AgentTool(agent=playwright_agent)
