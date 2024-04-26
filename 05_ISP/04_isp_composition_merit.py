from abc import ABC, abstractmethod


class Course(ABC):
    @abstractmethod
    def view_lecture(self) -> None:
        pass


class StudentBehavior(ABC):
    @abstractmethod
    def review_course(self) -> None:
        pass


class FreeStudentBehavior(StudentBehavior):
    def review_course(self) -> None:
        print("無料で入手したコースにはレビューできません")


class PaidStudentBehavior(StudentBehavior):
    def review_course(self) -> None:
        print("コースのレビューをお願いします")


# コンストラクタで生徒の種別を選択
class CourceFromStudents(Course):
    def __init__(self, student_behavior: StudentBehavior) -> None:
        self.student_behavior = student_behavior

    def view_lecture(self) -> None:
        print("視聴を開始します")

    def review_course(self) -> None:
        self.student_behavior.review_course()


free = FreeStudentBehavior()
student = CourceFromStudents(free)
student.view_lecture()
student.review_course()

paid = PaidStudentBehavior()
student = CourceFromStudents(paid)
student.view_lecture()
student.review_course()
