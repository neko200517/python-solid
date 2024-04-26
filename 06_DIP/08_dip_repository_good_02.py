from abc import ABC, abstractmethod


# クラスを適用した方法
class User:
    def __init__(self, name: str) -> None:
        self.name = name


# リポジトリを抽象化する
class AbstractUserRepository(ABC):
    @abstractmethod
    def add(self, user: User) -> None:
        pass


# SQLiteリポジトリ
class SQLiteUserRepository(AbstractUserRepository):
    def add(self, user: User) -> None:
        # 中略：データベースに接続
        query = f"INSERT INTO users (name) VALUES ('{user.name}')"
        # 中略：データベースの開放


# テスト用リポジトリ
class MockUserRepository(AbstractUserRepository):
    def __init__(self) -> None:
        self.users = []

    def add(self, user: User) -> None:
        self.users.append(user)


# ユーザーのユースケースを表現するクラス
class UserApplicationService:
    def __init__(self, repository: AbstractUserRepository) -> None:  # 抽象に依存、DIパターン
        self.repository = repository

    def register_user(self, name: str) -> None:
        user = User(name)
        self.repository.add(user)


# 使用例
sqlite_repository = SQLiteUserRepository()
user_application_service = UserApplicationService(sqlite_repository)
user_application_service.register_user("User")

mock_repository = MockUserRepository()
user_application_service = UserApplicationService(mock_repository)
user_application_service.register_user("User")
