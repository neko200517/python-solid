# ③次のコードはOCPに違反しているでしょうか。
# 違反している場合はその理由を述べたうえでOCPを満たすようにコードを改善してください。

# class Payment:
#   def pay(self, amount: int, method: str) -> None:
#     if method == "cash":
#       print(f"{amount}を現金で支払いました。")
#     elif method == "credit_card":
#       print(f"{amount}をクレジットカードで支払いました。")
#     elif method == "QRPay":
#       print(f"{amount}をQRPayで支払いました。")
#     else:
#       raise ValueError("利用できない決済方法です。")

# 違反している。
# 拡張に対して実装の追加が一つの関数で実現されており、保守性が悪い。

from abc import ABC,abstractmethod

class AbstractPayment(ABC):
  @abstractmethod
  def pay(self, amount: int):
    pass

class CashPayment(AbstractPayment):
  def pay(self, amount: int):
    print(f"{amount}を現金で支払いました。")

class CreditCardPayment(AbstractPayment):
  def pay(self, amount: int):
    print(f"{amount}をクレジットカードで支払いました。")

class QRPayPayment(AbstractPayment):
  def pay(self, amount: int):
    print(f"{amount}をQRPayで支払いました。")

def pay(amount: int, payment: AbstractPayment):
  if not isinstance(payment, AbstractPayment):
    raise ValueError("利用できない決済方法です。")
  payment.pay(amount)

amount = 100
pay(amount=amount, payment=CashPayment())
pay(amount=amount, payment=CreditCardPayment())
pay(amount=amount, payment=QRPayPayment())
pay(amount=amount, payment=None)