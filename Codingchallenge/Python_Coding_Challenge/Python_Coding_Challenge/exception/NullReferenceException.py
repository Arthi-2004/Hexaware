class NullReferenceException(Exception):
    def __init__(self, message="Missing pet information."):
        super().__init__(message)
