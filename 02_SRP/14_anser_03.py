# ③次のコードはSRPに違反しているでしょうか
# 違反している場合はその理由を述べたうえでSRPを満たすようにコードを改善してください。

# class Customer:
#   def __init__(self, name: str, age: int):
#     self.name = name
#     self.age = age

#   def __str__(self) -> str:
#     return f"名前：{self.name}, 年齢：{self.age}"

#   def calculate_discount(self, total_amount: int) -> None:
#     if self.age >= 60:
#       discount = total_amount * 0.1
#     else:
#       discount = total_amount * 0.05
#     print(f"割引額：{discount}")

#   def send_email(self) -> None:
#     email_content = f"お客様のご購入ありがとうございます、{self.name}さん。"
#     print("メールを送信しました。")

#   def calculate_points(self, total_amount: int) -> None:
#     points = total_amount / 10
#     print(f"獲得ポイント：{points}")

# ⇒2つ以上の責務が存在するためSRPの原則に違反している

# 顧客クラス
class Customer:
  def __init__(self, name: str, age: int):
    self.name = name
    self.age = age

  def __str__(self) -> str:
    return f"名前：{self.name} 年齢：{self.age}"

# メール送信クラス
class EmailSender:
  def send_email(self, customer: Customer) -> None:
    email_content = f"お客様のご購入ありがとうございます、{customer.name}さん。"
    print("メールを送信しました。")

# 割引計算クラス
class DiscountCalculator:
  def calculate_discount(self, customer: Customer, total_amount: int) -> None:
    if customer.age >= 60:
      discount = total_amount * 0.1
    else:
      discount = total_amount * 0.05
    print(f"割引額：{discount}")

# ポイント計算クラス
class PointCalculator:
  def calculate_points(self, customer: Customer, total_amount: int) -> None:
    points = total_amount / 10
    print(f"獲得ポイント：{points}")

customer = Customer("hoge", 20)
email = EmailSender()
discount = DiscountCalculator()
poiint = PointCalculator()

total_amount = 10

print(customer)
email.send_email(customer)
discount.calculate_discount(customer, total_amount)
poiint.calculate_points(customer, total_amount)