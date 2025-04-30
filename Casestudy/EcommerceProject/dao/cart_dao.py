from util.db_util import create_connection  # Ensure create_connection is working correctly
from entity.cart import Cart
from exception.not_found_exception import NotFoundException

class CartDAO:
    def __init__(self):
        # Using create_connection to get the database connection
        self.connection = create_connection()

    def add_cart(self, customer_id, product_id, quantity):
        # Ensure that no incorrect symbols like '#' are present in SQL queries
        cursor = self.connection.cursor()
        cursor.execute("""
            INSERT INTO cart (customer_id, product_id, quantity)  -- Make sure the table is 'cart', not 'carts'
            VALUES (?, ?, ?)
        """, (customer_id, product_id, quantity))
        self.connection.commit()

    def get_cart_by_customer_id(self, customer_id):
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT cart_id, customer_id, product_id, quantity
            FROM cart  -- Correct table name should be 'cart'
            WHERE customer_id = ?
        """, (customer_id,))
        rows = cursor.fetchall()
        carts = []

        for row in rows:
            carts.append(Cart(cart_id=row[0], customer_id=row[1], product_id=row[2], quantity=row[3]))

        if carts:
            return carts
        else:
            raise NotFoundException("No cart found for this customer ID")

    def delete_cart_item(self, cart_id):
        cursor = self.connection.cursor()
        cursor.execute("""
            DELETE FROM cart WHERE cart_id = ?  -- Correct table name should be 'cart'
        """, (cart_id,))
        self.connection.commit()

    def update_cart_quantity(self, cart_id, quantity):
        cursor = self.connection.cursor()
        cursor.execute("""
            UPDATE cart  -- Correct table name should be 'cart'
            SET quantity = ?
            WHERE cart_id = ?
        """, (quantity, cart_id))
        self.connection.commit()
    def view_cart(self, customer_id):
        # Method to view all cart items for a specific customer
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT cart_id, customer_id, product_id, quantity
            FROM cart
            WHERE customer_id = ?
        """, (customer_id,))
        rows = cursor.fetchall()
        if rows:
            carts = []
            for row in rows:
                carts.append(Cart(cart_id=row[0], customer_id=row[1], product_id=row[2], quantity=row[3]))
            return carts
        else:
            raise NotFoundException("No cart found for this customer ID")
    def clear_cart(self, customer_id):
        # Deletes all items from the cart for a given customer_id
        cursor = self.connection.cursor()
        cursor.execute("""
            DELETE FROM cart
            WHERE customer_id = ?
        """, (customer_id,))
        self.connection.commit()
        print(f"Cart for customer {customer_id} has been cleared.")