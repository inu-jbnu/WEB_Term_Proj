from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.db.deps import get_db
from app.db.models.question import Question
from app.db.models.test import Test
from app.schemas.questions import (
    QuestionCreate,
    QuestionUpdate,
    QuestionResponse,
)
from app.core.error_codes import RESOURCE_NOT_FOUND
from app.core.exception import AppException

router = APIRouter(prefix="/questions", tags=["Questions"])

# 1. 질문 생성 POST /tests/{test_id}/questions
@router.post(
    "/tests/{test_id}/questions",
    response_model=QuestionResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_question(
    test_id: int,
    request: QuestionCreate,
    db: Session = Depends(get_db),
):
    test = db.query(Test).filter(Test.test_id == test_id).first()
    if not test:
        raise AppException(**RESOURCE_NOT_FOUND, details={"test_id": test_id})

    question = Question(
        test_id=test_id,
        content=request.content,
        order_no=request.order_no,
    )

    db.add(question)
    db.commit()
    db.refresh(question)
    return question

# 2. 질문 목록 조회 GET /tests/{test_id}/questions
@router.get(
    "/tests/{test_id}/questions",
    response_model=list[QuestionResponse],
)
def get_questions_by_test(
    test_id: int,
    db: Session = Depends(get_db),
):
    return (
        db.query(Question)
        .filter(Question.test_id == test_id)
        .all()
    )

# 3. 질문 수정 PUT /questions/{id}
@router.put(
    "/{id}",
    response_model=QuestionResponse,
)
def update_question(
    id: int,
    request: QuestionUpdate,
    db: Session = Depends(get_db),
):
    question = db.query(Question).filter(Question.question_id == id).first()
    if not question:
        raise AppException(**RESOURCE_NOT_FOUND, details={"question_id": id})

    question.content = request.content
    db.commit()
    db.refresh(question)
    return question

# 4. 질문 삭제 DELETE /questions/{id}
@router.delete(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_question(
    id: int,
    db: Session = Depends(get_db),
):
    question = db.query(Question).filter(Question.question_id == id).first()
    if not question:
        raise AppException(**RESOURCE_NOT_FOUND, details={"question_id": id})

    db.delete(question)
    db.commit()
