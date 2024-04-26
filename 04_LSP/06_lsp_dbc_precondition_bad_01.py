# 事前条件を派生型で強めているパターン
class SuperHoge:
    def hoge(self, n: int) -> int:
        return n


class SubHoge(SuperHoge):
    def hoge(self, n: int) -> int:
        if n < 0:
            raise ValueError("0以上にしてください")
        return n
