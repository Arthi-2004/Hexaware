from abc import ABC, abstractmethod

class Donation(ABC):
    def __init__(self, donor_name, amount):
        self._donor_name = donor_name
        self._amount = amount

    @abstractmethod
    def record_donation(self):
        pass
