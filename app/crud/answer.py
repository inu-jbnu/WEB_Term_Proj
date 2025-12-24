from sqlalchemy.orm import Session
from app.db.models.answer import Answer
from app.schemas.answer import AnswerCreate

def create_answer(db: Session, answer: AnswerCreate) -> Answer:
    db_answer = Answer(
        test_result_id=answer.test_result_id,
        question_id=answer.question_id,
        choice_id=answer.choice_id
    )
    db.add(db_answer)
    db.commit()
    db.refresh(db_answer)
    return db_answer

def get_answers_by_test_result(db: Session, test_result_id: int):
    return db.query(Answer).filter(Answer.test_result_id == test_result_id).all()

def get_answer(db: Session, answer_id: int):
    return db.query(Answer).filter(Answer.answer_id == answer_id).first()

def delete_answer(db: Session, answer_id: int):
    db_answer = get_answer(db, answer_id)
    if not db_answer:
        return None
    db.delete(db_answer)
    db.commit()
    return True
