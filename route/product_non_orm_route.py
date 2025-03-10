from fastapi import APIRouter, Depends, HTTPException
from database.database import get_db_non_orm
from src.controller import product_non_orm_controller
import schema

router = APIRouter(
    prefix="/non-orm/products",
    tags=["Products"]
)

# get semua produk
@router.get("/", response_model=list[schema.ProductResponse])
def get_all_products(db = Depends(get_db_non_orm)):
    return product_non_orm_controller.get_all_products(db)

# get produk berdasarkan ID
@router.get("/{product_id}", response_model=schema.ProductResponse)
def get_product(product_id: int, db = Depends(get_db_non_orm)):
    return product_non_orm_controller.get_product(product_id, db)

# add produk 
@router.post("/", response_model=schema.ProductResponse)
def create_product(product: schema.ProductCreate, db = Depends(get_db_non_orm)):
    return product_non_orm_controller.create_product(product, db)

# update produk berdasarkan ID
@router.put("/{product_id}", response_model=schema.ProductResponse)
def update_product(product_id: int, product: schema.ProductCreate, db = Depends(get_db_non_orm)):
    return product_non_orm_controller.update_product(product_id, product, db)

# hapus produk berdasarkan ID
@router.delete("/{product_id}")
def delete_product(product_id: int, db = Depends(get_db_non_orm)):
    return product_non_orm_controller.delete_product(product_id, db)
