from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import timedelta

from openapi_server.apis.grocery_items_api import router as GroceryItemsApiRouter
from openapi_server.auth.auth import create_access_token, decode_access_token
from openapi_server.auth.models import users
from openapi_server.auth.password import hash_password, verify_password
from openapi_server.impl.database import database, metadata, engine

from sqlalchemy import select, insert
from databases import Database

app = FastAPI(
    title="Grocery List Management API",
    description="A simple REST API for managing a grocery shopping list, designed for student term projects.",
    version="1.0.0",
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

@app.on_event("startup")
async def startup():
    metadata.create_all(engine)
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.post("/register")
async def register(username: str, password: str, repeated_password: str):
    if not username or not password or not repeated_password:
        raise HTTPException(status_code=400, detail="All fields are required")

    if password != repeated_password:
        raise HTTPException(status_code=400, detail="Passwords do not match")

    query = select(users).where(users.c.username == username)
    existing_user = await database.fetch_one(query)
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    hashed = hash_password(password)
    insert_query = insert(users).values(
        username=username,
        hashed_password=hashed,
        role="user"
    )
    await database.execute(insert_query)

    return {"message": "Account created", "username": username}


@app.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    query = select(users).where(users.c.username == form_data.username)
    user = await database.fetch_one(query)

    if not user or not verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(status_code=400, detail="Invalid username or password")

    access_token = create_access_token(
        data={"sub": user["username"]}, expires_delta=timedelta(minutes=30)
    )
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/protected")
async def protected(token: str = Depends(oauth2_scheme)):
    user_data = decode_access_token(token)
    if not user_data:
        raise HTTPException(status_code=401, detail="Invalid token")
    return {"message": f"Welcome {user_data['sub']}!"}


app.include_router(GroceryItemsApiRouter)
