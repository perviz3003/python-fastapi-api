from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from ..schemas import auth as auth_schema
from .. import database, helpers, oauth2
from ..models import User

router = APIRouter(
    tags=['Authentication']
)

@router.post(
    '/sign-in',
    response_model=auth_schema.Token,
    status_code=status.HTTP_200_OK
)
def sign_in(
        credentials: OAuth2PasswordRequestForm=Depends(),
        db: Session=Depends(database.dbc)
    ):
    db_user = db.query(User).filter(User.email == credentials.username).first()
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='Invalid credentials'
        )
    if not helpers.verify_hash(
        password=credentials.password,
        hashed_password=db_user.password
    ):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='Invalid credentials'
        )
    access_token = oauth2.create_access_token(data={'user_id': db_user.id})
    return {
        'access_token': access_token,
        'token_type': 'bearer'
    }
