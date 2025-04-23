# exception.py

class InvalidDataException(Exception):
    def __init__(self, message="Invalid data provided."):
        self.message = message
        super().__init__(self.message)


class InsufficientStockException(Exception):
    def __init__(self, message="Insufficient stock available."):
        self.message = message
        super().__init__(self.message)


class IncompleteOrderException(Exception):
    def __init__(self, message="Order detail is incomplete."):
        self.message = message
        super().__init__(self.message)


class PaymentFailedException(Exception):
    def __init__(self, message="Payment processing failed."):
        self.message = message
        super().__init__(self.message)


class IOException(Exception):
    def __init__(self, message="An I/O error occurred."):
        self.message = message
        super().__init__(self.message)


class SqlException(Exception):
    def __init__(self, message="Database query failed."):
        self.message = message
        super().__init__(self.message)


class ConcurrencyException(Exception):
    def __init__(self, message="Concurrency conflict detected. Please retry."):
        self.message = message
        super().__init__(self.message)


class AuthenticationException(Exception):
    def __init__(self, message="Authentication failed. Invalid credentials."):
        self.message = message
        super().__init__(self.message)


class AuthorizationException(Exception):
    def __init__(self, message="Authorization failed. Access denied."):
        self.message = message
        super().__init__(self.message)
