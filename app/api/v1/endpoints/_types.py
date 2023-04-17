from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from scheme import schemas, crud
from database import get_db

router = APIRouter(prefix="/types", tags=["Types"])


@router.post("/", response_model=schemas.Type)
def create_type(type: schemas.TypeCreate, db: Session = Depends(get_db)):
    """
    Create new coin type
    """
    return crud.create_type(db, type)


@router.get("/", response_model=List[schemas.Type])
def read_types(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retrieve coin types
    """
    types = crud.get_types(db, skip=skip, limit=limit)
    return types


@router.put("/{type_id}", response_model=schemas.Type)
def update_type(type_id: int, type: schemas.TypeUpdate, db: Session = Depends(get_db)):
    """
    Update an existing coin type
    """
    existing_type = crud.get_type(db, type_id)
    if existing_type is None:
        raise HTTPException(status_code=404, detail="Type not found")
    return crud.update_type(db, type_id, type)


@router.delete("/{type_id}", response_model=schemas.Type)
def delete_type(type_id: int, db: Session = Depends(get_db)):
    """
    Delete an existing coin type
    """
    existing_type = crud.get_type(db, type_id)
    if existing_type is None:
        raise HTTPException(status_code=404, detail="Type not found")
    return crud.delete_type(db, type_id)
