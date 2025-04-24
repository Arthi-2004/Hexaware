from abc import ABC, abstractmethod
from bean.customer import Customer
from bean.account import Account

class IBankServiceProvider(ABC):

    @abstractmethod
    def create_account(self, customer: Customer, account_type: str, initial_balance: float) -> Account:
        pass

    @abstractmethod
    def list_accounts(self) -> list:
        pass

    @abstractmethod
    def calculate_interest(self, account_number: int) -> float:
        pass
