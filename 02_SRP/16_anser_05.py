# ⑤メールアドレスを表現する値オブジェクトを作成してみましょう
# 　ただしメールアドレスの値は次の条件を満たすものとする
# 　　・メールアドレスは必ず「＠」を含む
# 　　・メールアドレスの「＠」の前には少なくとも1文字以上、後ろには少なくとも2文字以上の文字列がある


class MailAddress:
    def __init__(self, value: str) -> None:
        if not "@" in value:
            raise ValueError("メールアドレスには必ず@マークが必要です。")
        local, domain = value.split("@")
        if not len(local) >= 1 or not len(domain) >= 2:
            raise ValueError("メールアドレスの「@」の前には少なくとも1文字以上、後ろには少なくとも2文字以上必要です。")
        self.mail_address = value

    def __str__(self) -> str:
        return self.mail_address


mail_address = MailAddress("t@ga")
print(mail_address)
