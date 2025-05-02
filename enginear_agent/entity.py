from pydantic import BaseModel


class GeneratePlanOutput(BaseModel):
    class Item(BaseModel):
        day: int
        title: str
        content: str

    title: str
    goal: str
    timeline: list[Item]


class GenerateDesignOutput(BaseModel):
    class Spec(BaseModel):
        category: str
        description: list[str]

    specs: list[Spec]


class UpdatePlanOutput(BaseModel):
    class Item(BaseModel):
        day: int
        title: str
        content: str

    title: str
    goal: str
    timeline: list[Item]
    update: str


class UpdateTaskOutput(BaseModel):
    class Task(BaseModel):
        class SubTask(BaseModel):
            estimated_hours: int
            summary: str
            acceptance_criteria: list[str]

        name: str
        sub_tasks: list[SubTask]

    title: str
    goal: str
    timeline: list[Task]
    update: str


class UpdateDesignOutput(BaseModel):
    class Spec(BaseModel):
        category: str
        description: list[str]

    specs: list[Spec]
    update: str


class EvaluateOutput(BaseModel):
    evaluation: str
    improvements: str
