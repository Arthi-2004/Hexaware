from datetime import datetime

class Transaction:
    def __init__(self, account, description, transaction_type, transaction_amount):
        self.account = account
        self.description = description
        self.transaction_type = transaction_type
        self.transaction_amount = transaction_amount
        self.date_time = datetime.now()

    def __str__(self):
        return f"Transaction on {self.date_time}: {self.transaction_type} {self.transaction_amount} for Account {self.account.account_number}, Description: {self.description}"
