from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.db.deps import get_db
from app.crud import question_choice as crud
from app.schemas.question_choice import (
    QuestionChoiceCreate,
    QuestionChoiceUpdate,
    QuestionChoiceResponse,
)

router = APIRouter(prefix="/choices", tags=["QuestionChoices"])

@router.post("/questions/{question_id}", response_model=QuestionChoiceResponse, status_code=status.HTTP_201_CREATED)
def create_question_choice(question_id: int, request: QuestionChoiceCreate, db: Session = Depends(get_db)):
    return crud.create_choice(db, question_id, request)

@router.get("/questions/{question_id}", response_model=List[QuestionChoiceResponse])
def get_choices_by_question(question_id: int, db: Session = Depends(get_db)):
    return crud.get_choices_by_question(db, question_id)

@router.put("/{choice_id}", response_model=QuestionChoiceResponse)
def update_question_choice(choice_id: int, request: QuestionChoiceUpdate, db: Session = Depends(get_db)):
    updated = crud.update_choice(db, choice_id, request)
    if not updated:
        raise HTTPException(status_code=404, detail="Choice not found")
    return updated

@router.delete("/{choice_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_question_choice(choice_id: int, db: Session = Depends(get_db)):
    result = crud.delete_choice(db, choice_id)
    if not result:
        raise HTTPException(status_code=404, detail="Choice not found")
    return {"ok": True}
