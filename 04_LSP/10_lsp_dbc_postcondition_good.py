# 事後条件を派生型で強めているパターン
class SuperHoge:
    def hoge(self, n: int) -> int:
        return n


class SubHooge(SuperHoge):
    def hoge(self, n: int) -> int:
        if n < 0:
            return 0  # 負の数はすべて0にして返す。戻り値の繁栄が狭くなっている。
        return n
