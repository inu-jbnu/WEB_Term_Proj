# app/crud/questions.py
from sqlalchemy.orm import Session
from app.db.models.question import Question
from app.schemas.questions import QuestionCreate, QuestionUpdate

def get_question(db: Session, question_id: int) -> Question | None:
    return db.query(Question).filter(Question.question_id == question_id).first()

def get_questions_by_test(db: Session, test_id: int) -> list[Question]:
    return db.query(Question).filter(Question.test_id == test_id).all()

def create_question(db: Session, test_id: int, question_data: QuestionCreate) -> Question:
    question = Question(
        test_id=test_id,
        content=question_data.content
    )
    db.add(question)
    db.commit()
    db.refresh(question)
    return question

def update_question(db: Session, question_id: int, question_data: QuestionUpdate) -> Question | None:
    question = get_question(db, question_id)
    if question:
        question.content = question_data.content
        db.commit()
        db.refresh(question)
    return question

def delete_question(db: Session, question_id: int) -> bool:
    question = get_question(db, question_id)
    if question:
        db.delete(question)
        db.commit()
        return True
    return False
