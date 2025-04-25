# exception/InvalidEmployeeIdException.py

class InvalidEmployeeIdException(Exception):
    def __init__(self, message="Invalid Employee ID. Employee does not exist."):
        super().__init__(message)
