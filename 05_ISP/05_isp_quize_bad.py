# 以下の複合機を表現するコードはISPに違反しているでしょうか

# 複合機クラスがクライアント側から見て不要なメソッドを公開してしまっているのでISPに違反している
# ⇒　PrinterClientでcopy_documentを呼び出す可能性がある
# ⇒　CopyClientでprint_documentを呼び出す可能性がある


# ドキュメントの値オブジェクト
class Document:
    def __init__(self) -> None:
        pass


# 複合機クラス
class MultifunctionPrinter:
    def print_document(self, document: Document) -> None:
        print("プリントを開始します")

    def copy_document(self, document: Document) -> None:
        print("コピーを開始します")


# クライアント
class PrintClient:
    def __init__(self, printer: MultifunctionPrinter) -> None:
        self.printer = printer

    def execute(self, document: Document) -> None:
        self.printer.print_document(document)


class CopyClient:
    def __init__(self, printer: MultifunctionPrinter) -> None:
        self.printer = printer

    def execute(self, document: Document) -> None:
        self.printer.copy_document(document)
