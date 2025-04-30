class AdoptionException(Exception):
    def __init__(self, message="Adoption failed."):
        super().__init__(message)
