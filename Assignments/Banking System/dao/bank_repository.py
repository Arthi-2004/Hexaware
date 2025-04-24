from abc import ABC, abstractmethod
from bean.account import Account

class IBankRepository(ABC):
    @abstractmethod
    def create_account(self, account: Account):
        pass

    @abstractmethod
    def list_accounts(self) -> list:
        pass

    @abstractmethod
    def get_account_details(self, account_number: int) -> Account:
        pass

    @abstractmethod
    def update_account(self, account: Account):
        pass

    @abstractmethod
    def get_transactions(self, account_number: int, from_date: str, to_date: str):
        pass
