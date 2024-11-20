import random
from time import sleep

from DBs.AccountsDB import AccountsDB
from DBs.WaitingListDB import WaitingListDB


class TransactionHandler:
    def __init__(self, accounts_conf, waiting_list_conf):
        self.accounts = AccountsDB(accounts_conf)
        self.waiting_list = WaitingListDB(waiting_list_conf)

    def handle_transaction(self, from_account: str, to_account: str, amount: float) -> None:
        if self.accounts.get_amount_by_iban(from_account) - amount < 0:
            raise ValueError("Insufficient funds found in the account with the following IBAN: " + from_account)

        sleep(1)
        self.accounts.set_account_amount(from_account, self.accounts.get_amount_by_iban(from_account) - amount)
        self.accounts.set_account_amount(to_account, self.accounts.get_amount_by_iban(to_account) + amount)