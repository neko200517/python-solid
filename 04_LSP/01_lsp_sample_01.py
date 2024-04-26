# 置換可能なケース
class Bird:
    def fly(self) -> str:
        return "飛びます"


class Pengin(Bird):
    def fly(self) -> str:
        return "飛べません"


def bird_fly(bird: Bird):
    print(bird.fly())


bird = Bird()
pengin = Pengin()

# 基本型と派生型を同様に扱えている
bird_fly(bird)
bird_fly(pengin)
