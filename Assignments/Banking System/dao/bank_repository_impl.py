from bean.customer import Customer  # Make sure you import Customer class

class BankRepositoryImpl:
    def __init__(self, db_conn):
        self.db_conn = db_conn
        self.cursor = db_conn.cursor()

    def create_customer(self, customer):
        try:
            query = """INSERT INTO customers (customer_id, first_name, last_name, email, phone_number, address)
                       VALUES (?, ?, ?, ?, ?, ?)"""
            self.cursor.execute(query, (
                customer.get_customer_id(),
                customer.get_first_name(),
                customer.get_last_name(),
                customer.get_email(),
                customer.get_phone_number(),
                customer.get_address()
            ))
            self.db_conn.commit()
            print(f"Customer {customer.get_first_name()} {customer.get_last_name()} created successfully.")
        except Exception as e:
            print(f"Error creating customer: {e}")

    def get_customer_by_id(self, customer_id):
        try:
            # Execute query to fetch customer by ID
            self.cursor.execute("SELECT * FROM customers WHERE customer_id = ?", (customer_id,))
            result = self.cursor.fetchone()
            if result:
                # Unpack the result and pass all columns to the Customer constructor
                return Customer(*result)  # This unpacks the tuple of columns returned by the query
            return None
        except Exception as e:
            print(f"Error fetching customer: {e}")
            return None
