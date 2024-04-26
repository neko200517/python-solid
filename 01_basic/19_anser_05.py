# フールプルーフとアクセス制限
# 次のコードに①～③の変更をそれぞれ行ってください

# class User:
#   def __init__(self, name: str, age: int) -> None:
#     self.name = name
#     self.age = age

# ① nameとageがプライベートな属性であることを表現してください
# ② @propertyデコレータを使って、クラスの外部から読み取り可能なname属性とage属性を定義してください
# ③ name属性とage属性をクラスの外部から変更可能にしてください
# 　ただしその際にガード節を用いて次の状態が保たれるようにしてください
# 　　・名前(name)は、1文字以上20文字以下
# 　　・年齢は(age)は、0歳以上150歳以下

class User:
  def __init__(self, name: str, age: int) -> None:
    if not 1 <= len(name) <= 20:
      raise ValueError("1文字以上20文字以下で入力してください")
    if not 0 <= age <= 150:
      raise ValueError("0歳以上150以下で入力してください")
    self._name = name
    self._age = age

  @property
  def name(self) -> str:
    return self._name

  @property
  def age(self) -> int:
    return self._age

  @name.setter
  def name(self, name: str) -> bool:
    if not 1 <= len(name) <= 20:
      raise ValueError("1文字以上20文字以下で入力してください")
    self._name = name

  @age.setter
  def age(self, age: int) -> bool:
    if not 0 <= age <= 150:
      raise ValueError("0歳以上150以下で入力してください")
    self._age = age

try:
  name = input("name?:")
  age = input("age?:")
  user = User(name, age)
  user.name = name
  user.age = age
  print(user.name)
  print(user.age)
except ValueError as e:
  print(e)