import random
from threading import Thread, Lock
from ThreadConfig import accounts_conf, waiting_list_conf
from time import sleep

from DBs.AccountsDB import AccountsDB
from DBs.WaitingListDB import WaitingListDB

accounts = AccountsDB(accounts_conf)
waiting_list = WaitingListDB(waiting_list_conf)

N_THREADS = 5

total_items_counter = waiting_list.get_len_waiting_list()
transaction_counter = 0
mutex_counter = Lock()


def test(i: int):
    global accounts
    global waiting_list
    global transaction_counter
    global total_items_counter

    while True:
        with mutex_counter:
            if total_items_counter == 0:
                break

            total_items_counter -= 1
            transaction = waiting_list.get_transaction_by_id(transaction_counter)
            print(i, transaction_counter, transaction["from"], transaction["to"])
            transaction_counter += 1

        while waiting_list.get_first_by_iban(transaction["from"]) != waiting_list.get_first_by_iban(transaction["to"]):
            continue

        with accounts.get_availability(transaction["from"]) and accounts.get_availability(transaction["to"]):
            if accounts.get_amount_by_iban(transaction["from"]) - transaction["amount"] < 0:
                continue

            sleep(random.uniform(0, 1.5))
            accounts.set_account_amount(transaction["from"],
                                        accounts.get_amount_by_iban(transaction["from"]) - transaction["amount"])
            accounts.set_account_amount(transaction["to"],
                                        accounts.get_amount_by_iban(transaction["to"]) + transaction["amount"])

            with mutex_counter:
                waiting_list.delete_from_to_iban(transaction["from"], transaction["to"])
                transaction_counter -= 1


threads = [Thread(target=test, args=(i, )) for i in range(N_THREADS)]

for t in threads:
    t.start()

for t in threads:
    t.join()

print(accounts.get_all_accounts())
print(waiting_list.get_len_waiting_list())
