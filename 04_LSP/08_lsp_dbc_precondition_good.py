# 事前条件を派生型で弱めているパターン
class SuperHoge:
    def hoge(self, n: int) -> int:
        if n < 0:
            raise ValueError("0以上にしてください")
        return n


class SubHoge(SuperHoge):
    def hoge(self, n: int) -> int:
        return n


def hoge0(hoge_obj: SuperHoge):
    print(hoge_obj.hoge(0))
