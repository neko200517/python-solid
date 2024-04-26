if __name__ == "__main__":
  try:
    n = int(input("整数値を入力してください:"))
    print(n)
  except ValueError: # 具体的な例外
    print("入力エラー：整数値を入力してください")