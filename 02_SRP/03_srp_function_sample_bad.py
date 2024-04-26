# データを処理する関数（3つの責務を持つ）
def process_data(data: list[str]) -> None:\
  # 責務１：データの整形
  formatted_data: list[int] = []
  for item in data:
    if item.isdigit(): # 文字列が数値かどうかを判定
      formatted_data.append(int(item))

  # 責務２：データの処理
  if len(formatted_data):
    total: int = sum(formatted_data)
    average: float = total / len(formatted_data)
  else:
    total: int = 0
    average: float = 0.0

  # 責務３：フォーマットした結果の出力
  print(f"合計:{total}")
  print(f"平均:{average}")

data = ["1", "2", "3"]
process_data(data)