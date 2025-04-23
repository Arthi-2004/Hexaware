class Product:
    def __init__(self, productname, description, price, productid=None):
        self.productid = productid
        self.productname = productname
        self.description = description
        self.price = price

    def get_next_productid(self, db_connector):
        # This method is not needed when using SQL Server's identity column.
        # Keeping it for your reference, but it's unnecessary in practice.
        db_connector.cursor.execute("SELECT MAX(productid) FROM products")
        result = db_connector.cursor.fetchone()
        return result[0] + 1 if result[0] is not None else 1

    def register_product(self, db_connector):
        try:
            # Do not specify productid in the insert query since it's auto-incremented
            db_connector.cursor.execute("""
                INSERT INTO products (productname, description, price)
                VALUES (?, ?, ?)
            """, (self.productname, self.description, self.price))
            db_connector.connection.commit()

            # Fetch the last inserted product ID (this is required as SQL Server auto-generates the ID)
            db_connector.cursor.execute("SELECT @@IDENTITY")
            self.productid = db_connector.cursor.fetchone()[0]
            print(f"Product registered successfully with ID: {self.productid}")
        except Exception as e:
            print(f"Error registering product: {e}")
