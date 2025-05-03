from google.adk import Agent
from google.adk.agents import LlmAgent, LoopAgent, SequentialAgent

from enginear_agent.settngs import Settings
from enginear_agent.tools.evaluate_design import evaluate_design_agent
from enginear_agent.tools.evaluate_plan import evaluate_plan_agent
from enginear_agent.tools.evaluate_task import evaluate_task_agent
from enginear_agent.tools.generate_design import generate_design_agent
from enginear_agent.tools.generate_plan import generate_plan_agent
from enginear_agent.tools.update_design import update_design_agent
from enginear_agent.tools.update_plan import update_plan_agent
from enginear_agent.tools.update_task import update_task_agent

sequential_plan_agent = SequentialAgent(
    name="sequential_plan_agent",
    description="プランニングを行うためのエージェント",
    sub_agents=[
        generate_plan_agent,
        LoopAgent(
            name="loop_plan_agent",
            max_iterations=2,
            sub_agents=[
                evaluate_plan_agent,
                update_plan_agent,
            ],
        ),
        LoopAgent(
            name="loop_task_agent",
            max_iterations=2,
            sub_agents=[
                evaluate_task_agent,
                update_task_agent,
            ],
        ),
        Agent(
            name="generate_plan_agent",
            model=Settings.model,
            instruction="与えられたインプットをYAML形式で整理し直して出力してください。updateは不要です。",
        )
    ]
)

sequential_design_agent = SequentialAgent(
    name="sequential_design_agent",
    description="設計を行うためのエージェント",
    sub_agents=[
        generate_design_agent,
        LoopAgent(
            name="loop_design_agent",
            max_iterations=2,
            sub_agents=[
                evaluate_design_agent,
                update_design_agent,
            ],
        ),
        Agent(
            name="generate_design_agent",
            model=Settings.model,
            instruction="与えられたインプットをYAML形式で整理し直して出力してください。updateは不要です。",
        )
    ]
)

root_agent = LlmAgent(
    name=Settings.name,
    model=Settings.model,
    description=Settings.description,
    instruction=Settings.instruction,
    sub_agents=[
        sequential_plan_agent,
        sequential_design_agent,
    ],
)
