from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    name = "planning_agent"
    # model = LiteLlm(model="ollama_chat/llama3.2")
    model = "gemini-2.0-flash-lite"
    description = "プランニングエージェント"
    instruction = "与えられたタスクに対して、最適な計画を立てるエージェントです。"
