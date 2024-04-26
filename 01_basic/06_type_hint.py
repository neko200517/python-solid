def add(n1: int, n2: int) -> int:
  return n1 + n2

# ただし実行時に無視される
print(add("1", "2"))

def greeting(name: str) -> str:
  return "Hello " + name

first_name = "hoge"
last_name = "fuga"

print(greeting(f"{first_name} {last_name}"))

# コンテナオブジェクトの型ヒント
number_list: list[int] = [1, 2, 3]
str_int_dict: dict[str, int] = {"a": 1, "b": 2}

# 独自の型
class Hoge:
  def __init__(self, value: str) -> None:
    self.value = value

def print_hoge(hoge: Hoge) -> None:
  print(hoge.value)

hoge: Hoge = Hoge("hoge")
print_hoge(hoge)