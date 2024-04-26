from abc import ABC, abstractmethod

# 通知のインタフェース
class AbstractNotification(ABC):
  # 継承したクラスは必ずこのメソッドをオーバーライドする必要がある
  @abstractmethod
  def send(self, user_id: id) -> None:
    pass

# 具体的な実装
class EmailNotification(AbstractNotification):
  def send(self, user_id: int) -> None:
    print("メール")

class SMSNotification(AbstractNotification):
  def send(self, user_id: int) -> None:
    print("SMS")

class PushNotification(AbstractNotification):
  def send(self, user_id: int) -> None:
    print("Push")

# 通知クライアント
def notify(user_id: int, notification: AbstractNotification):
  notification.send(user_id)

# 使用例
notifications = {
  "email": EmailNotification(),
  "sms": SMSNotification(),
  "push": PushNotification(),
}

notification_type = input("通知の種類を入力:")
notify(1, notifications[notification_type])