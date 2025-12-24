from pydantic import BaseModel
from typing import Optional


class QuestionChoiceBase(BaseModel):
    label: str
    content: str
    result_type: str


class QuestionChoiceCreate(QuestionChoiceBase):
    pass


class QuestionChoiceUpdate(BaseModel):
    label: Optional[str] = None
    content: Optional[str] = None
    result_type: Optional[str] = None


class QuestionChoiceResponse(BaseModel):
    choice_id: int
    question_id: int
    label: str
    content: str
    result_type: str

    class Config:
        from_attributes = True
