class Order:
  def place_order(self) -> None:
    # 在庫管理の処理
    print("在庫を確認します")
    print("在庫を減らします")

    # 支払処理
    print("支払いを処理します")

    # 配送処理
    print("注文を出荷します")

order = Order()
order.place_order()