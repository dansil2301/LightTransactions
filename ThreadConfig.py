from threading import Lock

THREAD_COUNTER = 3

waiting_list_conf = [
            {
                "from": "A",
                "to": "B",
                "amount": 200  # A 90 B 110
            },
            {
                "from": "B",
                "to": "C",
                "amount": 10  # B 0 C 210
            },
            {
                "from": "C",
                "to": "D",
                "amount": 10  # C 200 D 110
            },
            {
                "from": "D",
                "to": "A",
                "amount": 10  # D 100 A 100
            },
            {
                "from": "D",
                "to": "E",
                "amount": 10
            },
            {
                "from": "F",
                "to": "G",
                "amount": 10
            },
            {
                "from": "Z",
                "to": "Y",
                "amount": 10
            },
            {
                "from": "A",
                "to": "D",
                "amount": 10
            },
            {
                "from": "E",
                "to": "G",
                "amount": 10
            },
            {
                "from": "G",
                "to": "H",
                "amount": 10
            }
        ]

accounts_conf = {
            "A": {
                "account_amount": 100.0,
                "is_available": Lock()
            },
            "B": {
                "account_amount": 100.0,
                "is_available": Lock()
            },
            "C": {
                "account_amount": 100.0,
                "is_available": Lock()
            },
            "D": {
                "account_amount": 100.0,
                "is_available": Lock()
            },
            "E": {
                "account_amount": 100.0,
                "is_available": Lock()
            },
            "F": {
                "account_amount": 100.0,
                "is_available": Lock()
            },
            "G": {
                "account_amount": 100.0,
                "is_available": Lock()
            },
            "H": {
                "account_amount": 100.0,
                "is_available": Lock()
            },
            "I": {
                "account_amount": 100.0,
                "is_available": Lock()
            },
            "Z": {
                "account_amount": 100.0,
                "is_available": Lock()
            },
            "Y": {
                "account_amount": 100.0,
                "is_available": Lock()
            }
        }
