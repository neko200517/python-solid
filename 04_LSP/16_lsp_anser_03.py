# ③商品を表現するProductクラスについて考えてみましょう
# 商品は以下のルールを持つものとします
# 　・名前は1文字以上20文字以内
# 　・価格は1円以上
# 　・割引率は5～50%
# 次のコードに契約による設計の考え方を取り入れてコードを改善してください。


class Product:
    def __init__(self, name: str, price: int) -> None:
        self.check_precondition_name(name)
        self.check_precondition_price(price)
        self._name = name
        self._price = price

    def discount(self, discount_percent: int) -> None:
        self.check_precondition_discount_percent(discount_percent)
        new_price = self._price * (100 - discount_percent) // 100
        self.check_postcondition_price(new_price, discount_percent)
        self.check_invariant_price(new_price)
        self._price = new_price

    def change_name(self, new_name: str) -> None:
        self.check_precondition_name(new_name)
        self.check_postcondition_name(new_name)
        self.check_invariant_name(new_name)
        self._name = new_name

    # 事前条件（price）
    def check_precondition_price(self, price: int):
        if not price >= 1:
            raise ValueError("価格は1円以上")

    # 事前条件（name）
    def check_precondition_name(self, name: str):
        if not 1 <= len(name) <= 20:
            raise ValueError("名前は1文字以上20文字以内")

    # 事前条件（Price）
    def check_precondition_discount_percent(self, discount_percent: int):
        if not 5 <= discount_percent <= 50:
            raise ValueError("割引率は5%～50%")

    # 事後条件(price)
    def check_postcondition_price(self, new_price: int, discount_percent: int) -> None:
        # DBの値を取得
        db_price = new_price
        if db_price != new_price:
            raise ValueError("事後条件エラー:price")

    # 事後条件(name)
    def check_postcondition_name(self, new_name: str) -> None:
        # DBの値を取得
        db_name = new_name
        if db_name != new_name:
            raise ValueError("事後条件エラー:name")

    # 不変条件（price）
    def check_invariant_price(self, price: int):
        if not price >= 1:
            raise ValueError("価格は1円以上")

    # 不変条件（name）
    def check_invariant_name(self, name: str):
        if not 1 <= len(name) <= 20:
            raise ValueError("名前は1文字以上20文字以内")


product = Product("商品A", 100)
product.change_name("A商品A: 10%割引中")
product.discount(10)
print(product._name, product._price)
