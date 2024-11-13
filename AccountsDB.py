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
    def __init__(self):
        self.accounts = {
            "test403": {
                "account_amount": 100.0,
                "is_available": True
            },
            "test404": {
                "account_amount": 200.0,
                "is_available": True
            }
        }

    def _get_account(self, iban: str) -> dict:
        account = self.accounts.get(iban, None)

        if account is None:
            raise KeyError("IBAN is not found")

        return account

    def get_account_by_iban(self, iban: str) -> dict:
        account = self._get_account(iban)
        account["IBAN"] = iban
        return account

    def get_availability(self, iban: str) -> bool:
        account = self._get_account(iban)
        return account["is_available"]

    def set_account_amount(self, iban: str, amount: float) -> None:
        account = self._get_account(iban)
        account["account_amount"] = amount

    def set_account_availability(self, iban: str, is_available: bool) -> None:
        account = self._get_account(iban)
        account["is_available"] = is_available
