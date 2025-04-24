# Import the ICustomerServiceProvider from the correct path
from service.icustomer_service_provider import ICustomerServiceProvider

# Import other necessary classes
from dao.bank_repository import BankRepositoryImpl
from bean.savings_account import SavingsAccount
from bean.current_account import CurrentAccount
from bean.zero_balance_account import ZeroBalanceAccount

class CustomerServiceProviderImpl(ICustomerServiceProvider):

    def __init__(self, bank_repo: BankRepositoryImpl):
        self.bank_repo = bank_repo

    def get_account_balance(self, account_number: int) -> float:
        account = self.bank_repo.get_account_details(account_number)
        return account.balance

    def deposit(self, account_number: int, amount: float) -> float:
        account = self.bank_repo.get_account_details(account_number)
        account.balance += amount
        self.bank_repo.update_account(account)
        return account.balance

    def withdraw(self, account_number: int, amount: float) -> float:
        account = self.bank_repo.get_account_details(account_number)
        if isinstance(account, SavingsAccount) and account.balance - amount < 500:
            raise ValueError("Cannot withdraw below minimum balance for savings account.")
        if isinstance(account, CurrentAccount) and account.balance - amount < -account.overdraft_limit:
            raise ValueError("Withdrawal exceeds overdraft limit.")
        
        account.balance -= amount
        self.bank_repo.update_account(account)
        return account.balance

    def transfer(self, from_account_number: int, to_account_number: int, amount: float) -> bool:
        from_account = self.bank_repo.get_account_details(from_account_number)
        to_account = self.bank_repo.get_account_details(to_account_number)

        if from_account.balance < amount:
            raise ValueError("Insufficient balance for transfer.")
        
        from_account.balance -= amount
        to_account.balance += amount

        self.bank_repo.update_account(from_account)
        self.bank_repo.update_account(to_account)
        return True

    def get_account_details(self, account_number: int):
        return self.bank_repo.get_account_details(account_number)

    def get_transactions(self, account_number: int, from_date: str, to_date: str):
        return self.bank_repo.get_transactions(account_number, from_date, to_date)
