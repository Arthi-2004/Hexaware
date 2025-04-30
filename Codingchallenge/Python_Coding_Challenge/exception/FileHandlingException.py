class FileHandlingException(Exception):
    def __init__(self, message="Error reading file."):
        super().__init__(message)
