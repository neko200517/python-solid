class User:
  def __init__(self, name):
    if len(name) > 20:
      raise ValueError("ユーザー名が20文字を超えています")
    self.name = name

try:
  user = User(input("ユーザー名を入力してください："))
except ValueError as e:
  print(e)