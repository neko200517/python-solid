# ④以下の音楽ストリーミングサービスのコードはISPに違反しているでしょうか。
# 違反している場合はその理由を述べ、ISPを満たすようなコードに改善してください。

# この音楽ストリーミングサービスでは
# 無料ユーザーと有料ユーザーで使用できる機能が異なります
# ・無料ユーザーは広告ありの再生のみが可能
# ・有料ユーザーは広告なしの再生・一時停止・スキップが可能

# ⇒　ISPに違反している
# 　　AbstractMusicPlayerにサブクラスで使わないメソッドが定義されているため


class FreeMusicPlayerBehavior:
    def play(self) -> None:
        print("広告あり")
        print("再生します")


class PaidMusicPlayerBehavior:
    def play(self) -> None:
        print("再生します")

    def pause(self) -> None:
        print("一時停止します")

    def skip(self) -> None:
        print("スキップします")


class FreeUserPlayer:
    def __init__(self, playlist: list) -> None:
        self.behavior = FreeMusicPlayerBehavior()

    def play(self) -> None:
        self.behavior.play()


class PaidUserPlayer:
    def __init__(self, playlist: list) -> None:
        self.behavior = PaidMusicPlayerBehavior()

    def play(self) -> None:
        self.behavior.play()

    def pause(self) -> None:
        self.behavior.pause()

    def skip(self) -> None:
        self.behavior.skip()


playlist = []

free = FreeUserPlayer(playlist)
free.play()

paid = PaidUserPlayer(playlist)
paid.play()
paid.pause()
paid.skip()
