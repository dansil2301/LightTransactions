from ReadersWriters import ReadersWriters


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
    def __init__(self, waiting_list: list):
        self.readerWriters = ReadersWriters("Writers-First", 0.5)
        self.waiting_list = [
            {
                "from": "A",
                "to": "B",
                "amount": 10  # A 90 B 110
            },
            {
                "from": "B",
                "to": "C",
                "amount": 110  # B 0 C 210
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

    def get_first_by_iban(self, iban: str) -> dict:
        self.readerWriters.reader_enter()
        for transaction in self.waiting_list:
            if transaction["from"] == iban or transaction["to"] == iban:
                self.readerWriters.reader_exit()
                return transaction
        raise KeyError("IBAN is not found in waiting list")

    def get_first(self) -> dict:
        return self.waiting_list[0]

    def get_transaction_by_id(self, position: int) -> dict:
        if position < len(self.waiting_list) <= position:
            raise KeyError("IBAN is not found in waiting list")
        return self.waiting_list[position]

    def delete_from_to_iban(self, from_iban: str, to_iban: str) -> None:
        self.readerWriters.writer_enter()
        for i, transaction in enumerate(self.waiting_list):
            if transaction["from"] == from_iban and transaction["to"] == to_iban:
                self.waiting_list.pop(i)
                self.readerWriters.writer_exit()
                break

    def get_len_waiting_list(self) -> int:
        return len(self.waiting_list)
