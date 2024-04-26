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

email_notification = EmailNotification()
email_notification.send(123)

sms_notification = SMSNotification()
sms_notification.send(456)

push_notification = PushNotification()
push_notification.send(678)