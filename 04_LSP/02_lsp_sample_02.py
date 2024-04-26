# 置換不可能なケース
class Bird:
    def fly(self) -> str:
        return "飛びます"


class Pengin(Bird):
    def fly(self) -> None:
        raise Exception("飛べません")


def bird_fly(bird: Bird):
    print(bird.fly())


bird = Bird()
pengin = Pengin()

bird_fly(bird)
bird_fly(pengin)  # 例外が発生する
