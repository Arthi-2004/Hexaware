
# exceptions.py

class InsufficientFundsException(Exception):
    def __init__(self, message="Insufficient funds for this transaction"):
        self.message = message
        super().__init__(self.message)

class InvalidAccountException(Exception):
    def __init__(self, message="The provided account number is invalid"):
        self.message = message
        super().__init__(self.message)

class OverDraftLimitExceededException(Exception):
    def __init__(self, message="Overdraft limit exceeded for current account"):
        self.message = message
        super().__init__(self.message)
