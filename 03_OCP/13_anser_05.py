# ⑤④の解答のコードに料金が70%になるシニア割引のデコレータを追加してください。

from abc import ABC, abstractmethod

class AbstractRoomFee(ABC):
  @abstractmethod
  def cost(self, hours: int) -> int:
    pass

class RoomFeeDecorator(AbstractRoomFee, ABC):
  def __init__(self, decorated_customer: AbstractRoomFee) -> None:
    self.decorated_customer = decorated_customer

  def cost(self, hours: int) -> int:
    return super().cost(hours)

class RoomFee(AbstractRoomFee):
  def cost(self, hours: int) -> int:
    return int(hours * 700 * 1.0)

class StudentDecorator(RoomFeeDecorator):
  def cost(self, hours: int):
    return int(self.decorated_customer.cost(hours) * 0.8)

class MemberDecorator(RoomFeeDecorator):
  def cost(self, hours: int):
    return int(self.decorated_customer.cost(hours) * 0.9)

class SeniorDecorator(RoomFeeDecorator):
  def cost(self, hours: int):
    return int(self.decorated_customer.cost(hours) * 0.7)

hours = 2
fee = RoomFee()
print(f"一般料金：{fee.cost(hours)}円")

student = StudentDecorator(fee)
print(f"学生料金：{student.cost(hours)}円")

member = MemberDecorator(fee)
print(f"会員料金：{member.cost(hours)}円")

senior = SeniorDecorator(fee)
print(f"シニア料金：{senior.cost(hours)}円")

student_member = MemberDecorator(student)
print(f"学生＋会員料金：{student_member.cost(hours)}円")

senior_member = MemberDecorator(senior)
print(f"シニア＋会員料金：{senior_member.cost(hours)}円")