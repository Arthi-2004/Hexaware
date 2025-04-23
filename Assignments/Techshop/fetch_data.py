import pyodbc

# Function to establish the connection to the database
def create_connection():
    # Updated connection string using trusted connection (no username/password)
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=SHRUTHI;'  # Replace with your server name
        'DATABASE=TECHSHOP_NEW;'  # Replace with your database name
        'Trusted_Connection=yes;'  # Use trusted connection instead of username/password
    )
    return conn

# Function to fetch and display data
def fetch_data():
    conn = create_connection()
    cursor = conn.cursor()

    # Fetching data from customers table
    cursor.execute("SELECT * FROM dbo.customers")
    customers = cursor.fetchall()
    print("Customers:")
    for customer in customers:
        print(customer)

    # Fetching data from products table
    cursor.execute("SELECT * FROM dbo.products")
    products = cursor.fetchall()
    print("\nProducts:")
    for product in products:
        print(product)

    # Fetching data from orders table
    cursor.execute("SELECT * FROM dbo.orders")
    orders = cursor.fetchall()
    print("\nOrders:")
    for order in orders:
        print(order)

    # Fetching data from orderdetails table
    cursor.execute("SELECT * FROM dbo.orderdetails")
    order_details = cursor.fetchall()
    print("\nOrder Details:")
    for order_detail in order_details:
        print(order_detail)

    conn.close()

# Run this function when this script is executed
if __name__ == "__main__":
    fetch_data()
