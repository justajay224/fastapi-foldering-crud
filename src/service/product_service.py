from sqlalchemy.orm import Session
from src.repository import product_repository
import schema

# lait All produk
def get_all_products(db: Session):
    return product_repository.get_products(db)

# liat produk berdasarkan ID
def get_product(db: Session, product_id: int):
    return product_repository.get_product_by_id(db, product_id)

# Menambah produk baru
def create_new_product(db: Session, product: schema.ProductCreate):
    return product_repository.create_product(db, product)

# update produk berdasarkan ID
def update_existing_product(db: Session, product_id: int, product: schema.ProductCreate):
    return product_repository.update_product(db, product_id, product)

# hapus produk berdasarkan ID
def delete_existing_product(db: Session, product_id: int):
    return product_repository.delete_product(db, product_id)
