# 1.次のコードの問題点を指摘し、適切な形にせよ
#
# try:
#   x = int(input("整数を入力してください："))
#   result = 10 / x
#   print("結果：", result)
# except Exception:
#   pass

result = 0
try:
  x = int(input("整数を入力してください："))
  result = 10 / x
except ValueError:
  print("整数を入力してください")
except ZeroDivisionError:
  print("0で除算できません")
else:
  print("結果：", result)