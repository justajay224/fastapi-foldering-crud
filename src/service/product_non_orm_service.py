from src.repository import product_non_orm_repository
import schema

# liat All produk
def get_all_products(db):
    return product_non_orm_repository.get_all_products(db)

# liat produk berdasarkan ID
def get_product(db, product_id: int):
    return product_non_orm_repository.get_product_by_id(db, product_id)

# Menambah produk baru
def create_new_product(db, product: schema.ProductCreate):
    return product_non_orm_repository.create_product(db, product)

# update produk berdasarkan ID
def update_existing_product(db, product_id: int, product: schema.ProductCreate):
    return product_non_orm_repository.update_product(db, product_id, product)

# hapus produk berdasarkan ID
def delete_existing_product(db, product_id: int):
    return product_non_orm_repository.delete_product(db, product_id)
