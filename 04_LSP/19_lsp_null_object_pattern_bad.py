# Null Objectパターン

from abc import ABC, abstractmethod


class DiscountParameters:
    def __init__(self, items: list):
        self._items = items

    @property
    def total_price(self) -> int:
        return sum(price for _, price in self._items)

    @property
    def item_count(self) -> int:
        return len(self._items)


class CouponStrategy(ABC):
    @abstractmethod
    def apply_discount(self, context: DiscountParameters) -> int:  # 引数をオブジェクトにする
        pass


class PercentageDiscountCoupon(CouponStrategy):
    def __init__(self, percetage: int) -> None:
        self.percentage = percetage

    def apply_discount(self, context: DiscountParameters) -> int:
        return int(context.total_price * (1 - self.percentage / 100))  # 必要な属性だけを利用する


class QuantityDiscountCoupon(CouponStrategy):
    def apply_discount(self, context: DiscountParameters) -> int:
        if context.item_count >= 10:
            return int(context.total_price * 0.9)
        return context.total_price


class ShoppingCart:
    def __init__(self, discount_strategy: CouponStrategy = None) -> None:
        self.items = []
        self.discount_storategy = discount_strategy

    def add_item(self, item_name: str, price: int):
        self.items.append((item_name, price))

    def calculate_total(self) -> int:
        context = DiscountParameters(self.items)
        # クーポンの使用があるかどうかで条件分岐
        if self.discount_storategy is not None:
            return self.discount_storategy.apply_discount(context)
        return context.total_price


cart = ShoppingCart()
cart.add_item("item", 100)
print(f"{cart.calculate_total()}円")
