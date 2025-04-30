from util.db_util import create_connection  # Update this to use create_connection
from entity.order import Order
from exception.not_found_exception import NotFoundException
from entity.order_item import OrderItem  # Assuming you have this class to represent order items

class OrderDAO:
    def __init__(self):
        # Using create_connection to get the database connection
        self.connection = create_connection()

    def add_order(self, customer_id, total_price, shipping_address):
        """
        Adds a new order to the database.

        :param customer_id: The ID of the customer placing the order.
        :param total_price: The total price of the order.
        :param shipping_address: The shipping address for the order.
        """
        cursor = self.connection.cursor()
        cursor.execute("""
            INSERT INTO orders (customer_id, total_price, shipping_address)
            VALUES (?, ?, ?)
        """, (customer_id, total_price, shipping_address))
        self.connection.commit()

    def get_order_by_customer_id(self, customer_id):
        """
        Retrieves an order based on the customer ID.

        :param customer_id: The ID of the customer whose order is to be fetched.
        :return: An Order object.
        :raises NotFoundException: If no order is found for the given customer ID.
        """
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT order_id, customer_id, total_price, shipping_address
            FROM orders
            WHERE customer_id = ?
        """, (customer_id,))
        row = cursor.fetchone()
        if row:
            return Order(order_id=row[0], customer_id=row[1], total_price=row[2], shipping_address=row[3])
        else:
            raise NotFoundException("Order not found for this customer ID")

    def create_order(self, order, order_items):
        """
        Creates a new order and inserts order items into the order_items table.

        :param order: The Order object containing order details.
        :param order_items: A list of OrderItem objects to be associated with the order.
        :return: The order_id of the newly created order.
        """
        cursor = self.connection.cursor()

        # Insert the main order details into the 'orders' table
        cursor.execute("""
            INSERT INTO orders (customer_id, total_price, shipping_address)
            VALUES (?, ?, ?)
        """, (order.customer_id, order.total_price, order.shipping_address))

        # Get the last inserted order ID (auto-incremented)
        cursor.execute("SELECT SCOPE_IDENTITY()")
        order_id_row = cursor.fetchone()
        order_id = order_id_row[0]  # 👈 Extract the actual value
        # Insert the associated order items into the 'order_items' table
        for item in order_items:
            cursor.execute("""
                INSERT INTO order_items (order_id, product_id, quantity)
                VALUES (?, ?, ?)
            """, (order_id, item.product_id, item.quantity))

        # Commit the transaction
        self.connection.commit()

        return order_id

    # Method to fetch orders for a customer by customer_id
    def get_order_by_customer_id(self, customer_id):
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT order_id, customer_id, total_price, shipping_address
            FROM orders  -- Ensure that the table name is 'orders' or as per your DB schema
            WHERE customer_id = ?
        """, (customer_id,))
        rows = cursor.fetchall()
        orders = []
        
        for row in rows:
            orders.append(Order(order_id=row[0], customer_id=row[1], total_price=row[2], shipping_address=row[3]))
        
        if orders:
            return orders
        else:
            raise NotFoundException("No orders found for this customer ID.")