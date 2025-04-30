import sys
import os

# Add the root directory to sys.path to allow relative imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Now, you can import the modules from dao and util
from dao.customer_dao import CustomerDAO
from dao.product_dao import ProductDAO
from dao.cart_dao import CartDAO
from dao.order_dao import OrderDAO
from exception.not_found_exception import NotFoundException
from entity.customer import Customer
from entity.product import Product
from entity.cart import Cart
from entity.order import Order
from entity.order_item import OrderItem

def display_menu():
    print("\nEcommerce Application Menu:")
    print("1. Register Customer")
    print("2. Create Product")
    print("3. Delete Product")
    print("4. Add to Cart")
    print("5. View Cart")
    print("6. Place Order")
    print("7. View Customer Orders")
    print("8. Exit")

def register_customer():
    name = input("Enter customer name: ")
    email = input("Enter customer email: ")
    password = input("Enter customer password: ")

    customer = Customer(None, name, email, password)
    customer_dao = CustomerDAO()
    customer_dao.add_customer(customer.name, customer.email, customer.password)

    # Retrieve the customer ID after registration
    registered_customer = customer_dao.get_customer_by_email(email)  # Assuming method exists
    print(f"Customer {name} registered successfully! Your customer ID is {registered_customer.customer_id}. You can use this ID to place orders.")

def create_product():
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    description = input("Enter product description: ")
    stockQuantity = int(input("Enter stock quantity: "))

    product = Product(None, name, price, description, stockQuantity)
    product_dao = ProductDAO()
    product_dao.add_product(product.name, product.price, product.description, product.stockQuantity)

    # After creating the product, display the product list with their IDs
    products = product_dao.get_all_products()
    print("Available Products:")
    for product in products:
        print(f"Product ID: {product.product_id}, Name: {product.name}, Price: {product.price}")

def delete_product():
    product_id = int(input("Enter product ID to delete: "))
    product_dao = ProductDAO()

    try:
        product_dao.delete_product(product_id)
        print(f"Product with ID {product_id} deleted successfully!")
    except NotFoundException:
        print("Product not found!")

def add_to_cart():
    customer_id = int(input("Enter customer ID: "))
    product_dao = ProductDAO()
    product_dao.get_all_products()

    products = product_dao.get_all_products()
    print("Available Products:")
    for product in products:
        print(f"Product ID: {product.product_id}, Name: {product.name}, Price: {product.price}")

    product_id = int(input("Enter product ID to add to cart: "))
    quantity = int(input("Enter quantity: "))

    # Create a Cart instance
    cart = Cart(None, customer_id, product_id, quantity)
    
    # Create a CartDAO instance
    cart_dao = CartDAO()

    # Add the cart to the database
    cart_dao.add_cart(customer_id, product_id, quantity)

    print(f"✅ Added {quantity} of product {product_id} to the cart for customer {customer_id}.")

def view_cart():
    customer_id = int(input("Enter customer ID to view cart: "))
    cart_dao = CartDAO()

    cart_items = cart_dao.view_cart(customer_id)
    if cart_items:
        print("\nItems in cart:")
        for item in cart_items:
            print(f"Product ID: {item.product_id}, Quantity: {item.quantity}")
    else:
        print("Cart is empty.")

def place_order():
    customer_id = int(input("Enter customer ID: "))
    order_dao = OrderDAO()
    cart_dao = CartDAO()

    # Fetch cart items for the customer
    cart_items = cart_dao.view_cart(customer_id)
    if not cart_items:
        print("Cart is empty. Cannot place order.")
        return

    total_price = 0
    order_items = []

    # Calculate the total price and create order items
    for item in cart_items:
        product = ProductDAO().get_product_by_id(item.product_id)
        total_price += product.price * item.quantity
        order_items.append(OrderItem(None, None, item.product_id, item.quantity))  # Create OrderItem objects

    # Now ask for the shipping address
    shipping_address = input("Enter shipping address: ")

    # Print the total price and shipping address for debugging purposes
    print(f"Total Price: {total_price}")
    print(f"Shipping Address: {shipping_address}")

    # Ensure total_price and shipping_address are correctly passed
    if total_price <= 0 or not shipping_address:
        print("Error: Total price or shipping address is missing.")
        return

    # Create the Order object with the required data
    order = Order(customer_id, total_price, shipping_address)  # Pass customer_id, total_price, and shipping_address

    # Place the order (you can add order_id if required, or let the database generate it)
    order_id = order_dao.create_order(order, order_items)
    print(f"✅ Order placed successfully")

    # Clear the cart after placing the order
    cart_dao.clear_cart(customer_id)

def view_customer_orders():
    customer_id = int(input("Enter customer ID to view orders: "))
    order_dao = OrderDAO()

    try:
        # Use the correct method name, which is 'get_order_by_customer_id'
        orders = order_dao.get_order_by_customer_id(customer_id)  
        if orders:
            for order in orders:
                print(order)  # Or print the order details in your desired format
        else:
            print("No orders found for this customer.")
    except NotFoundException as e:
        print(e)

def main():
    while True:
        display_menu()
        choice = int(input("Enter your choice: "))

        if choice == 1:
            register_customer()
        elif choice == 2:
            create_product()
        elif choice == 3:
            delete_product()
        elif choice == 4:
            add_to_cart()
        elif choice == 5:
            view_cart()
        elif choice == 6:
            place_order()
        elif choice == 7:
            view_customer_orders()
        elif choice == 8:
            print("Exiting the application.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
