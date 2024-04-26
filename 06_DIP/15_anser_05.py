# ⑤次のコードはDIPに違反しているでしょうか
# 違反している場合はその理由を述べたうえでDIPを満たすようにコードを改善してください

# ⇒　依存性の抽入パターンを使用しているがユースケースがリポジトリに依存しているためDIPに違反している

from abc import ABC, abstractmethod


# ユーザーを表現するクラス
class User:
    def __init__(self, id: int, name: str) -> None:
        self.id = id
        self.name = name


class UserRepository(ABC):
    @abstractmethod
    def save(self, user: User) -> None:
        pass

    @abstractmethod
    def get(self, id: int) -> User:
        pass


# RDBへのアクセスを担当するクラス
class RDBUserRepository(UserRepository):
    def save(self, user: User) -> None:
        print(f"Save {user.name} to the RDB")

    def get(self, id: int) -> User:
        print(f"Get user from the RDB by id {id}")
        return User(id, "user_name")


# ユーザーに関するユースケースを実現するクラス
class UserApplicationService:
    def __init__(self, repository: UserRepository) -> None:
        self.user_repository = repository

    def crate(self, id: int, name: str) -> None:
        user = User(id, name)
        self.user_repository.save(user)

    def get(self, id: int) -> User:
        return self.user_repository.get(id)


rdb = RDBUserRepository()
service = UserApplicationService(rdb)
service.crate(1, "ユーザー")
user = service.get(1)
print(f"{user.id}, {user.name}")
