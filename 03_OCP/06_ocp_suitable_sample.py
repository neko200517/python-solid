# 現時点でユーザーが1種類しかないといった例の場合、OCPの設計をあえて採用しない手もある


class User:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
