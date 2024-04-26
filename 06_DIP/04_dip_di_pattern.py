from abc import ABC, abstractmethod


class AbstractNotification(ABC):  # 抽象クラス
    @abstractmethod
    def send(send, user_id: int) -> None:
        pass


class EmailNotification(AbstractNotification):  # 具象クラス
    def send(send, user_id: int) -> None:
        print("Email")


class SMSNotification(AbstractNotification):  # 具象クラス
    def send(send, user_id: int) -> None:
        print("SMS")


# どの具象クラスに依存するかは定義時にはまだ決まっていない
def notify(user_id: int, notification: AbstractNotification):
    notification.send(user_id)


notification1 = EmailNotification()
notification2 = SMSNotification()

# 関数の呼び出し時に具象クラスへの依存を注入する
notify(1, notification1)
notify(2, notification2)
