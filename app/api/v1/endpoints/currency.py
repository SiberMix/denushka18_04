from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from scheme import schemas
from database import get_db
from scheme.crud import get_currencies, get_currency

router = APIRouter(prefix="/currencies", tags=["Currencies"])


@router.post("/", response_model=schemas.Currency)
def create_currency(currency: schemas.CurrencyCreate, db: Session = Depends(get_db)):
    """
    Create new currency
    """
    return create_currency(db, currency)


@router.get("/", response_model=List[schemas.Currency])
def read_currencies(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retrieve currencies
    """
    currencies = get_currencies(db, skip=skip, limit=limit)
    return currencies


@router.get("/{currency_id}", response_model=schemas.Currency)
def read_currency(currency_id: int, db: Session = Depends(get_db)):
    """
    Retrieve currency by ID
    """
    db_currency = get_currency(db, currency_id)
    if db_currency is None:
        raise HTTPException(status_code=404, detail="Currency not found")
    return db_currency


@router.put("/{currency_id}", response_model=schemas.Currency)
def update_currency(
    currency_id: int, currency: schemas.CurrencyUpdate, db: Session = Depends(get_db)
):
    """
    Update an existing currency
    """
    existing_currency = get_currency(db, currency_id)
    if existing_currency is None:
        raise HTTPException(status_code=404, detail="Currency not found")
    return update_currency(db, currency_id, currency)


@router.delete("/{currency_id}", response_model=schemas.Currency)
def delete_currency(currency_id: int, db: Session = Depends(get_db)):
    """
    Delete an existing currency
    """
    existing_currency = get_currency(db, currency_id)
    if existing_currency is None:
        raise HTTPException(status_code=404, detail="Currency not found")
    return delete_currency(db, currency_id)
