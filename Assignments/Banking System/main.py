from dao.bank_repository_impl import BankRepositoryImpl
from bean.customer import Customer
from service.bank_service_provider_impl import BankServiceProviderImpl
import pyodbc

def get_db_connection():
    return pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=DELL;'
        'DATABASE=HMBank;'
        'Trusted_Connection=yes;'
    )

def main():
    db_conn = get_db_connection()
    print("Database connection established successfully!")

    bank_repo = BankRepositoryImpl(db_conn)
    bank_service = BankServiceProviderImpl(bank_repo)

    # Change the customer_id if 1001 already exists
    customer = Customer(230, "John", "Doe",  "john.doe@example.com", "9876543210", "123 Elm Street")


    # Try to insert customer
    bank_repo.create_customer(customer)

    # Try to create savings account
    print(f"Attempting to create Savings account for customer {customer.get_customer_id()}")
    savings_account = bank_service.create_account(customer, 'Savings', 5000)

if __name__ == "__main__":
    main()
