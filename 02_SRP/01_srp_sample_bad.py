# 動画を表現するクラス
class Video:
  def __init__(self, title: str, file_name: str) -> None:
    self.title = title
    self.file_name = file_name
    self.comments: list[tuple[str, str]] = []

# 動画の処理を行うクラス
class VideoController:
  # 動画のアップロード
  def upload_video(self, video: Video) -> None:
    print(f"{video.title}がアップロードされました。")

  # 動画の再生
  def play_video(self, video: Video) -> None:
    print(f"{video.title}を再生します。")

  # コメントの登録
  def post_comment(self, video: Video, user_name: str, comment: str) -> None:
    video.comments.append((user_name, comment))
    print(f"{user_name}が次のコメントを投稿しました:{comment}")