# bean/account.py
class Account:
    last_acc_no = 0  # Static variable for generating account numbers

    def __init__(self, account_number, account_type, customer_id, balance):
        self.account_number = account_number
        self.account_type = account_type
        self.customer_id = customer_id
        self.balance = balance

        # Ensure last_acc_no stays in sync
        if account_number > Account.last_acc_no:
            Account.last_acc_no = account_number

    def __str__(self):
        return f"Account Number: {self.account_number}, Type: {self.account_type}, Balance: {self.balance}"
