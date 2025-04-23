class Order:
    def __init__(self, customerid, orderdate, totalamount, orderid=None):
        self.orderid = orderid
        self.customerid = customerid
        self.orderdate = orderdate
        self.totalamount = totalamount

    def place_order(self, db_connector):
        try:
            # Insert new order without specifying orderid (because it's auto-incremented)
            db_connector.cursor.execute("""
                INSERT INTO orders (customerid, orderdate, totalamount)
                VALUES (?, ?, ?)
            """, (self.customerid, self.orderdate, self.totalamount))
            db_connector.connection.commit()

            # Fetch the last inserted order ID (this is required as SQL Server auto-generates the ID)
            db_connector.cursor.execute("SELECT @@IDENTITY")
            self.orderid = db_connector.cursor.fetchone()[0]
            print(f"Order placed successfully with ID: {self.orderid}")
        except Exception as e:
            print(f"Error placing order: {e}")
