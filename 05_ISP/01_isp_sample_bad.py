from abc import ABC, abstractmethod


class Cource(ABC):
    # 共通のメソッド
    @abstractmethod
    def view_lecture(self) -> None:
        pass

    # 更新専用のメソッド
    @abstractmethod
    def add_lecture(self, countent_name: str) -> None:
        pass

    # 生徒専用のメソッド
    @abstractmethod
    def review_cource(self) -> None:
        pass


# 講師クラス
class CourseFromInstructors(Cource):
    def view_lecture(self) -> None:
        print("視聴を開始します")

    def add_lecture(self, countent_name: str) -> None:
        print(f"新規レクチャー「{countent_name}」を作成しました")

    def review_cource(self) -> None:
        pass  # 講師はレビューできないので実装しない


# 生徒クラス
class CourseFromStudents(Cource):
    def view_lecture(self) -> None:
        print("視聴を開始します")

    def add_lecture(self, countent_name: str) -> None:
        pass  # 生徒はレクチャーを追加できないので実装しない

    def review_cource(self) -> None:
        print("コースのレビューをお願いします")
