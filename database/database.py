import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2 
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# Koneksi untuk ORM menggunakan SQLAlchemy
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Koneksi untuk non-ORM 
def get_db_non_orm():
    # Mengambil variabel koneksi dari file .env
    host = os.getenv("DB_HOST")  
    user = os.getenv("DB_USER") 
    password = os.getenv("DB_PASSWORD")  
    database = os.getenv("DB_NAME") 

    # Membuat koneksi ke database
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    return connection
