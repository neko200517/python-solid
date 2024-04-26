# 不変条件に派生型で違反しているパターン
class SuperHoge:
    def __init__(self, n: int) -> None:
        if n < 1:
            raise ValueError("1以上にしてください")  # 不変条件、nは1以上
        self._n = n

    def hoge(self, n: int) -> int:
        # 事前条件
        if n < 1:
            raise ValueError("1以上にしてください")
        self._n = self._n * n
        return self._n


class SubHonge(SuperHoge):
    def hoge(self, n: int) -> int:
        # 事前条件
        if n < 1:
            raise ValueError("1以上にしてください")
        # // ... 切り捨て除算
        self._n = self._n // n  # nが1よりも小さくなる可能性がある
        return self._n
