class WaitingListDB:
    """
    A class that contains all transactions
    to be executed by threads

    Structure:
    waiting_list = [
        {
            "from": *IBAN,
            "to": *IBAN,
            "amount": 404
        },
        ...
    ]
    """
    def __init__(self):
        self.waiting_list = [
            {
                "from": "test403",
                "to": "test404",
                "amount": 10
            },
            {
                "from": "test404",
                "to": "test403",
                "amount": 10
            }
        ]

    def get_first_by_iban(self, iban: str) -> dict:
        for transaction in self.waiting_list:
            if transaction["from"] == iban or transaction["to"] == iban:
                return transaction
            raise KeyError("IBAN is not found in waiting list")

    def get_first(self) -> dict:
        return self.waiting_list[0]
