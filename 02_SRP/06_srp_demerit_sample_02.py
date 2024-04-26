# 在庫管理クラス
class Inventory:
  def check(self) -> None:
    print("在庫を確認します")

  def reduce(self) -> None:
    print("在庫を減らします")

# 支払処理クラス
class Payment:
  def process(self) -> None:
    print("支払いを処理します")

# 配送処理クラス
class Shipping:
  def ship_order(self) -> None:
    print("注文を出荷します")

inventory = Inventory()
payment = Payment()
shipping = Shipping()

inventory.check()
inventory.reduce()
payment.process()
shipping.ship_order()