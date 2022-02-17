from fastapi import APIRouter, status, Depends, HTTPException, Response
from sqlalchemy.orm import Session
from ..schemas import user as user_schema
from ..crud import users as users_crud
from ..database import dbc
from .. import helpers, oauth2

router = APIRouter(
    prefix='/users',
    tags=['Users']
)

@router.post(
    path='/',
    response_model=user_schema.User,
    status_code=status.HTTP_201_CREATED
)
def create_user(
        user: user_schema.UserCreate,
        db: Session=Depends(dependency=dbc)
    ):
    db_user = users_crud.get_user_by_email(email=user.email, db=db)
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='User already exists'
        )
    hashed_password = helpers.get_hash(password=user.password)
    user.password = hashed_password
    return users_crud.create_user(user=user, db=db)

@router.get(
    path='/{user_id}/',
    response_model=user_schema.User,
    status_code=status.HTTP_200_OK
)
def get_user_info(
        user_id: int,
        db: Session=Depends(dependency=dbc),
        current_user: object=Depends(oauth2.get_current_user)
    ):
    if current_user.id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='Forbidden'
        )
    db_user = users_crud.get_user(user_id=user_id, db=db)
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User not found'
        )
    return db_user

@router.put(
    path='/{user_id}/',
    response_model=user_schema.User,
    status_code=status.HTTP_200_OK
)
def change_password(
        user_id: int,
        user: user_schema.UserUpdate,
        db: Session=Depends(dependency=dbc),
        current_user: object=Depends(oauth2.get_current_user)
    ):
    if current_user.id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='Forbidden'
        )
    db_user = users_crud.get_user(user_id=user_id, db=db)
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User not found'
        )
    hashed_password = helpers.get_hash(password=user.password)
    user.password = hashed_password
    return users_crud.update_user(user_id=user_id, user=user, db=db)

@router.delete(
    path='/{user_id}/',
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_user(
        user_id: int,
        db: Session=Depends(dependency=dbc),
        current_user: object=Depends(oauth2.get_current_user)
    ):
    if current_user.id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='Forbidden'
        )
    db_user = users_crud.get_user(user_id=user_id, db=db)
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User not found'
        )
    return Response(status_code=status.HTTP_204_NO_CONTENT)
