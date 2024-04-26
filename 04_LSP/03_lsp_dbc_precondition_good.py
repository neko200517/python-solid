# 事前条件を守れるように変更したコード（ガード節を追加）
class BankAccount:
    def __init__(self) -> None:
        self._balance = 0

    # 入金
    def deposit(self, amount: int) -> None:
        if amount < 0:
            raise ValueError("事前条件：入金額は0以上")
        self._balance += amount

    # 出金
    def withdraw(self, amount: int) -> None:
        if amount < 0:
            raise ValueError("事前条件：出金額は0以上")
        if amount > self._balance:
            raise ValueError("事前条件：引き出し額は現在の残高以下")
        self._balance -= amount
