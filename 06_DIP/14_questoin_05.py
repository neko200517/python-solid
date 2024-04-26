# ⑤次のコードはDIPに違反しているでしょうか
# 違反している場合はその理由を述べたうえでDIPを満たすようにコードを改善してください


# ユーザーを表現するクラス
class User:
    def __init__(self, id: int, name: str) -> None:
        self.id = id
        self.name = name


# RDBへのアクセスを担当するクラス
class RDBUserRepository:
    def save(self, user: User) -> None:
        print(f"Save {user.name} to the RDB")

    def get(self, id: int) -> User:
        print(f"Get user from the RDB by id {id}")
        return User(id, "user_name")


# ユーザーに関するユースケースを実現するクラス
class UserApplicationService:
    def __init__(self) -> None:
        self.user_repository = RDBUserRepository()

    def crate(self, id: int, name: str) -> None:
        user = User(id, name)
        self.user_repository.save(user)

    def get(self, id: int) -> None:
        self.user_repository.get(id)
