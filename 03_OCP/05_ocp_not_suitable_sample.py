# OCPの早すぎる適用

# 現時点でユーザーが1種類しかないといった例の場合、何でもかんでもOCPを採用するのは過剰といえる

from abc import ABC, abstractmethod

class AbstractUser(ABC):
  def __init__(self, name: str, age: int) -> None:
    self.name = name
    self.age = age

class NormalUser(AbstractUser):
  pass
