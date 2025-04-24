from bean.exceptions import InsufficientFundException, InvalidAccountException, OverDraftLimitExceededException

class BankAccount:
    def __init__(self, account_number, customer_name, balance):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            raise InsufficientFundException("Not enough balance to withdraw.")
        self.balance -= amount

    def transfer(self, target_account, amount):
        if self.balance < amount:
            raise InsufficientFundException("Not enough balance to transfer.")
        if not isinstance(target_account, BankAccount):
            raise InvalidAccountException("Target account is invalid.")
        self.balance -= amount
        target_account.deposit(amount)

    def get_account_number(self):
        return self.account_number

    def get_balance(self):
        return self.balance

    def print_account_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Balance: ${self.balance}")