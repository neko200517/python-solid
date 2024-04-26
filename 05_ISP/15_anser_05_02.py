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


class NoBankAccount:
    pass


class ATMParamters:
    def __init__(self, amount: int, to_bank: BankAccount = NoBankAccount()) -> None:
        self.amount = amount
        self.to_bank = to_bank


class WithdrawATMInterface(ABC):
    @abstractmethod
    def withdraw_transaction(self, context: ATMParamters) -> None:
        pass


class DepositATMInterface(ABC):
    @abstractmethod
    def deposit_transaction(self, context: ATMParamters) -> None:
        pass


class TransferATMInterface(ABC):
    @abstractmethod
    def transfer_transaction(self, context: ATMParamters) -> None:
        pass


class WithdrawATMBehavior(WithdrawATMInterface):
    def withdraw_transaction(self, context: ATMParamters) -> None:
        print("出金成功")


class DepositATMBehavior(DepositATMInterface):
    def deposit_transaction(self, context: ATMParamters) -> None:
        print("入金成功")


class TransferATMBehavior(TransferATMInterface):
    def transfer_transaction(self, context: ATMParamters) -> None:
        print("振込成功")


class WithdrawATMClient:
    def __init__(self, bank_account: BankAccount) -> None:
        self.bank_account = bank_account
        self.atm = WithdrawATMBehavior()

    def execute(self, context: ATMParamters):
        self.atm.withdraw_transaction(context)


class DepositATMClient:
    def __init__(self, bank_account: BankAccount) -> None:
        self.bank_account = bank_account
        self.atm = DepositATMBehavior()

    def execute(self, context: ATMParamters):
        self.atm.deposit_transaction(context)


class TransferATMClient:
    def __init__(self, bank_account: BankAccount) -> None:
        self.bank_account = bank_account
        self.atm = TransferATMBehavior()

    def execute(self, context: ATMParamters):
        self.atm.transfer_transaction(context)


mybank = BankAccount()

watm = WithdrawATMClient(bank_account=mybank)
watm.execute(ATMParamters(1000))

datm = DepositATMClient(bank_account=mybank)
datm.execute(ATMParamters(1000))

tatm = TransferATMClient(bank_account=mybank)
tatm.execute(ATMParamters(1000, BankAccount()))
