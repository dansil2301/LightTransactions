from DBs.AccountsDB import AccountsDB
from DBs.WaitingListDB import WaitingListDB


class TransactionHandler:
    def __init__(self):
        self.accounts = AccountsDB()
        self.waiting_list = WaitingListDB()
