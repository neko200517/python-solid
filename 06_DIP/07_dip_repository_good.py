# クラスを適用した方法
class User:
    def __init__(self, name: str) -> None:
        self.name = name


# Repositoryパターン
class SQLiteUserRepository:
    def add(self, user: User) -> None:
        # 中略：データベースに接続
        query = f"INSERT INTO users (name) VALUES ('{user.name}')"
        # 中略：データベースの開放


# ユーザーのユースケースを表現するクラス
class UserApplicationService:
    def __init__(self) -> None:
        self.repository = SQLiteUserRepository()

    def register_user(self, name: str) -> None:
        user = User(name)
        self.repository.add(user)


# 使用例
user_application_service = UserApplicationService()
user_application_service.register_user("User")
