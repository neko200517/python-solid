if __name__ == "__main__":
  i = 0
  while True:
    try:
      n = int(input("整数値を入力してください:"))
    except Exception:
      pass
    else: # tryの中で例外が発生した場合の処理
      print("正常な値が入力されました")
      print(n)
      break
    finally: # 例外の発生の有無によらず実行される処理
      i += 1

print(f"{i}回目の入力で成功しました")
