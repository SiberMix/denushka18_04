from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List


from database import get_db
from scheme import schemas, crud

router = APIRouter(prefix="/mints", tags=["Mints"])


@router.post("/", response_model=schemas.Mint)
def create_mint(mint: schemas.MintCreate, db: Session = Depends(get_db)):
    """
    Create new mint
    """
    return crud.create_mint(db, mint)


@router.get("/", response_model=List[schemas.Mint])
def read_mints(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retrieve mints
    """
    mints = crud.get_mints(db, skip=skip, limit=limit)
    return mints


@router.get("/{mint_id}", response_model=schemas.Mint)
def read_mint(mint_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a single mint
    """
    mint = crud.get_mint(db, mint_id=mint_id)
    if mint is None:
        raise HTTPException(status_code=404, detail="Mint not found")
    return mint


@router.put("/{mint_id}", response_model=schemas.Mint)
def update_mint(mint_id: int, mint: schemas.MintUpdate, db: Session = Depends(get_db)):
    """
    Update an existing mint
    """
    existing_mint = crud.get_mint(db, mint_id=mint_id)
    if existing_mint is None:
        raise HTTPException(status_code=404, detail="Mint not found")
    return crud.update_mint(db, mint_id=mint_id, mint=mint)


@router.delete("/{mint_id}", response_model=schemas.Mint)
def delete_mint(mint_id: int, db: Session = Depends(get_db)):
    """
    Delete an existing mint
    """
    existing_mint = crud.get_mint(db, mint_id=mint_id)
    if existing_mint is None:
        raise HTTPException(status_code=404, detail="Mint not found")
    return crud.delete_mint(db, mint_id=mint_id)
