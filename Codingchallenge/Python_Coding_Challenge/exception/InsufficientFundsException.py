class InsufficientFundsException(Exception):
    def __init__(self, message="Minimum donation amount is $10."):
        super().__init__(message)
