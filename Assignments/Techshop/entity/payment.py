# entity/product.py

class Product:
    def __init__(self, productname, description, price):
        self.productname = productname
        self.description = description
        self.price = price

    def register_product(self, db_connector):
        try:
            db_connector.cursor.execute("""
                INSERT INTO products (productname, description, price)
                VALUES (?, ?, ?)
            """, self.productname, self.description, self.price)
            db_connector.connection.commit()
            print("Product registered successfully.")
        except Exception as e:
            print(f"Error registering product: {e}")
