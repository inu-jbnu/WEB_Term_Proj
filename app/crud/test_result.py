from sqlalchemy.orm import Session
from app.db.models.test_result import TestResult
from app.schemas.test_result import TestResultCreate, TestResultUpdate

def create_test_result(db: Session, data: TestResultCreate) -> TestResult:
    db_result = TestResult(**data.dict())
    db.add(db_result)
    db.commit()
    db.refresh(db_result)
    return db_result

def get_test_result(db: Session, test_result_id: int) -> TestResult:
    return db.query(TestResult).filter(TestResult.test_result_id == test_result_id).first()

def get_all_test_results(db: Session):
    return db.query(TestResult).all()

def update_test_result(db: Session, test_result_id: int, data: TestResultUpdate) -> TestResult:
    db_result = get_test_result(db, test_result_id)
    if not db_result:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(db_result, key, value)
    db.commit()
    db.refresh(db_result)
    return db_result

def delete_test_result(db: Session, test_result_id: int) -> bool:
    db_result = get_test_result(db, test_result_id)
    if not db_result:
        return False
    db.delete(db_result)
    db.commit()
    return True
