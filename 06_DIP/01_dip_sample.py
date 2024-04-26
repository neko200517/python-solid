# eコマースの注文処理


#### 下位モジュール
def validate_user(user_name: str) -> str:
    # ユーザーの有効性をチェック
    pass


def check_stock(product_name: str) -> bool:
    # 在庫をチェック
    pass


def make_payment(user_name: str, product_name: str) -> bool:
    # 支払いを処理
    pass


def update_stock(product_name: str) -> None:
    # 在庫を更新
    pass


##### 上位モジュール
def process_order(user_name: str, product_name: str) -> str:
    if not validate_user(user_name):
        return "無効なユーザーです"
    if not check_stock(product_name):
        return "在庫切れです"
    if not make_payment(user_name, product_name):
        return "購入額が足りません"

    update_stock(product_name)
    return "注文処理が完了しました"
