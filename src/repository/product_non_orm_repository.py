import psycopg2
from psycopg2.extras import DictCursor
from schema import ProductCreate

# mendapatkan semua produk
def get_all_products(db):
    cursor = db.cursor(cursor_factory=DictCursor)
    cursor.execute("SELECT id, name, category, price, stock FROM products")
    products = cursor.fetchall()
    
    # Konversi Decimal ke float
    converted_products = []
    for product in products:
        product_dict = dict(product)
        product_dict["price"] = float(product_dict["price"])
        converted_products.append(product_dict)
    
    cursor.close()
    return converted_products

# mencari berdasarkan id produk
def get_product_by_id(db, product_id: int):
    cursor = db.cursor(cursor_factory=DictCursor)
    cursor.execute(
        "SELECT id, name, category, price, stock FROM products WHERE id = %s",
        (product_id,)
    )
    product = cursor.fetchone()
    
    if product:
        product = dict(product)
        product["price"] = float(product["price"])
    
    cursor.close()
    return product

# mencari berdasarkan nama produk
def get_product_by_name(db, name: str):
    cursor = db.cursor(cursor_factory=DictCursor)
    cursor.execute("SELECT * FROM products WHERE name = %s", (name,))
    product = cursor.fetchone()
    cursor.close()
    return product

# add produk baru
def create_product(db, product: ProductCreate):
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO products (name, category, price, stock) VALUES (%s, %s, %s, %s) RETURNING id",
        (product.name, product.category, product.price, product.stock)
    )
    inserted_id = cursor.fetchone()[0]  # Dapatkan ID dari hasil RETURNING
    db.commit()
    cursor.close()
    return {**product.dict(), "id": inserted_id} 

# update
def update_product(db, product_id: int, product: ProductCreate):
    cursor = db.cursor()
    cursor.execute(
        "UPDATE products SET name = %s, category = %s, price = %s, stock = %s WHERE id = %s RETURNING id, name, category, price, stock",
        (product.name, product.category, product.price, product.stock, product_id)
    )
    updated_product = cursor.fetchone()
    db.commit()
    cursor.close()
    
    # Konversi sesuai schema
    return {
        "id": product_id,
        "name": updated_product[1],
        "category": updated_product[2],
        "price": updated_product[3],
        "stock": updated_product[4]
    }

# hapus
def delete_product(db, product_id: int):
    cursor = db.cursor()
    cursor.execute("DELETE FROM products WHERE id = %s", (product_id,))
    db.commit()
    cursor.close()
    return {"message": "Produk berhasil dihapus"}
