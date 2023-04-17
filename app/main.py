from fastapi import FastAPI
from api.v1.endpoints import coin_collection, currency, issuing_country, mint, _types
from database import engine, Base


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(coin_collection.router, prefix="/v1")
app.include_router(currency.router, prefix="/v1")
app.include_router(issuing_country.router, prefix="/v1")
app.include_router(mint.router, prefix="/v1")
app.include_router(_types.router, prefix="/v1")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)

