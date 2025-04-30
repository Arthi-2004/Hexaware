class InvalidPetAgeException(Exception):
    def __init__(self, message="Pet age must be a positive integer."):
        super().__init__(message)
