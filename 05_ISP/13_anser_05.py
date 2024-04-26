# ⑤以下のATMを表現したコードはISPに違反しているでしょうか。
# 違反していた場合はその理由を述べたうえでISPを満たすようにコードを改善してください

# ただしATMで操作できる操作は
# ・引き出し
# ・預入
# ・振込
# の３つだけであり、
# これらの操作は1つのトランザクションで1つだけ行われます。
# またBankAccountは銀行の口座を表す値オブジェクトであるとします

# ⇒　インタフェースが分離されていないため違反している

from abc import ABC, abstractmethod


class BankAccount:
    pass


class ATMInterface(ABC):
    @abstractmethod
    def withdraw_transaction(self, amount: int) -> None:
        pass

    @abstractmethod
    def deposit_transaction(self, amount: int) -> None:
        pass

    @abstractmethod
    def transfer_transaction(self, to_bank: BankAccount, amount: int) -> None:
        pass


class ATM(ATMInterface):
    def __init__(self, bank_account: BankAccount) -> None:
        self.bank_account = bank_account

    def withdraw_transaction(self, amount: int) -> None:
        print("出金成功")

    def deposit_transaction(self, amount: int) -> None:
        print("入金成功")

    def transfer_transaction(self, to_bank: BankAccount, amount: int) -> None:
        print("振込成功")


bank = BankAccount()
to_bank = BankAccount()
atm = ATM(bank)
atm.withdraw_transaction(100)
atm.deposit_transaction(100)
atm.transfer_transaction(to_bank, 100)
