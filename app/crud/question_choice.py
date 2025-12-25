from sqlalchemy.orm import Session
from app.db.models.question_choice import QuestionChoice
from app.schemas.question_choice import QuestionChoiceCreate, QuestionChoiceUpdate

def create_choice(db: Session, question_id: int, request: QuestionChoiceCreate):
    db_choice = QuestionChoice(
        question_id=question_id,
        label=request.label,
        content=request.content,
        result_type=request.result_type
    )
    db.add(db_choice)
    db.commit()
    db.refresh(db_choice)
    return db_choice

def get_choices_by_question(db: Session, question_id: int):
    return db.query(QuestionChoice).filter(QuestionChoice.question_id == question_id).all()

def update_choice(db: Session, choice_id: int, request: QuestionChoiceUpdate):
    db_choice = db.query(QuestionChoice).filter(QuestionChoice.choice_id == choice_id).first()
    if not db_choice:
        return None
    
    for key, value in request.dict(exclude_unset=True).items():
        setattr(db_choice, key, value)
    
    db.commit()
    db.refresh(db_choice)
    return db_choice

def delete_choice(db: Session, choice_id: int):
    db_choice = db.query(QuestionChoice).filter(QuestionChoice.choice_id == choice_id).first()
    if not db_choice:
        return False
    db.delete(db_choice)
    db.commit()
    return True

