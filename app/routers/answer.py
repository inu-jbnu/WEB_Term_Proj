from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.db.deps import get_db
from app.crud import answer as crud
from app.schemas.answer import AnswerCreate, AnswerResponse

router = APIRouter(prefix="/answers", tags=["Answers"])

@router.post("/", response_model=AnswerResponse, status_code=status.HTTP_201_CREATED)
def create_answer(request: AnswerCreate, db: Session = Depends(get_db)):
    return crud.create_answer(db, request)

@router.get("/test-results/{test_result_id}", response_model=List[AnswerResponse])
def get_answers_by_test_result(test_result_id: int, db: Session = Depends(get_db)):
    return crud.get_answers_by_test_result(db, test_result_id)

@router.delete("/{answer_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_answer(answer_id: int, db: Session = Depends(get_db)):
    result = crud.delete_answer(db, answer_id)
    if not result:
        raise HTTPException(status_code=404, detail="Answer not found")
    return {"ok": True}
