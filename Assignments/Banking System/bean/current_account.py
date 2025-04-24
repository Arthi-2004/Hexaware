from bean.account import Account

class CurrentAccount(Account):
    def __init__(self, balance, customer, overdraft_limit):
        super().__init__("Current", balance, customer)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if self.balance + self.overdraft_limit >= amount:
            self.balance -= amount
            return self.balance
        else:
            raise Exception("Overdraft limit exceeded")

    def print_account_info(self):
        super().print_account_info()
        print(f"Overdraft Limit: ${self.overdraft_limit}")
