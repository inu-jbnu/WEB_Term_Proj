from pydantic import BaseModel
from datetime import datetime

class AnswerCreate(BaseModel):
    test_result_id: int
    question_id: int
    choice_id: int

class AnswerResponse(BaseModel):
    answer_id: int
    test_result_id: int
    question_id: int
    choice_id: int

    class Config:
        from_attributes = True
