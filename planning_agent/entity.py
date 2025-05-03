from pydantic import BaseModel


class GeneratePlanOutput(BaseModel):
    class Step(BaseModel):
        description: str

    steps: list[Step]


class UpdatePlanOutput(BaseModel):
    class Step(BaseModel):
        description: str
        resolved: str | None

    steps: list[Step]
