# 次のAgeクラスにカード節を追加して
# コンストラクタ0～130の整数以外が渡されると
# 例外（ValueError）が発生するようにしてください
# ただし整数値がどうかのチェックにはis_int関数を使ってください

class Age:
  def __init__(self, value):
    if not Age.is_int(age):
      raise ValueError("整数でありません")
    if int(value) < 0 or int(value) > 130:
      raise ValueError("0～130の整数を入力してください")
    self.value = value

  def is_int(value):
    try:
      int_value = int(value)
      return int_value == int(value)
    except ValueError:
      return False

try:
  age = input("age?:")
  age_class = Age(age)
  print(age_class.value)
except ValueError as e:
  print(e)