# SRPを満たすように関数を3つに分割

# データを処理する関数
def format_data(data: list[str]) -> list[int]:
  # 責務１：データの整形
  formatted_data: list[int] = []
  for item in data:
    if item.isdigit(): # 文字列が数値かどうかを判定
      formatted_data.append(int(item))
  return formatted_data

# 責務２：データの処理
def calculate_data(data: list[int]) -> tuple[int, float]:
  if len(data):
    total: int = sum(data)
    average: float = total / len(data)
  else:
    total: int = 0
    average: float = 0.0
  return total, average

# 責務３：フォーマットした結果の出力
def print_processed_result(data: list[str]) -> None:
  formated_data: list[int] = format_data(data)
  total, average = calculate_data(formated_data)

  print(f"合計:{total}")
  print(f"平均:{average}")

data = ["1", "2", "3"]
print_processed_result(data)
