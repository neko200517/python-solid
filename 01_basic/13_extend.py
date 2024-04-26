# クラスBはstrクラスに依存している
class B:
  def method_b(self):
    print("Class B method")

# クラスAはクラスBに依存している（継承）
class A(B):
  def method_a(self):
    super().method_b()

a = A()
a.method_a()