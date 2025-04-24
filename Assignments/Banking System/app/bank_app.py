# bank_app.py
from service.bank_service_provider_impl import BankServiceProviderImpl
from dao.bank_repository_impl import BankRepositoryImpl
from utils.db_util import DBUtil
from bean.customer import Customer

def main():
    # Establish database connection
    db_conn = DBUtil.get_db_conn()
    if db_conn is None:
        print("Failed to connect to the database.")
        return

    # Initialize Repository and Service layers
    bank_repo = BankRepositoryImpl(db_conn)
    bank_service = BankServiceProviderImpl(bank_repo)
    
    # Create a new customer (simplified)
    customer = Customer(1001, "John", "Doe", "john.doe@example.com", "123456789", "123 Elm Street")
    
    # Create a new savings account for the customer
    account_type = 'Savings'
    balance = 5000
    bank_service.create_account(account_type, customer.customer_id, balance)

    # List all accounts for the customer
    accounts = bank_service.list_accounts()
    print("\nList of accounts:")
    for account in accounts:
        print(f"Account ID: {account[0]}, Type: {account[1]}, Balance: {account[2]}")
    
    # Close the connection when done
    DBUtil.close_db_conn(db_conn)

if __name__ == "__main__":
    main()
