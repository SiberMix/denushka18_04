from datetime import datetime, timedelta

from fastapi import FastAPI, Depends, Form, Request
from fastapi.responses import HTMLResponse
from jose import jwt

from api.v1.endpoints import coin_collection, currency, issuing_country, mint, _types

from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from database import engine, Base, get_db
from sqlalchemy.orm import Session

from models.user import User

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(coin_collection.router, prefix="/v1")
app.include_router(currency.router, prefix="/v1")
app.include_router(issuing_country.router, prefix="/v1")
app.include_router(mint.router, prefix="/v1")
app.include_router(_types.router, prefix="/v1")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})


@app.get("/register", response_class=HTMLResponse)
async def register_get(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})


@app.post("/register", response_class=HTMLResponse)
async def register_post(
        request: Request,
        db: Session = Depends(get_db),
        username: str = Form(...),
        password: str = Form(...),
):
    user = db.query(User).filter(User.username == username).first()
    if user:
        return templates.TemplateResponse(
            "register.html", {"request": request, "message": "User already exists"}
        )
    else:
        new_user = User(username=username, password=password)
        db.add(new_user)
        db.commit()

        return templates.TemplateResponse(
            "register.html", {"request": request, "message": "Registration successful"}
        )


@app.get("/login", response_class=HTMLResponse)
async def login_get(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@app.post("/login", response_class=HTMLResponse)
async def login_post(
        request: Request,
        db: Session = Depends(get_db),
        username: str = Form(...),
        password: str = Form(...),
):
    user = db.query(User).filter(User.username == username).first()
    if not user or user.password != password:
        return templates.TemplateResponse(
            "login.html",
            {
                "request": request,
                "message": "Invalid username or password",
                "image_path": "nopass.jpg",
            },
        )

    # Generate token
    token_expiration = datetime.utcnow() + timedelta(hours=1)  # token expires in 1 hour
    token_payload = {"sub": user.username, "exp": token_expiration}
    token = jwt.encode(token_payload, "secret_key", algorithm="HS256")

    # Update user's token field in the database
    user.token = token
    db.commit()

    name = user.username
    return templates.TemplateResponse(
        "dashboard.html", {"request": request, "name": name, "token": token}
    )


if __name__ == "__main__":
    import uvicorn
    from fastapi import Depends
    from sqlalchemy.orm import Session
    from database import get_db

    uvicorn.run(app, host="0.0.0.0", port=8000)
