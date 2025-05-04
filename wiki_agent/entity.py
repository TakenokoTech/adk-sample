from pydantic import BaseModel


class TreeOutput(BaseModel):
    paths: list[str]


class PlanOutput(BaseModel):
    plans: list[str]


class CheckOutput(BaseModel):
    docs: str
    next_action: str
