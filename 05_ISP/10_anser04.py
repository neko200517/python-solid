# ④以下の音楽ストリーミングサービスのコードはISPに違反しているでしょうか。
# 違反している場合はその理由を述べ、ISPを満たすようなコードに改善してください。

# この音楽ストリーミングサービスでは
# 無料ユーザーと有料ユーザーで使用できる機能が異なります
# ・無料ユーザーは広告ありの再生のみが可能
# ・有料ユーザーは広告なしの再生・一時停止・スキップが可能

# ⇒　ISPに違反している
# 　　AbstractMusicPlayerにサブクラスで使わないメソッドが定義されているため

from abc import ABC, abstractmethod


class AbstractMusicPlayer(ABC):
    def __init__(self, playlist: list) -> None:
        self.plyalist = playlist

    @abstractmethod
    def play(self) -> None:
        pass

    @abstractmethod
    def pause(self) -> None:
        pass

    @abstractmethod
    def skip(self) -> None:
        pass


class FreeUserPlayer(AbstractMusicPlayer):
    def play(self) -> None:
        print("広告あり")
        print("再生します")

    def pause(self) -> None:
        pass

    def skip(self) -> None:
        pass


class PaidUserPlayer(AbstractMusicPlayer):
    def play(self) -> None:
        print("再生します")

    def pause(self) -> None:
        print("一時停止します")

    def skip(self) -> None:
        print("スキップします")


playlist = []

free = FreeUserPlayer(playlist)
free.play()

paid = PaidUserPlayer(playlist)
paid.play()
paid.pause()
paid.skip()
