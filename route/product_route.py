from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.database import get_db
from src.controller import product_controller
import schema

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)

# get semua produk
@router.get("/", response_model=list[schema.ProductResponse])
def get_all_products(db: Session = Depends(get_db)):
    return product_controller.get_all_products(db)

# get produk berdasarkan ID
@router.get("/{product_id}", response_model=schema.ProductResponse)
def get_product(product_id: int, db: Session = Depends(get_db)):
    return product_controller.get_product(product_id, db)

# add produk 
@router.post("/", response_model=schema.ProductResponse)
def create_product(product: schema.ProductCreate, db: Session = Depends(get_db)):
    return product_controller.create_product(product, db)

# update produk berdasarkan ID
@router.put("/{product_id}", response_model=schema.ProductResponse)
def update_product(product_id: int, product: schema.ProductCreate, db: Session = Depends(get_db)):
    return product_controller.update_product(product_id, product, db)

# hapus produk berdasarkan ID
@router.delete("/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    return product_controller.delete_product(product_id, db)
