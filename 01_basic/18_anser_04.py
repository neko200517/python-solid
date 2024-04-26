# 型ヒント

# 次のコードに型ヒントをつけてください
# ただし半径（radius）はintとします

# class Circle:
#   PI = 3.14

#   def __init__(self, radius):
#     self._radius = radius
#
#   def length(self):
#     return self._radius * 2 * Circle.PI
#
#   def area(self):
#     return self._radius * self._radius * Circle.PI

class Circle:
  PI = 3.14

  def __init__(self, radius: int) -> None:
    self._radius = radius

  def length(self) -> float:
    return self._radius * 2 * Circle.PI

  def area(self) -> float:
    return self._radius * self._radius * Circle.PI

circle = Circle(5)
print(circle.length())
print(circle.area())