# 事後条件を守れるように変更したコード
class BankAccount:
    def __init__(self) -> None:
        self._balance = 0

    # 入金
    def deposit(self, amount: int) -> None:
        if amount < 0:
            raise ValueError("事前条件：入金額は0以上")

        old_balance = self._balance
        new_balance = self._balance + amount
        self._check_postcondition(new_balance, old_balance, amount)
        self._balance = new_balance

    # 出金
    def withdraw(self, amount: int) -> None:
        if amount < 0:
            raise ValueError("事前条件：出金額は0以上")
        if amount > self._balance:
            raise ValueError("事前条件：引き出し額は現在の残高以下")

        old_balance = self._balance
        new_balance = self._balance - amount
        self._check_postcondition(new_balance, old_balance, amount)
        self._balance = new_balance

    # 事後条件を確認するメソッド
    def _check_postcondition(self, new_balance: int, old_balance: int, amount: int):
        diff = new_balance - old_balance
        if abs(diff) != amount:
            raise ValueError("事後条件：入金・出金額と口座残高に整合性がある")
