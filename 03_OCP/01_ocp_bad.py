class Notification:
  def send(self, notification_type: str, user_id: int):
    if notification_type == "email":
      print("メール")
    elif notification_type == "sms":
      print("SMS")
    elif notification_type == "push":
      print("プッシュ通知")

notification = Notification()
notification.send("sms", 123)
notification.send("push", 456)