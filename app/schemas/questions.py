# app/schemas/questions.py
from pydantic import BaseModel

class QuestionCreate(BaseModel):
    content: str

class QuestionUpdate(BaseModel):
    content: str

class QuestionResponse(BaseModel):
    question_id: int
    content: str

    class Config:
        from_attributes = True
