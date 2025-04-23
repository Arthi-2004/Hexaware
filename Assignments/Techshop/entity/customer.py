class Customer:
    def __init__(self, firstname, lastname, email, phone, address, customerid=None):
        self.customerid = customerid
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.phone = phone
        self.address = address

    def get_next_customerid(self, db_connector):
        # This method is not needed when using SQL Server's identity column.
        # But keeping it for your preference.
        db_connector.cursor.execute("SELECT MAX(customerid) FROM customers")
        result = db_connector.cursor.fetchone()
        last_customerid = result[0] if result[0] else 0
        return last_customerid + 1

    def register_customer(self, db_connector):
        try:
            # Do not specify customerid in the insert query since it's auto-incremented
            db_connector.cursor.execute("""
                INSERT INTO customers (firstname, lastname, email, phone, address)
                VALUES (?, ?, ?, ?, ?)
            """, (self.firstname, self.lastname, self.email, self.phone, self.address))
            db_connector.connection.commit()

            # Fetch the last inserted customer ID (this is required as SQL Server auto-generates the ID)
            db_connector.cursor.execute("SELECT @@IDENTITY")
            self.customerid = db_connector.cursor.fetchone()[0]
            print(f"Customer registered successfully with ID: {self.customerid}")
        except Exception as e:
            print(f"Error registering customer: {e}")
