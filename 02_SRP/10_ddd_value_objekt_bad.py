# ミュータブル（可変）な値オブジェクト
class Yen:
  def __init__(self, amount: int):
    self._amount = amount

  def __add__(self, other: 'Yen'):
    # 自身を変更しているため意図しない動作になっている
    self._amount += other._amount
    return self

  def __str__(self):
    return f"{self._amount}円"

price1 = Yen(100)
print(price1) # 100円

price2 = price1 + Yen(200)
print(price2) # 300円

print(price1, price2) # 300円 300円