from sqlalchemy.orm import Session
from app.db.models.result_type import ResultType
from app.schemas.result_type import ResultTypeCreate, ResultTypeUpdate

def create_result_type(db: Session, data: ResultTypeCreate) -> ResultType:
    db_result = ResultType(**data.dict())
    db.add(db_result)
    db.commit()
    db.refresh(db_result)
    return db_result

def get_result_type(db: Session, result_type_id: str) -> ResultType:
    return db.query(ResultType).filter(ResultType.result_type == result_type_id).first()

def get_all_result_types(db: Session):
    return db.query(ResultType).all()

def update_result_type(db: Session, result_type_id: str, data: ResultTypeUpdate) -> ResultType:
    db_result = get_result_type(db, result_type_id)
    if not db_result:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(db_result, key, value)
    db.commit()
    db.refresh(db_result)
    return db_result

def delete_result_type(db: Session, result_type_id: str) -> bool:
    db_result = get_result_type(db, result_type_id)
    if not db_result:
        return False
    db.delete(db_result)
    db.commit()
    return True
