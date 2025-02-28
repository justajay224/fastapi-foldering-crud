from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.service import product_service
from src.repository import product_repository
import schema

# All produk
def get_all_products(db: Session):
    products = product_service.get_all_products(db)
    return products

# produk berdasarkan ID
def get_product(product_id: int, db: Session):
    product = product_service.get_product(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

# Add produk + Validasi ID unik dan tipe data
def create_product(product: schema.ProductCreate, db: Session):
    # nama produk tidak kosong
    if not product.name or product.name.strip() == "":
        raise HTTPException(status_code=400, detail="Product name cannot be empty")

    # Harga harus lebih dari 0
    if product.price <= 0:
        raise HTTPException(status_code=400, detail="Price must be greater than zero")
    
    # Validasi: Stok tidak boleh negatif
    if product.stock < 0:
        raise HTTPException(status_code=400, detail="Stock cannot be negative")

    # Validasi: Pastikan produk dengan nama yang sama belum ada di database
    existing_product = product_repository.get_product_by_name(db, product.name)
    if existing_product:
        raise HTTPException(status_code=400, detail="Product with this name already exists")

    return product_service.create_new_product(db, product)

# gupdate produk berdasarkan ID
def update_product(product_id: int, product: schema.ProductCreate, db: Session):
    existing_product = product_repository.get_product_by_id(db, product_id)
    if not existing_product:
        raise HTTPException(status_code=404, detail="Product not found")

    # produk tidak kosong
    if not product.name or product.name.strip() == "":
        raise HTTPException(status_code=400, detail="Product name cannot be empty")

    # Harga harus lebih dari 0
    if product.price <= 0:
        raise HTTPException(status_code=400, detail="Price must be greater than zero")

    updated_product = product_service.update_existing_product(db, product_id, product)
    return updated_product

# Menghapus produk berdasarkan ID
def delete_product(product_id: int, db: Session):
    existing_product = product_repository.get_product_by_id(db, product_id)
    if not existing_product:
        raise HTTPException(status_code=404, detail="Product not found")

    deleted_product = product_service.delete_existing_product(db, product_id)
    return {"message": "Product deleted successfully"}
