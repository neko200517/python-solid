# 最悪の方法（SQLをコードにべた書き）
class User:
    def __init__(self, name: str) -> None:
        self.name = name


class UserApplicationService:
    # ユーザーの新規作成
    def register_user(self, name: str) -> None:
        user = User(name)

        # 中略：データベースに接続

        query = f"INSERT INTO users (name) VALUES ('{user.name}')"

        # 中略：データベースの開放


# 使用例
user_application_service = UserApplicationService()
user_application_service.register_user("User")
