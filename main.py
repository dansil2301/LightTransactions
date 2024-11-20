import threading
from copy import copy
from threading import Thread

from TransactionLogic.TransactionHandler import TransactionHandler
from TransactionLogic.TransactionSync import TransactionSync
from ThreadConfig import THREAD_COUNTER, waiting_list_conf, accounts_conf
from DBs.WaitingListDB import WaitingListDB

import time

linear_waiting_list_conf = copy(waiting_list_conf)
linear_accounts_conf = copy(accounts_conf)

transaction_sync = TransactionSync()
total_items_counter = WaitingListDB(waiting_list_conf).get_len_waiting_list()
mutex = threading.Lock()
start_time = None
end_time = None

mutex_first_thread = threading.Lock()
first_thread = True

SYNC_TIME = None
LINEAR_TIME = None


def test_sync(i: int):
    global total_items_counter
    global start_time
    global end_time
    global first_thread

    with mutex_first_thread:
        if first_thread:
            start_time = time.time()
            first_thread = False

    while True:
        with mutex:
            if total_items_counter == 0:
                break

            total_items_counter -= 1

        transaction_sync.start_transaction()

    end_time = time.time()


threads = [Thread(target=test_sync, args=(i + 1,)) for i in range(THREAD_COUNTER)]

for t in threads:
    t.start()

for t in threads:
    t.join()

SYNC_TIME = end_time - start_time


def test_linear():
    global LINEAR_TIME
    global linear_waiting_list_conf
    global linear_accounts_conf
    handler = TransactionHandler(linear_accounts_conf, linear_waiting_list_conf)

    start_time = time.time()
    for transaction in linear_waiting_list_conf:
        account_from = transaction["from"]
        account_to = transaction["to"]
        amount = transaction["amount"]

        handler.handle_transaction(account_from, account_to, amount)
        print(f"Linear transaction from {account_from} to {account_to}")
    end_time = time.time()
    LINEAR_TIME = end_time - start_time


test_linear()

print(f"Sync transaction time: {SYNC_TIME}")
print(f"Linear transaction time: {LINEAR_TIME}")
print(f"Is sync faster: {SYNC_TIME < LINEAR_TIME}")
