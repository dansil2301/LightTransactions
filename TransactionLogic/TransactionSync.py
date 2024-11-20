import threading

from DBs.AccountsDB import AccountsDB
from DBs.WaitingListDB import WaitingListDB
from ThreadConfig import accounts_conf, waiting_list_conf
from TransactionLogic.TransactionHandler import TransactionHandler


class TransactionSync:
    def __init__(self):
        self.accounts = AccountsDB(accounts_conf)
        self.waiting_list = WaitingListDB(waiting_list_conf)

        self.transaction_handler = TransactionHandler(accounts_conf, waiting_list_conf)

        self.transaction_pointer = 0

        self.mutex_counter = threading.Lock()

    def _deletion_from_waiting_list(self, from_acc: str, to_acc: str) -> None:
        with self.mutex_counter:
            try:
                self.waiting_list.delete_from_to_iban(from_acc, to_acc)
            except Exception as e:
                raise ValueError(f"Couldn't delete transaction from account '{from_acc}' to '{to_acc} failed: {e}")
            self.transaction_pointer -= 1

    def _transfer_transaction_from_waiting_list(self, from_acc: str, to_acc: str, amount: float) -> None:
        try:
            self.transaction_handler.handle_transaction(from_acc, to_acc, amount)
            print(f"Transaction from {from_acc} to {to_acc} of amount {amount} has been successfully transferred")
        except Exception as e:
            raise ValueError(f"Transaction from account '{from_acc}' to '{to_acc}' failed: {e}")

    def _wait_in_queue(self, from_acc: str, to_acc: str) -> None:
        try:
            while self.waiting_list.get_first_by_iban(from_acc) != self.waiting_list.get_first_by_iban(to_acc):
                continue
        except Exception as e:
            raise ValueError(f"Couldn't find any transactions for these accounts: {e}")

    def start_transaction(self):
        try:
            with self.mutex_counter:
                try:
                    transaction = self.waiting_list.get_transaction_by_id(self.transaction_pointer)
                except Exception as e:
                    print(f"Couldn't find transaction by id")

                from_acc = transaction["from"]
                to_acc = transaction["to"]
                amount = transaction["amount"]

                self.transaction_pointer += 1

            self._wait_in_queue(from_acc, to_acc)

            with self.accounts.get_availability(from_acc) and self.accounts.get_availability(to_acc):
                self._transfer_transaction_from_waiting_list(from_acc, to_acc, amount)
                self._deletion_from_waiting_list(from_acc, to_acc)
        except Exception as e:
            self._deletion_from_waiting_list(from_acc, to_acc)
            print(e)
