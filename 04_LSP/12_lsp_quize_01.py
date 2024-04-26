# ①次のコードはLSPに違反しているか

# 自分の回答：
# 正方形はwidth, heightが同じ値でなければならないという事前条件があるため、
# 派生型が基本型の事前条件を強めているというLSPの違反がるため違反している。

# A.
# ⇒クライアントを見ないと判断できない


class Rectangle:  # 長方形クラス
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    def area(self) -> int:
        return self.width * self.height


class Square(Rectangle):  # 正方形クラス
    def __init__(self, side: int) -> None:
        super().__init__(side, side)
