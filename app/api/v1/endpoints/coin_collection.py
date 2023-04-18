from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db


from scheme import schemas, crud
from scheme.crud import get_coin_collections, get_coin_collection

router = APIRouter(prefix="/coin-collections", tags=["Coin Collections"])


@router.post("/", response_model=schemas.CoinCollection)
def create_coin_collection(
    coin_collection: schemas.CoinCollectionCreate, db: Session = Depends(get_db)
):
    """
    Create new coin collection
    """
    return crud.create_coin_collection(db, coin_collection)


@router.get("/", response_model=List[schemas.CoinCollection])
def read_coin_collections(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    """
    Retrieve coin collections
    """
    coin_collections = get_coin_collections(db, skip=skip, limit=limit)
    return coin_collections


@router.get("/{coin_collection_id}", response_model=schemas.CoinCollection)
def read_coin_collection(coin_collection_id: int, db: Session = Depends(get_db)):
    """
    Retrieve coin collection by ID
    """
    db_coin_collection = get_coin_collection(db, coin_collection_id)
    if db_coin_collection is None:
        raise HTTPException(status_code=404, detail="Coin collection not found")
    return db_coin_collection


@router.put("/{coin_collection_id}", response_model=schemas.CoinCollection)
def update_coin_collection(
    coin_collection_id: int,
    coin_collection: schemas.CoinCollectionUpdate,
    db: Session = Depends(get_db),
):
    """
    Update an existing coin collection
    """
    existing_coin_collection = crud.get_coin_collection(db, coin_collection_id)
    if existing_coin_collection is None:
        raise HTTPException(status_code=404, detail="Coin collection not found")
    updated_data = coin_collection.dict(exclude_unset=True)
    return crud.update_coin_collection(db, coin_collection_id, updated_data)


@router.delete("/{coin_collection_id}", response_model=schemas.CoinCollection)
def delete_coin_collection(coin_collection_id: int, db: Session = Depends(get_db)):
    """
    Delete an existing coin collection
    """
    db_coin_collection = get_coin_collection(db, coin_collection_id)
    if db_coin_collection is None:
        raise HTTPException(status_code=404, detail="Coin collection not found")
    return delete_coin_collection(db, db_coin_collection=db_coin_collection)
