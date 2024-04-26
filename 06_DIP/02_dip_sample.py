from abc import ABC, abstractmethod


class AbstractNotification(ABC):  # 抽象クラス
    @abstractmethod
    def send(self, user_id: int) -> None:
        pass


class EmailNotification(AbstractNotification):  # 具象クラス
    def send(self, user_id: int) -> None:
        print("Email")


class SMSNotification(AbstractNotification):  # 具象クラス
    def send(self, user_id: int) -> None:
        print("SMS")


def notify(notify: AbstractNotification, user_id: int) -> None:
    notify.send(user_id)
