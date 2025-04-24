from bean.savings_account import SavingsAccount
from bean.current_account import CurrentAccount
from bean.zero_balance_account import ZeroBalanceAccount

class Bank:
    def __init__(self):
        # Use ONE at a time

        # Option 1: List of accounts
        # self.accounts = []

        # Option 2: Set of accounts (no duplicates)
        # self.accounts = set()

        # Option 3: Dict (HashMap) of accounts
        self.accounts = {}  # account_number: account_obj

    def create_account(self, customer, acc_type, balance, interest_rate=None, overdraft_limit=None):
        acc_type = acc_type.strip().lower()

        if acc_type == "savings":
            new_account = SavingsAccount(customer, balance, interest_rate)
        elif acc_type == "current":
            new_account = CurrentAccount(customer, balance, overdraft_limit)
        elif acc_type == "zerobalance":
            new_account = ZeroBalanceAccount(customer, balance)
        else:
            print("Invalid account type!")
            return

        # List
        # self.accounts.append(new_account)

        # Set
        # self.accounts.add(new_account)

        # Dict (HashMap)
        self.accounts[new_account.get_account_number()] = new_account

        print(f"Account created for {customer.get_first_name()} {customer.get_last_name()} (ID: {customer.get_customer_id()})")

    def get_account(self, account_number):
        # List
        # for acc in self.accounts:
        #     if acc.get_account_number() == account_number:
        #         return acc
        # return None

        # Set (same as list logic)

        # Dict
        return self.accounts.get(account_number)

    def list_accounts(self):
        print("\n--- Account List ---")

        # List or Set
        # sorted_accounts = sorted(self.accounts, key=lambda acc: (acc.customer.get_first_name(), acc.customer.get_last_name()))

        # Dict
        sorted_accounts = sorted(self.accounts.values(), key=lambda acc: (acc.customer.get_first_name(), acc.customer.get_last_name()))

        for acc in sorted_accounts:
            acc.print_account_info()
