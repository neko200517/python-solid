# ④次のコードはDIPに違反しているでしょうか
# 違反している場合はその理由を述べたうえでDIPを満たすようにコードを改善してください

# ⇒　CarがGasolineEngineとNormalTiersに依存しているためDIPに違反している

from abc import ABC, abstractmethod


class EngineInterface(ABC):
    @abstractmethod
    def start(self) -> None:
        pass


class TierInterface(ABC):
    @abstractmethod
    def is_inflated(self) -> bool:
        pass

    @abstractmethod
    def use_air(self) -> None:
        pass


class GasolineEngine(EngineInterface):
    def start(self) -> None:
        print("ガソリンエンジンが始動しました")


class NormalTiers(TierInterface):
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
    def __init__(self, engine: EngineInterface, tiers: TierInterface) -> None:
        self.engine = engine
        self.tiers = tiers

    def start(self) -> None:
        if self.tiers.is_inflated():
            self.engine.start()
            self.tiers.use_air()
            print("車が発信しました")


# クライアントでガソリンとタイヤの種類を選択して車を生成するコードに改修
gasoline_engine = GasolineEngine()
normal_tiers = NormalTiers()
car = Car(gasoline_engine, normal_tiers)
car.start()
