from fastapi import FastAPI
from database.database import engine
from src.models import models
from route.index import include_routers

app = FastAPI()

# Database setup 
models.Base.metadata.create_all(bind=engine)

include_routers(app)

# Home route
# @app.get("/")
# def home():
#     return {"message": "FastAPI CRUD Produk"}