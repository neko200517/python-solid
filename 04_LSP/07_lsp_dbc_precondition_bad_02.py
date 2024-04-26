# 事前条件を派生型で強めているパターン（例外なし）
class SuperHoge:
    def hoge(self, n: int) -> int:
        return n


class SubHoge(SuperHoge):
    def hoge(self, n: int) -> int:
        # 0以上を期待している（単なるガード節の書き洩らし）
        return n
