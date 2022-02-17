from sqlalchemy.orm import Session
from ..schemas import user as user_schema
from ..models import User

def create_user(
        user: user_schema.UserCreate,
        db: Session
    ):
    new_user = User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user_by_email(
        email: str,
        db: Session
    ):
    db_user = db.query(User).filter(User.email == email).first()
    if db_user is None:
        return None
    return db_user

def get_user(
        user_id: int,
        db: Session
    ):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        return None
    return db_user

def update_user(
        user_id: int,
        user: user_schema.UserUpdate,
        db: Session
    ):
    db_user = db.query(User).filter(User.id == user_id)
    db_user.update(user.dict(), synchronize_session=False)
    db.commit()
    return db_user.first()

def delete_user(
        user_id: int,
        db: Session
    ):
    db_user = db.query(User).filter(User.id == user_id)
    db_user.delete(synchronize_session=False)
    db.commit()
    return None
