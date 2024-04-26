# 次のコードはDIPに違反している
# DIPを満たすようにした上で
# DIパターンを使ってFastSwimingとSlowSwimingを
# Fishオブジェクトの生成時に切り替えるようにしてください

from abc import ABC, abstractmethod


class AbstractSwimming(ABC):
    @abstractmethod
    def swim(self) -> str:
        pass


class FastSwimming(AbstractSwimming):
    def swim(self) -> str:
        return "速く泳ぎます"


class SlowSwiming(AbstractSwimming):
    def swim(self) -> str:
        return "ゆっくり泳ぎます"


class Fish:
    def __init__(self, behavior: AbstractSwimming) -> None:
        self.swimming_behavior = behavior

    def swim(self) -> None:
        print(f"魚が{self.swimming_behavior.swim()}")


fish1 = Fish(FastSwimming())
fish2 = Fish(SlowSwiming())

fish1.swim()
fish2.swim()
