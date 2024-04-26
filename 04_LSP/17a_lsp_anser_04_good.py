# ④次のコードはLSPに違反しているでしょうか。
# 違反している場合はその理由を述べたうえで、
# LSPを満たすようにコードを改善してください。

# PercentageDiscountCouponとQuentityDiscountCouponのコンストラクタが一致していないため引数の互換性がない
# 基本型であるCouponStrategyと派生型のQuentityDiscountCouponのapply_discountの引数が一致していないため互換性がない
# クライアントの観点からLSPに違反している

# from abc import ABC, abstractmethod


# class CouponStrategy(ABC):
#     @abstractmethod
#     def apply_discount(self, price: int) -> int:
#         pass


# class PercentageDiscountCoupon(CouponStrategy):
#     def __init__(self, percetage: int) -> None:
#         self.percentage = percetage

#     def apply_discount(self, price: int) -> int:
#         return int(price * (1 - self.percentage / 100))


# class QuantityDiscountCoupon(CouponStrategy):
#     def apply_discount(self, price: int, items_count: int) -> int:
#         if items_count >= 10:
#             return int(price * 0.9)
#         return price


# class ShoppingCart:
#     def __init__(self, discount_strategy: CouponStrategy) -> None:
#         self.items = []
#         self.discount_storategy = discount_strategy

#     def add_item(self, item_name: str, price: int):
#         self.items.append((item_name, price))

#     def calculate_total(self) -> int:
#         total = sum(price for _, price in self.items)
#         return self.discount_storategy.apply_discount(total)


# coupon = PercentageDiscountCoupon(10)
# cart = ShoppingCart(coupon)
# cart.add_item("item1", 100)
# cart.add_item("item2", 200)
# v = cart.calculate_total()
# print(v)

from abc import ABC, abstractmethod


class CouponStrategy(ABC):
    @abstractmethod
    def apply_discount(self, price: int, items_count: int = 0) -> int:  # 引数を追加
        pass


class PercentageDiscountCoupon(CouponStrategy):
    def __init__(self, percetage: int) -> None:
        self.percentage = percetage

    def apply_discount(self, price: int, items_count: int = 0) -> int:
        return int(price * (1 - self.percentage / 100))


class QuantityDiscountCoupon(CouponStrategy):
    def apply_discount(self, price: int, items_count: int) -> int:
        if items_count >= 10:
            return int(price * 0.9)
        return price


class ShoppingCart:
    def __init__(self, discount_strategy: CouponStrategy) -> None:
        self.items = []
        self.discount_storategy = discount_strategy

    def add_item(self, item_name: str, price: int):
        self.items.append((item_name, price))

    def calculate_total(self) -> int:
        total = sum(price for _, price in self.items)
        return self.discount_storategy.apply_discount(total, len(self.items))


coupon = PercentageDiscountCoupon(10)
cart = ShoppingCart(coupon)
for i in range(10):
    cart.add_item("item1", 100)
v = cart.calculate_total()
print(v)

coupon = QuantityDiscountCoupon()
cart = ShoppingCart(coupon)
for i in range(10):
    cart.add_item("item1", 100)
v = cart.calculate_total()
print(v)
