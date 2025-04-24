from bean.account import Account  # Make sure to import Account class

class SavingsAccount(Account):
    def __init__(self, balance, customer, interest_rate):
        super().__init__("Savings", balance, customer)  # Inheriting Account class and setting account_type to "Savings"
        self.interest_rate = interest_rate

    def apply_interest(self):
        self.balance += self.balance * self.interest_rate / 100  # Applying interest on the balance

    def print_account_info(self):
        super().print_account_info()
        print(f"Interest Rate: {self.interest_rate}%")
