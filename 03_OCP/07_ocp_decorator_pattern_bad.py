# よくない設計

# ベースのコーヒークラス
class Coffee:
  @property
  def cost(self) -> int:
    return 200

  @property
  def description(self) -> str:
    return "コーヒー"

# 生クリームをトッピングしたコーヒー
class CreamCofee(Coffee):
  @property
  def cost(self) -> int:
    return super().cost + 50

  @property
  def description(self) -> str:
    return f"{super().description}、生クリーム"

# バニラアイスをトッピングしたコーヒー
class VanillaCofee(Coffee):
  @property
  def cost(self) -> int:
    return super().cost + 70

  @property
  def description(self) -> str:
    return f"{super().description}、バニラアイス"

cream_cofee = CreamCofee()
print(cream_cofee.cost)
print(cream_cofee.description)

vanilla_cofee = VanillaCofee()
print(vanilla_cofee.cost)
print(vanilla_cofee.description)