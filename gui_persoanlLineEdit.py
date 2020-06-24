import os

from PyQt5.QtWidgets import (QLineEdit)


class LineEdit(QLineEdit):
    def __init__(self, parent):
        super().__init__(parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):
        e.accept()

    def set_data(self, data):
        self.data = data

    def dropEvent(self, e):
        text = e.mimeData().text()
        text = text.replace("file:///", "")

        if os.name == "nt":
            text = text.replace("/", "\\")

        self.setText(text)
