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

# 注文処理のFacade
class OrderFacade:
  def __init__(self) -> None:
    self.inventory = Inventory()
    self.payment = Payment()
    self.shipping = Shipping()

  def place_order(self) -> None:
    self.inventory.check()
    self.inventory.reduce()
    self.payment.process()
    self.shipping.ship_order()

order_facade = OrderFacade()
order_facade.place_order()