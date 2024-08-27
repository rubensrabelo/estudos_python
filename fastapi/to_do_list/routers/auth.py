from typing import Annotated
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from pydantic import BaseModel
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordRequestForm

from models import Users
from database import SessionLocal

router = APIRouter()

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class CreateUserRequest(BaseModel):
    username: str
    email: str
    first_name: str
    last_name: str
    password: str
    role: str


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependecy = Annotated[Session, Depends(get_db)]


def authenticate_user(username: str, password: str, db):
    user = db.query(Users).filter(Users.username == username).fisrt()

    if not user or not bcrypt_context.verify(password, user.hashed_password):
        return False

    return True


@router.post("/auth", status_code=status.HTTP_201_CREATED)
async def create_user(db: db_dependecy, user_request: CreateUserRequest):
    user_model = Users(
        username=user_request.username,
        email=user_request.email,
        first_name=user_request.first_name,
        last_name=user_request.last_name,
        role=user_request.role,
        hashed_password=bcrypt_context.hash(user_request.password),
        is_active=True
    )

    db.add(user_model)
    db.commit()


@router.post("/token")
async def login_for_acess_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: db_dependecy
):
    user = authenticate_user(form_data.username, form_data.password, db)

    if not user:
        return "Failed Authentication"

    return "Sucessful Authentication"
