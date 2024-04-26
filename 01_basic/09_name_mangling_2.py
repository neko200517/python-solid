class A:
  def __init__(self):
    self.__hoge = 123 # _A__hogeに置換される

  def print_hoge(self):
    print(self.__hoge) # _A__hogeを出力

class B(A):
  def __init__(self):
    super().__init__()
    self.__hoge = 456 # _B__hogeに置換される（親クラスの__hogeという名前が衝突していても独立して利用可能）

b = B()
b.print_hoge() # 123

print(b._A__hoge) # 123
print(b._B__hoge) # 456