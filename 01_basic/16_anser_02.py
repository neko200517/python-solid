# 2.以下のコードにおいて次の値をinput()に入力したときの出力はそれぞれどうなるか
#
# 1
# 0
# a

try:
  x = int(input(""))
  result = 10 / x
  print("try")
except ValueError:
  print("ValueError")
except ZeroDivisionError:
  print("ZeroDivisionError")
else:
  print("else")
finally:
  print("finally")

# 1: try, else, finally
# 0: ZeroDivisionError, finally
# a: ValueError, finally