# app/schemas/questions.py
from pydantic import BaseModel

class QuestionCreate(BaseModel):
    content: str
    order_no: int  # <-- 이 줄을 추가하세요

class QuestionUpdate(BaseModel):
    content: str
    order_no: int | None = None  # (선택사항) 업데이트 때도 필요할 수 있으니 넣어두면 좋습니다

class QuestionResponse(BaseModel):
    question_id: int
    content: str
    order_no: int  # <-- 결과창에서도 보이게 여기도 추가하세요

    class Config:
        from_attributes = True

