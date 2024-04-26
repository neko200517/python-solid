# 契約による設計を意識していないコード
class BankAccount:
    def __init__(self) -> None:
        self._balance = 0

    def deposit(self, amount: int) -> None:
        self._balance += amount

    def withdraw(self, amount: int) -> None:
        self._balance -= amount
