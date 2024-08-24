from typing import Annotated
from pydantic import BaseModel, Field
from fastapi import FastAPI, Depends, HTTPException, status, Path
from sqlalchemy.orm import Session

import models
from models import Todos
from database import engine, SessionLocal

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

db_dependecy = Annotated[Session, Depends(get_db)]


class TodoRequest(BaseModel):
    title: str = Field(min_length=3)
    description: str = Field(min_length=3, max_length=100)
    priority: int = Field(gt=0, lt=6)
    complete: bool


@app.get("/", status_code=status.HTTP_200_OK)
async def get_all(db: db_dependecy):
    return db.query(Todos).all()


@app.get("/todo/{todo_id}", status_code=status.HTTP_200_OK)
async def get_by_id(db: db_dependecy, todo_id: int = Path(gt=0)):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()

    if todo_model:
        return todo_model

    return HTTPException(status_code=404, detail="Todo not found.")


@app.post("/todo", status_code=status.HTTP_200_OK)
async def create_todo(db: db_dependecy, todo_request: TodoRequest):
    todo_model = Todos(**todo_request.dict())

    db.add(todo_model)
    db.commit()
