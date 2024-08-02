from typing import Optional

from fastapi import FastAPI, Path, Query, HTTPException
from pydantic import BaseModel, Field
from stalette import status

app = FastAPI()


class Book:
    ...