from bean.account import Account

class ZeroBalanceAccount(Account):
    def __init__(self, customer):
        super().__init__("ZeroBalance", 0, customer)  # ZeroBalanceAccount starts with a balance of 0

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def print_account_info(self):
        super().print_account_info()
        print("This is a zero-balance account.")
