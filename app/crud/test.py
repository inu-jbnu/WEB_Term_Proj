# app/crud/test.py
from sqlalchemy.orm import Session
from app.db.models.test import Test
from app.schemas.test import TestCreate, TestUpdate

def create_test(db: Session, test_in: TestCreate) -> Test:
    db_test = Test(
        title=test_in.title,
        description=test_in.description
    )
    db.add(db_test)
    db.commit()
    db.refresh(db_test)
    return db_test

def get_test(db: Session, test_id: int) -> Test | None:
    return db.query(Test).filter(Test.test_id == test_id).first()

def get_tests(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Test).offset(skip).limit(limit).all()

def update_test(db: Session, test_id: int, test_in: TestUpdate) -> Test | None:
    db_test = db.query(Test).filter(Test.test_id == test_id).first()
    if not db_test:
        return None
    if test_in.title is not None:
        db_test.title = test_in.title
    if test_in.description is not None:
        db_test.description = test_in.description
    db.commit()
    db.refresh(db_test)
    return db_test

def delete_test(db: Session, test_id: int) -> bool:
    db_test = db.query(Test).filter(Test.test_id == test_id).first()
    if not db_test:
        return False
    db.delete(db_test)
    db.commit()
    return True
