# クラスAはクラスBに依存している（コンポジション）
class A:
  def __init__(self):
    self.b = B()

  def method_a(self):
    self.b.method_b()

# クラスBはstrクラスに依存している
class B:
  def method_b(self):
    print("Class B method")

a = A()
a.method_a()