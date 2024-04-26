# Pythonでは慣例としてプライベートな属性・メソッドには名前の先頭に_をつけて表現する

class MyClass:
  def __int__(self, value: str) -> None:
    self._value = value

  def _private_method(self) -> None:
    print("private method")

  def public_method(self) -> None:
    print("public method")

my_class = MyClass(4)

# ただし実際にはアクセス可能
print(my_class._value)
print(my_class._private_method())