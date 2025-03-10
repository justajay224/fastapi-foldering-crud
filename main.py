from fastapi import FastAPI
from database.database import engine
from src.models import models
from route.index import all_routers 

app = FastAPI()

# Database setup 
models.Base.metadata.create_all(bind=engine)

# Include semua router sekaligus
for router in all_routers:
    app.include_router(router)

# Home route
@app.get("/")
def home():
    return {"message": "Welcome to FastAPI CRUD Product"}