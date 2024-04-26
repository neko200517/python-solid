# 次のコードはDIPに違反している
# DIPを満たすようにした上で
# DIパターンを使ってFastSwimingとSlowSwimingを
# Fishオブジェクトの生成時に切り替えるようにしてください


class FastSwimming:
    def swim(self) -> str:
        return "速く泳ぎます"


class SlowSwiming:
    def swim(self) -> str:
        return "ゆっくり泳ぎます"


class Fish:
    def __init__(self) -> None:
        self.swimming_behavior = FastSwimming()

    def swim(self) -> None:
        print(f"魚が{self.swimming_behavior.swim()}")
