class Rectangle:
  def __init__(self, width: int, height: int) -> None:
    self._width = width
    self._height = height

  # widthのGetterメソッド
  @property
  def width(self) -> int:
    return self._width

  # heightのGetterメソッド
  @property
  def height(self) -> int:
    return self._height

  # width属性が上書きされたときに呼び出されるメソッド
  @width.setter
  def width(self, value: int) -> None:
    if value < 0:
      raise ValueError("required: width >= 0")
    self._width = value

  # height属性が上書きされたときに呼び出されるメソッド
  @height.setter
  def height(self, value: int) -> None:
    if value < 0:
      raise ValueError("required: height >= 0")
    self._height = value


rect = Rectangle(1, 2)
try:
  rect.width = 10 # Setterを定義したので上書き可能
  rect.height = -1 # バリデーションエラー
except ValueError as e:
  print(e)
finally:
  print(rect.width, rect.height)