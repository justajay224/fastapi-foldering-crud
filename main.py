from fastapi import FastAPI
from database.database import engine
from src.models import models
from route import product_route, product_non_orm_route

app = FastAPI()


models.Base.metadata.create_all(bind=engine)

app.include_router(product_route.router)
app.include_router(product_non_orm_route.router)

@app.get("/")
def home():
    return {"message": "Welcome to FastAPI CRUD Product"}
