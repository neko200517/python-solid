# ②次のコードはLSPに違反しているか
# adjust_width関数から見たときに、LSPに違反しているか？

# 自分の回答：
# adjust_widthにSquareが来た時にLSPに違反する。
# widthしか変更していないためheightとwidthの値が一致せず正方形として成り立たなくため
# 正方形の事前条件に違反していることになる。そのためLSPに違反している。


class Rectangle:  # 長方形クラス
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    def area(self) -> int:
        return self.width * self.height


class Square(Rectangle):  # 正方形クラス
    def __init__(self, side: int) -> None:
        super().__init__(side, side)


def adjust_width(rectangle: Rectangle, new_width: int) -> None:
    print(f"初期の面積：{rectangle.area()}")
    rectangle.width = new_width
    print(f"幅を調整後の面積：{rectangle.area()}")


def print_area(rectanble: Rectangle) -> None:
    print(f"面積：{rectangle.area()}")


rectangle = Rectangle(5, 10)
adjust_width(rectangle, 7)

square = Square(5)
adjust_width(square, 7)  # 5 * 7 = 35: 期待した結果と異なる
