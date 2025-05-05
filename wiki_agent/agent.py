from google.adk import Agent
from google.adk.agents import SequentialAgent, LoopAgent

from wiki_agent.settngs import Settings
from wiki_agent.tools.check_mermaid import check_mermaid_format
from wiki_agent.tools.fetch_code import fetch_source_code, fetch_file_tree

fetch_file_agent = Agent(
    name="fetch_file_agent",
    model=Settings.model,
    instruction=Settings.tree_instruction,
    tools=[fetch_file_tree],
    output_key="tree",
)

plan_agent = Agent(
    name="plan_agent",
    model=Settings.model,
    instruction=Settings.plan_instruction,
    output_key="plan",
)

fetch_source_agent = Agent(
    name="fetch_source_agent",
    model=Settings.model,
    instruction=Settings.source_instruction,
    tools=[fetch_source_code],
    output_key="source",
)

check_agent = Agent(
    name="check_agent",
    model=Settings.model,
    instruction=Settings.check_instruction,
    output_key="check",
)

generate_markdown_agent = Agent(
    name="generate_markdown_agent",
    model=Settings.model,
    instruction=Settings.markdown_instruction,
)

evaluate_markdown_agent = Agent(
    name="evaluate_markdown_agent",
    model=Settings.model,
    instruction=Settings.evaluate_instruction,
    output_key="evaluate",
    tools=[check_mermaid_format],
)

update_markdown_agent = Agent(
    name="update_markdown_agent",
    model=Settings.model,
    instruction=Settings.markdown_instruction,
)

root_agent = SequentialAgent(
    name=Settings.name,
    description=Settings.description,
    sub_agents=[
        fetch_file_agent,
        plan_agent,
        LoopAgent(
            name=Settings.name,
            max_iterations=2,
            sub_agents=[fetch_source_agent, check_agent],
        ),
        generate_markdown_agent,
        LoopAgent(
            name=Settings.name,
            max_iterations=1,
            sub_agents=[evaluate_markdown_agent, update_markdown_agent],
        ),
    ]
)
