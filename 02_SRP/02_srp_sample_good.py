# 動画を表現するクラス
class Video:
  def __init__(self, title: str, file_name: str) -> None:
    self.title = title
    self.file_name = file_name
    self.comments: list[tuple[str, str]] = []

# 動画のアップロード
class VideoUploader:
  def upload(self, video: Video) -> None:
    print(f"{video.title}がアップロードされました。")

# 動画の再生
class VideoPlayer:
  def play(self, video: Video) -> None:
    print(f"{video.title}を再生します。")

# コメントの登録
class CommentPost:
  def post_comment(self, video: Video, user_name: str, comment: str) -> None:
    video.comments.append((user_name, comment))
    print(f"{user_name}が次のコメントを投稿しました:{comment}")

video = Video("video", "video.mp4")

videoUploader = VideoUploader()
videoUploader.upload(video)

videoPlayer = VideoPlayer()
videoPlayer.play(video)

commnetPost = CommentPost()
commnetPost.post_comment(video, "user", "comment")