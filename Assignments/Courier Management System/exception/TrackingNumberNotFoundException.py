# exception/TrackingNumberNotFoundException.py

class TrackingNumberNotFoundException(Exception):
    def __init__(self, message="Tracking number not found."):
        super().__init__(message)
