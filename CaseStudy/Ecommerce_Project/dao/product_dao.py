from util.db_util import create_connection  # Update this to use create_connection
from entity.product import Product
from exception.not_found_exception import NotFoundException

class ProductDAO:
    def __init__(self):
        # Using create_connection to get the database connection
        self.connection = create_connection()

    def add_product(self, name, price, description, stockQuantity):
        cursor = self.connection.cursor()
        cursor.execute("""
            INSERT INTO products (name, price, description, stockQuantity)
            VALUES (?, ?, ?, ?)
        """, (name, price, description, stockQuantity))
        self.connection.commit()

    def get_product_by_id(self, product_id):
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT product_id, name, price, description, stockQuantity
            FROM products
            WHERE product_id = ?
        """, (product_id,))
        row = cursor.fetchone()
        if row:
            return Product(product_id=row[0], name=row[1], price=row[2], description=row[3], stockQuantity=row[4])
        else:
            raise NotFoundException("Product not found with this ID")

    def get_all_products(self):
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT product_id, name, price, description, stockQuantity
            FROM products
        """)
        rows = cursor.fetchall()
        products = []
        for row in rows:
            product = Product(product_id=row[0], name=row[1], price=row[2], description=row[3], stockQuantity=row[4])
            products.append(product)
        return products

    def delete_product(self, product_id):
        cursor = self.connection.cursor()
        cursor.execute("""
            DELETE FROM products
            WHERE product_id = ?
        """, (product_id,))
        self.connection.commit()
        print(f"✅ Product with ID {product_id} has been deleted.")
