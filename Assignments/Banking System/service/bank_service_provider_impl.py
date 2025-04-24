# bank_service_provider_impl.py

class BankServiceProviderImpl:
    def __init__(self, bank_repo):
        self.bank_repo = bank_repo

    def create_account(self, customer, account_type, initial_balance):
        # Get the customer from the repository
        existing_customer = self.bank_repo.get_customer_by_id(customer.get_customer_id())

        if existing_customer:
            print(f"Account creation for customer {customer.get_customer_id()} is valid.")
            # Proceed with account creation logic (not shown here)
        else:
            print(f"Customer {customer.get_customer_id()} not found.")
            # Handle the case where the customer does not exist
