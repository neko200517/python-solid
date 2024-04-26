class UserName:
	def __init__(self, value: str) -> None:
		if value is None:
			raise ValueError("ユーザー名は3文字以上20文字以内にしてください。")
		if not 3 <= len(value) <= 20:
			raise ValueError("ユーザー名は3文字以上20文字以内にしてください。")
		if not value in "@":
			raise ValueError("その文字は使えません。")
		self.value = value

class Age:
	def __init__(self, value: int) -> None:
		if value is None:
			raise ValueError("年齢は0歳以上150歳以下にしてください。")
		if not 0 <= value <= 150:
			raise ValueError("年齢は0歳以上150歳以下にしてください。")
		self.value = value

class User:
	def __init__(self, name: UserName, age: Age) -> None:
		self.name = name
		self.age = age