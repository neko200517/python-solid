# ④次のコードはDIPに違反しているでしょうか
# 違反している場合はその理由を述べたうえでDIPを満たすようにコードを改善してください


class GasolinEngine:
    def start(self) -> None:
        print("ガソリンエンジンが始動しました")


class NormalTiers:
    def __init__(self) -> None:
        self._pressure: int = 100

    def is_inflated(self) -> bool:
        if self._pressure >= 1:
            return True
        else:
            print("タイヤに空気を入れてください")
            return False

    def use_air(self) -> None:
        self._pressure -= 1


class Car:
    def __init__(self) -> None:
        self.engine = GasolinEngine()
        self.tiers = NormalTiers()

    def start(self) -> None:
        if self.tiers.is_inflated():
            self.engine.start()
            self.tiers.use_air()
            print("車が発信しました")
