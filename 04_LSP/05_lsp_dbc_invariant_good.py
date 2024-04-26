# 事後条件を守れるように変更したコード
class BankAccount:
    def __init__(self) -> None:
        self._balance = 0

    # クラス外部から変更されないようにする
    @property
    def balance(self):
        return self._balance

    # 入金
    def deposit(self, amount: int) -> None:
        if amount < 0:
            raise ValueError("事前条件：入金額は0以上")

        new_balance = self._balance + amount
        self._check_invariant(new_balance)  # 不変条件をチェック
        self._balance = new_balance

    # 出金
    def withdraw(self, amount: int) -> None:
        if amount < 0:
            raise ValueError("事前条件：出金額は0以上")
        if amount > self._balance:
            raise ValueError("事前条件：引き出し額は現在の残高以下")

        new_balance = self._balance - amount
        self._check_invariant(new_balance)  # 不変条件をチェック
        self._balance = new_balance

    # 不変条件を確認するメソッド
    def _check_invariant(self, new_balance):
        if new_balance < 0:
            raise ValueError("不変条件：残高は常に0以上の整数値")
