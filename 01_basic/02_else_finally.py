if __name__ == "__main__":
    i = 0
    while True:
        try:
            n = int(input("整数値を入力してください:"))
        except ValueError:
            print("入力エラー：整数値を入力してください")
        else:  # tryの中で例外が発生した場合の処理
            print("正常な値が入力されました")
            print(n)
            break
        finally:  # 例外の発生の有無によらず実行される処理
            i += 1

print(f"{i}回目の入力で成功しました")

try:
    input("")
except:
    pass
