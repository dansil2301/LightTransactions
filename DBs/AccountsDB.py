from threading import Lock


class AccountsDB:
    """
    A class that contains all accounts
    and methods to extract data properly

    Structure:
    accounts = {
        "52 TS 404 404": {
            "account_amount": 404.0,
            "is_available": True
        }
        ...
    }
    """
    def __init__(self, accounts: dict):
        self.accounts = {
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

    def _get_account(self, iban: str) -> dict:
        account = self.accounts.get(iban, None)

        if account is None:
            raise KeyError("IBAN is not found")

        return account

    def get_all_accounts(self):
        return self.accounts

    def get_account_by_iban(self, iban: str) -> dict:
        account = self._get_account(iban)
        account["IBAN"] = iban
        return account

    def get_availability(self, iban: str) -> Lock:
        account = self._get_account(iban)
        return account["is_available"]

    def set_account_amount(self, iban: str, amount: float) -> None:
        account = self._get_account(iban)
        account["account_amount"] = amount

    def get_amount_by_iban(self, iban: str) -> float:
        account = self._get_account(iban)
        return account["account_amount"]

    def set_account_availability(self, iban: str, is_available: bool) -> None:
        account = self._get_account(iban)
        account["is_available"] = is_available
