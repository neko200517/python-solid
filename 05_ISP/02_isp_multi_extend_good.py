# 多重継承
from abc import ABC, abstractmethod


# 共通のインタフェース
class Cource(ABC):
    @abstractmethod
    def view_lecture(self) -> None:
        pass


# 講師専用のインタフェース
class InstructorCourceInterface(ABC):
    @abstractmethod
    def add_lecture(self, countent_name: str) -> None:
        pass


## 生徒専用のインタフェース
class StudentsCourceInterface(ABC):
    @abstractmethod
    def review_cource(self) -> None:
        pass


# 講師クラス
class CourseFromInstructors(
    Cource, InstructorCourceInterface
):  # 共通のインタフェースと講師専用インタフェースを多重継承
    def view_lecture(self) -> None:
        print("視聴を開始します")

    def add_lecture(self, countent_name: str) -> None:
        print(f"新規レクチャー「{countent_name}」を作成しました")


# 生徒クラス
class CourseFromStudents(
    Cource, StudentsCourceInterface
):  # 共通のインタフェースと生徒専用インタフェースを多重継承
    def view_lecture(self) -> None:
        print("視聴を開始します")

    def review_cource(self) -> None:
        print("コースのレビューをお願いします")
