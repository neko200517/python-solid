# ③商品を表現するProductクラスについて考えてみましょう
# 商品は以下のルールを持つものとします
# 　・名前は1文字以上20文字以内
# 　・価格は1円以上
# 　・割引率は5～50%
# 次のコードに契約による設計の考え方を取り入れてコードを改善してください。


class Product:
    def __init__(self, name: str, price: int) -> None:
        if not 1 <= len(name) <= 20:  # 不変条件
            raise ValueError("名前は1文字以上20文字以内")
        if price < 1:  # 不変条件
            raise ValueError("価格は1円以上")
        self._name = name
        self._price = price

    @property  # 読み取り専用にして外部から変更不可に（不変条件の維持）
    def name(self) -> str:
        return self._name

    @property  # 読み取り専用にして外部から変更不可に（不変条件の維持）
    def price(self) -> int:
        return self._price

    def discount(self, discount_percent: int) -> None:
        if not 5 <= discount_percent <= 50:  # 事前条件
            raise ValueError("割引率は5～50%")
        self._price = self._price * (100 - discount_percent) // 100

    def change_name(self, new_name: str) -> None:
        if not 1 <= len(new_name) <= 20:  # 事前条件・不変条件
            raise ValueError("名前は1文字以上20文字以内")
        self._name = new_name


# 事後条件は事前条件や不変条件のようにガード節として組み込まれるというよりはテストケースとして確認するのが基本
