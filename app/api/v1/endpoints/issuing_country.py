from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List


from scheme import schemas
from database import get_db
from scheme import crud

router = APIRouter(prefix="/issuing-countries", tags=["Issuing Countries"])


@router.post("/", response_model=schemas.IssuingCountry)
def create_issuing_country(
    issuing_country: schemas.IssuingCountryCreate, db: Session = Depends(get_db)
):
    """
    Create new issuing country
    """
    return crud.create_issuing_country(db, issuing_country)


@router.get("/", response_model=List[schemas.IssuingCountry])
def read_issuing_countries(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    """
    Retrieve issuing countries
    """
    issuing_countries = crud.get_issuing_countries(db, skip=skip, limit=limit)
    return issuing_countries


@router.get("/{issuing_country_id}", response_model=schemas.IssuingCountry)
def read_issuing_country(issuing_country_id: int, db: Session = Depends(get_db)):
    """
    Retrieve an issuing country by ID
    """
    issuing_country = crud.get_issuing_country(db, issuing_country_id)
    if issuing_country is None:
        raise HTTPException(status_code=404, detail="Issuing country not found")
    return issuing_country


@router.put("/{issuing_country_id}", response_model=schemas.IssuingCountry)
def update_issuing_country(
    issuing_country_id: int,
    issuing_country: schemas.IssuingCountryUpdate,
    db: Session = Depends(get_db),
):
    """
    Update an existing issuing country
    """
    existing_issuing_country = crud.get_issuing_country(db, issuing_country_id)
    if existing_issuing_country is None:
        raise HTTPException(status_code=404, detail="Issuing country not found")
    return crud.update_issuing_country(db, issuing_country_id, issuing_country)


@router.delete("/{issuing_country_id}", response_model=schemas.IssuingCountry)
def delete_issuing_country(issuing_country_id: int, db: Session = Depends(get_db)):
    """
    Delete an existing issuing country
    """
    existing_issuing_country = crud.get_issuing_country(db, issuing_country_id)
    if existing_issuing_country is None:
        raise HTTPException(status_code=404, detail="Issuing country not found")
    return crud.delete_issuing_country(db, issuing_country_id)
