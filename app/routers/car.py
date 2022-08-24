from fastapi import APIRouter, HTTPException, Request
from app.cruds.CrudOperations import Operations
from connection.models import Car
from schemas.car import CarIn, CarOut, CarOutExplicit, CarParams
from typing import List, Optional

router = APIRouter(tags=["CarOut"], prefix="/car")
crud = Operations(Car)
