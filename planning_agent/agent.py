import logging

from google.adk import Agent
from google.adk.agents import SequentialAgent, LlmAgent

from planning_agent.entity import GeneratePlanOutput
from planning_agent.settngs import Settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

planning_agent = LlmAgent(
    name="generate_plan_agent",
    model=Settings.model,
    instruction="""
    与えられたタスクに対して、実行計画を3つのステップに分けて立ててください。
    ただし、１つのステップ内の作業は細かく明確にしてください。
    """,
    output_schema=GeneratePlanOutput,
    output_key="output",
)

"""
execute_agent = LlmAgent(
    name="execute_agent",
    model=Settings.model,
    instruction=""
    与えられたステップを１つ実施してください。
    内容に関して、不明瞭な事項があっても勝手に決めて問題ありません。
    "",
    sub_agents=[
        Agent(
            name="generate_design_agent",
            model=Settings.model,
            instruction=generate_design_instruction + "結果はresolvedに格納してください。",
            output_schema=UpdatePlanOutput,
        ),
        Agent(
            name="generate_plan_agent",
            model=Settings.model,
            instruction=generate_plan_instruction + "結果はresolvedに格納してください。",
            output_schema=UpdatePlanOutput,
        )
    ],
)

class ExecuteAgent(BaseAgent):
    async def _run_async_impl(self, ctx: InvocationContext) -> AsyncGenerator[Event, None]:
        logger.info(f"[{self.name}] start.")
        steps = ctx.session.state.get("output", {}).get("steps", [])
        for step in steps[0:3]:
            current_ctx = ctx.model_copy()
            current_ctx.session.state["output"] = step
            logger.info(f"[{self.name}] step: {step}, current_ctx: {current_ctx}")
            # async for event in execute_agent.run_async(current_ctx):
            #     yield event
            yield Event(author=self.name, content={"parts": [{"text": step}]}, actions=EventActions())
"""

root_agent = SequentialAgent(
    name=Settings.name,
    description=Settings.description,
    sub_agents=[
        planning_agent,
        # LoopAgent(
        #     name="loop_agent",
        #     sub_agents=[
        #         Agent(
        #             name="generate_design_agent",
        #             model=Settings.model,
        #             instruction=f"""
        #             与えられたステップを１つ実施してください。
        #             {generate_design_instruction}
        #             "結果はresolvedに格納してください。
        #             """,
        #             output_schema=UpdatePlanOutput,
        #         ),
        #         Agent(
        #             name="generate_plan_agent",
        #             model=Settings.model,
        #             instruction=f"""
        #             与えられたステップを１つ実施してください。
        #             {generate_plan_instruction}
        #             "結果はresolvedに格納してください。
        #             """,
        #             output_schema=UpdatePlanOutput,
        #         )
        #     ],
        #     max_iterations=3
        # ),
        Agent(
            name="generate_output_agent",
            model=Settings.model,
            instruction="与えられたインプットをYAML形式で整理し直して出力してください。updateは不要です。",
        )
    ]
)
