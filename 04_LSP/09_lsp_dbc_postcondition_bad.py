# 事後条件を派生型で弱めているパターン
class SuperHoge:
    def hoge(self, n: int) -> int:
        return n


class SubHooge(SuperHoge):
    def hoge(self, n: int) -> int | tuple[int, str]:  # 戻り値の範囲が広くなっている
        if n > 0:
            return n, "正の数です"
        return n


def hoge_client(hoge_obj: SuperHoge):
    return hoge_obj(2) * 10
