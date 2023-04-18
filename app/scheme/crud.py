from sqlalchemy.orm import Session

import models
from models import CoinCollection
from models.user import User
from scheme import schemas
from scheme.user import UserCreate


def create_coin_collection(db: Session, coin_collection: schemas.CoinCollectionCreate):
    db_coin_collection = CoinCollection(**coin_collection.dict())
    db.add(db_coin_collection)
    db.commit()
    db.refresh(db_coin_collection)
    return db_coin_collection


def get_coin_collections(db: Session, skip: int = 0, limit: int = 100):
    return db.query(CoinCollection).offset(skip).limit(limit).all()


def get_coin_collection(db: Session, coin_collection_id: int):
    return (
        db.query(CoinCollection).filter(CoinCollection.id == coin_collection_id).first()
    )


def update_coin_collection(
    db: Session, coin_collection_id: int, coin_collection: schemas.CoinCollectionUpdate
):
    db_coin_collection = (
        db.query(CoinCollection).filter(CoinCollection.id == coin_collection_id).first()
    )
    if not db_coin_collection:
        return None
    update_data = coin_collection.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_coin_collection, key, value)
    db.add(db_coin_collection)
    db.commit()
    db.refresh(db_coin_collection)
    return db_coin_collection


def delete_coin_collection(db: Session, coin_collection_id: int):
    db_coin_collection = (
        db.query(CoinCollection).filter(CoinCollection.id == coin_collection_id).first()
    )
    if not db_coin_collection:
        return None
    db.delete(db_coin_collection)
    db.commit()
    return db_coin_collection


# Types
def create_type(db: Session, type: schemas.TypeCreate):
    db_type = models.Type(**type.dict())
    db.add(db_type)
    db.commit()
    db.refresh(db_type)
    return db_type


def get_types(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Type).offset(skip).limit(limit).all()


def get_type(db: Session, type_id: int):
    return db.query(models.Type).filter(models.Type.id == type_id).first()


def update_type(db: Session, type_id: int, type: schemas.TypeUpdate):
    db_type = db.query(models.Type).filter(models.Type.id == type_id).first()
    if db_type:
        db_type.name = type.name
        db.commit()
        db.refresh(db_type)
    return db_type


def delete_type(db: Session, type_id: int):
    db_type = db.query(models.Type).filter(models.Type.id == type_id).first()
    if db_type:
        db.delete(db_type)
        db.commit()
        db.flush()
    return db_type


def create_currency(db: Session, currency: schemas.CurrencyCreate):
    db_currency = models.Currency(**currency.dict())
    db.add(db_currency)
    db.commit()
    db.refresh(db_currency)
    return db_currency


def get_currencies(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Currency).offset(skip).limit(limit).all()


def get_currency(db: Session, currency_id: int):
    return db.query(models.Currency).filter(models.Currency.id == currency_id).first()


def update_currency(db: Session, currency_id: int, currency: schemas.CurrencyUpdate):
    db_currency = (
        db.query(models.Currency).filter(models.Currency.id == currency_id).first()
    )
    if db_currency:
        update_data = currency.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_currency, key, value)
        db.commit()
        db.refresh(db_currency)
    return db_currency


def delete_currency(db: Session, currency_id: int):
    db_currency = (
        db.query(models.Currency).filter(models.Currency.id == currency_id).first()
    )
    if db_currency:
        db.delete(db_currency)
        db.commit()
    return db_currency


def create_issuing_country(db: Session, issuing_country: schemas.IssuingCountryCreate):
    db_issuing_country = models.IssuingCountry(**issuing_country.dict())
    db.add(db_issuing_country)
    db.commit()
    db.refresh(db_issuing_country)
    return db_issuing_country


def get_issuing_countries(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.IssuingCountry).offset(skip).limit(limit).all()


def get_issuing_country(db: Session, issuing_country_id: int):
    return (
        db.query(models.IssuingCountry)
        .filter(models.IssuingCountry.id == issuing_country_id)
        .first()
    )


def update_issuing_country(
    db: Session, issuing_country_id: int, issuing_country: schemas.IssuingCountryUpdate
):
    db_issuing_country = (
        db.query(models.IssuingCountry)
        .filter(models.IssuingCountry.id == issuing_country_id)
        .first()
    )
    if db_issuing_country:
        update_data = issuing_country.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_issuing_country, key, value)
        db.commit()
        db.refresh(db_issuing_country)
    return db_issuing_country


def delete_issuing_country(db: Session, issuing_country_id: int):
    db_issuing_country = (
        db.query(models.IssuingCountry)
        .filter(models.IssuingCountry.id == issuing_country_id)
        .first()
    )
    if db_issuing_country:
        db.delete(db_issuing_country)
        db.commit()
    return db_issuing_country


def create_mint(db: Session, mint: schemas.MintCreate):
    db_mint = models.Mint(**mint.dict())
    db.add(db_mint)
    db.commit()
    db.refresh(db_mint)
    return db_mint


def get_mints(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Mint).offset(skip).limit(limit).all()


def get_mint(db: Session, mint_id: int):
    return db.query(models.Mint).filter(models.Mint.id == mint_id).first()


def update_mint(db: Session, mint_id: int, mint: schemas.MintUpdate):
    db_mint = db.query(models.Mint).filter(models.Mint.id == mint_id).first()
    if db_mint:
        db_mint.name = mint.name
        db_mint.country = mint.country
        db.commit()
        db.refresh(db_mint)
    return db_mint


def delete_mint(db: Session, mint_id: int):
    db_mint = db.query(models.Mint).filter(models.Mint.id == mint_id).first()
    if db_mint:
        db.delete(db_mint)
        db.commit()
    return db_mint

def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

def create_user(db: Session, user: UserCreate):
    db_user = User(username=user.username, hashed_password=user.hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user