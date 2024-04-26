# ④スマートホームのシステムについて考えてみましょう
# 　・家を出るときには電灯とエアコンを消してカーテンを閉める
# 　・家に帰ってきたときには電灯とエアコンをつけてカーテンを開ける
# 上記の2つの手順をそれぞれ１つのメソッドだけで完了するようにするには、
# 次のコードにどのような変更を加えればよいでしょうか。

# class Light:
#   def turn_on(self):
#     print("電灯がオンになりました")

#   def turn_off(self):
#     print("電灯がオフになりました")

# class AirConditioner:
#   def turn_on(self):
#     print("エアコンがオンになりました")

#   def turn_off(self):
#     print("エアコンがオフになりました")

# class Curtain:
#   def open(self):
#     print("カーテンを開けました")

#   def close(self):
#     print("カーテンを閉めました")

class Light:
  def turn_on(self):
    print("電灯がオンになりました")

  def turn_off(self):
    print("電灯がオフになりました")

class AirConditioner:
  def turn_on(self):
    print("エアコンがオンになりました")

  def turn_off(self):
    print("エアコンがオフになりました")

class Curtain:
  def open(self):
    print("カーテンを開けました")

  def close(self):
    print("カーテンを閉めました")

class SmartHomeFacade():
  def __init__(self):
    self.light = Light()
    self.air_conditioner = AirConditioner()
    self.curtain = Curtain()

  def leave_home(self):
    self.light.turn_on()
    self.air_conditioner.turn_on()
    self.curtain.open()

  def return_home(self):
    self.light.turn_off()
    self.air_conditioner.turn_off()
    self.curtain.close()

smart_home_facade = SmartHomeFacade()
smart_home_facade.leave_home()
smart_home_facade.return_home()