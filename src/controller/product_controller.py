from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.service import product_service
from src.repository import product_repository
import schema

# get All produk
def get_all_products(db: Session):
    products = product_service.get_all_products(db)
    return products

# get produk berdasarkan ID
def get_product(product_id: int, db: Session):
    product = product_service.get_product(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Produk tidak ditemukan")
    return product

# Add produk + Validasi 
def create_product(product: schema.ProductCreate, db: Session):
    # nama produk tidak kosong
    if not product.name or product.name.strip() == "":
        raise HTTPException(status_code=400, detail="Nama produk tidak boleh kosong")

    # Harga lebih dari 0
    if product.price <= 0:
        raise HTTPException(status_code=400, detail="Harga harus lebih dari 0")
    
    # Stok tidak negatif
    if product.stock < 0:
        raise HTTPException(status_code=400, detail="Stok tidak boleh kurang dari 0")

    # Cek nama
    existing_product = product_repository.get_product_by_name(db, product.name)
    if existing_product:
        raise HTTPException(status_code=400, detail="Nama produk telah digunakan")

    return product_service.create_new_product(db, product)

# gupdate produk berdasarkan ID
def update_product(product_id: int, product: schema.ProductCreate, db: Session):
    existing_product = product_repository.get_product_by_id(db, product_id)
    if not existing_product:
        raise HTTPException(status_code=404, detail="Produk tidak ditemukan")

    # nama tidak kosong
    if not product.name or product.name.strip() == "":
        raise HTTPException(status_code=400, detail="Nama tidak boleh kosong")

    # Harga harus lebih dari 0
    if product.price <= 0:
        raise HTTPException(status_code=400, detail="Harga harus lebih dari 0")
    
    if product.stock < 0:
        raise HTTPException(status_code=400, detail="Stok tidak boleh kurang dari 0")

    updated_product = product_service.update_existing_product(db, product_id, product)
    return updated_product

# Menghapus produk berdasarkan ID
def delete_product(product_id: int, db: Session):
    existing_product = product_repository.get_product_by_id(db, product_id)
    if not existing_product:
        raise HTTPException(status_code=404, detail="Produk tidak ditemukan")

    deleted_product = product_service.delete_existing_product(db, product_id)
    return {"message": "produk berhasil di hapus"}
