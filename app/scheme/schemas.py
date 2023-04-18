from typing import List

from pydantic import BaseModel


class CoinCollectionBase(BaseModel):
    description: str
    nominal_value: str
    year_of_issue: str
    serial_number: str


class CoinCollectionCreate(CoinCollectionBase):
    type_id: int
    currency_id: int
    mint_id: int
    issuing_country_id: int


class CoinCollection(CoinCollectionBase):
    id: int
    type_id: int
    currency_id: int
    mint_id: int
    issuing_country_id: int

    class Config:
        orm_mode = True


class CoinCollectionUpdate(BaseModel):
    description: str


class TypeBase(BaseModel):
    name: str


class TypeCreate(TypeBase):
    pass


class TypeUpdate(TypeBase):
    pass


class Type(TypeBase):
    id: int
    coin_collections: List[CoinCollection] = []

    class Config:
        orm_mode = True


class CurrencyBase(BaseModel):
    name: str


class CurrencyCreate(CurrencyBase):
    name: str


class CurrencyUpdate(CurrencyBase):
    name: str


class Currency(CurrencyBase):
    id: int

    class Config:
        orm_mode = True


class CurrencyWithCollections(Currency):
    coin_collections: List["CoinCollection"] = []

    class Config:
        orm_mode = True


class MintBase(BaseModel):
    name: str
    country: str


class MintCreate(MintBase):
    pass
class MintUpdate(MintBase):
    pass


class Mint(MintBase):
    id: int
    coin_collections: List[CoinCollection] = []

    class Config:
        orm_mode = True


class IssuingCountryBase(BaseModel):
    name: str


class IssuingCountryCreate(IssuingCountryBase):
    pass


class IssuingCountry(IssuingCountryBase):
    id: int
    coin_collections: List[CoinCollection] = []

    class Config:
        orm_mode = True


class IssuingCountryUpdate(IssuingCountryBase):
    pass
