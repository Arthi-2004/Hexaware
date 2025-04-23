from entity.customer import Customer
from entity.product import Product
from entity.order import Order
from entity.order_detail import OrderDetail  # Ensure this is the correct path
from database_connector import DatabaseConnector

def main():
    try:
        # Connect to the database
        db_connector = DatabaseConnector()
        db_connector.connect()
        print("Database connection established successfully.\n")

        # Register a new customer
        print("--- Customer Registration ---")
        new_customer = Customer("Alice", "Smith", "alice.smith@example.com", "9876543210", "456 Elm St, Chennai, India")
        new_customer.register_customer(db_connector)  # Register customer in the database
        print(f"Customer registered successfully with ID: {new_customer.customerid}\n")

        # Register a new product
        print("--- Product Registration ---")
        new_product = Product("Smartphone", "A high-end smartphone with excellent features", 800.00)
        new_product.register_product(db_connector)  # Register product in the database
        print(f"Product registered successfully with ID: {new_product.productid}\n")

        # Place a new order
        print("--- Order Placement ---")
        order = Order(new_customer.customerid, "2025-04-25", 800.00)  # Use customer ID from registered customer
        order.place_order(db_connector)  # Place the order in the database
        print(f"Order placed successfully with ID: {order.orderid}\n")

        # Add order details
        print("--- Adding Order Details ---")
        order_detail = OrderDetail(order.orderid, new_product.productid, 1)  # Use order and product IDs from inserted records
        order_detail.add_order_detail(db_connector)  # Add order details in the database
        print(f"Order detail added successfully with ID: {order_detail.orderdetailid}\n")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Ensure database connection is closed
        db_connector.close()
        print("Database connection closed.\n")

if __name__ == "__main__":
    main()
