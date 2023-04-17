from fastapi import APIRouter
from .endpoints import coin_collection, currency, issuing_country, mint, _types

router = APIRouter()
router.include_router(coin_collection.router, prefix="/coin-collections", tags=["Coin Collections"])
router.include_router(currency.router, prefix="/currencies", tags=["Currencies"])
router.include_router(issuing_country.router, prefix="/issuing-countries", tags=["Issuing Countries"])
router.include_router(mint.router, prefix="/mints", tags=["Mints"])
router.include_router(_types.router, prefix="/types", tags=["Types"])
