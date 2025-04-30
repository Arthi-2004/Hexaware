from util.db_util import create_connection  # Update this to use create_connection
from entity.customer import Customer
from exception.not_found_exception import NotFoundException

class CustomerDAO:
    def __init__(self):
        # Using create_connection to get the database connection
        self.connection = create_connection()

    def add_customer(self, name, email, password):
        cursor = self.connection.cursor()
        cursor.execute("""
            INSERT INTO customers (name, email, password)
            VALUES (?, ?, ?)
        """, (name, email, password))
        self.connection.commit()

    def get_customer_by_email(self, email):
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT customer_id, name, email, password
            FROM customers
            WHERE email = ?
        """, (email,))
        row = cursor.fetchone()
        if row:
            return Customer(customer_id=row[0], name=row[1], email=row[2], password=row[3])
        else:
            raise NotFoundException("Customer not found with this email")

    def get_customer_by_id(self, customer_id):
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT customer_id, name, email, password
            FROM customers
            WHERE customer_id = ?
        """, (customer_id,))
        row = cursor.fetchone()
        if row:
            return Customer(customer_id=row[0], name=row[1], email=row[2], password=row[3])
        else:
            raise NotFoundException("Customer not found with this ID")
