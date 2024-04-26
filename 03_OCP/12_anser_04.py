# ④あるカラオケ店の料金計算システムについて考えてみよう

# このカラオケ店では、次のような料金システムになっているものとする
# ・利用時間は1時間単位
# ・基本料金は1時間当たり700円
# ・学生は料金が基本料金の80％になる
# ・会員は料金が基本料金の90％になる
# ・学生割引と会員割引は併用できる

# 以下のコードをSOLID原則の観点から見た問題点を指摘した上で、Decoratorパターンを適用して問題を解決してください。

# def calcurate_fee(hours: int, is_student: bool, is_member: bool) -> int:
#   base_rate: int = 700
#   discount_rate: float = 1.0

#   if is_student and is_member:
#     discount_rate = 0.8 * 0.9
#   elif is_student:
#     discount_rate = 0.8
#   elif is_member:
#     discount_rate = 0.9

#   total_fee: int = int(hours * base_rate * discount_rate)
#   return total_fee

# hours: int = 2
# is_student: bool = True
# is_member: bool = True

# fee: int = calcurate_fee(hours, is_student, is_member)
# print(f"カラオケ店の料金は：{fee}円")

# 問題点：
# 一つの関数内で判定と計算の責務を2つ背負っている：SRPの違反
# 会員の種類が増えたときなど拡張性に弱い：OCPの違反

from abc import ABC, abstractmethod

class AbstractRoomFee(ABC):
  @abstractmethod
  def cost(self, hours: int) -> int:
    pass

class BaseRoomFee(AbstractRoomFee):
  def cost(self, hours: int) -> int:
    return int(hours * 700 * 1.0)

class RoomFeeDecorator(AbstractRoomFee, ABC):
  def __init__(self, decorated_customer: AbstractRoomFee) -> None:
    self.decorated_customer = decorated_customer

  @abstractmethod
  def cost(self, hours: int) -> int:
    pass

class StudentDecorator(RoomFeeDecorator):
  def cost(self, hours: int):
    return int(self.decorated_customer.cost(hours) * 0.8)

class MemberDecorator(RoomFeeDecorator):
  def cost(self, hours: int):
    return int(self.decorated_customer.cost(hours) * 0.9)

def calcurator_fee(hour: int, fee=AbstractRoomFee) -> int:
  print(f"カラオケ店の料金は：{fee.cost(hour)}円")

hours = 2
base = BaseRoomFee()
calcurator_fee(hours, base)
calcurator_fee(hours, StudentDecorator(base))
calcurator_fee(hours, MemberDecorator(base))
calcurator_fee(hours, MemberDecorator(StudentDecorator(base)))
