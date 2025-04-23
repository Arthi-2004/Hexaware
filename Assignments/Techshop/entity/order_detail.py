class OrderDetail:
    def __init__(self, orderid, productid, quantity, orderdetailid=None):
        self.orderdetailid = orderdetailid
        self.orderid = orderid
        self.productid = productid
        self.quantity = quantity

    def validate_productid(self, db_connector):
        # Check if productid exists in the products table
        db_connector.cursor.execute("SELECT COUNT(*) FROM products WHERE productid = ?", (self.productid,))
        result = db_connector.cursor.fetchone()
        if result[0] == 0:
            raise ValueError(f"Product ID {self.productid} does not exist in the products table.")

    def add_order_detail(self, db_connector):
        try:
            # Validate productid before inserting order detail
            self.validate_productid(db_connector)

            # Insert order details into the orderdetails table without specifying orderdetailid (auto-incremented)
            db_connector.cursor.execute("""
                INSERT INTO orderdetails (orderid, productid, quantity)
                VALUES (?, ?, ?)
            """, self.orderid, self.productid, self.quantity)
            db_connector.connection.commit()

            # Fetch the last inserted orderdetailid (required for auto-incremented ID)
            db_connector.cursor.execute("SELECT @@IDENTITY")
            self.orderdetailid = db_connector.cursor.fetchone()[0]
            print(f"Order detail added successfully with ID: {self.orderdetailid}")
        except Exception as e:
            print(f"Error adding order detail: {e}")
