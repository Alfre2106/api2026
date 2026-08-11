from psycopg2.extras import RealDictCursor
from database.connection import get_db_connection
from schemas.product_schema import ProductCreate, ProductUpdate

class ProductService:

    @staticmethod
    def get_all():
        conn = get_db_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute("SELECT id, nombre, precio FROM productos;")
        products = cursor.fetchall()
        cursor.close()
        conn.close()
        return products

    @staticmethod
    def get_by_id(product_id: int):
        conn = get_db_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute("SELECT id, nombre, precio FROM productos WHERE id = %s;", (product_id,))
        product = cursor.fetchone()
        cursor.close()
        conn.close()
        return product

    @staticmethod
    def create(product_data: ProductCreate):
        conn = get_db_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute(
            "INSERT INTO productos (nombre, precio) VALUES (%s, %s) RETURNING id, nombre, precio;",
            (product_data.nombre, product_data.precio)
        )
        new_product = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()
        return new_product

    @staticmethod
    def update(product_id: int, product_data: ProductUpdate):
        product = ProductService.get_by_id(product_id)
        if not product:
            return None

        updated_name = product_data.nombre if product_data.nombre is not None else product['nombre']
        updated_price = product_data.precio if product_data.precio is not None else product['precio']

        conn = get_db_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute(
            "UPDATE productos SET nombre = %s, precio = %s WHERE id = %s RETURNING id, nombre, precio;",
            (updated_name, updated_price, product_id)
        )
        updated_product = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()
        return updated_product

    @staticmethod
    def delete(product_id: int):
        product = ProductService.get_by_id(product_id)
        if not product:
            return False

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM productos WHERE id = %s;", (product_id,))
        conn.commit()
        cursor.close()
        conn.close()
        return True