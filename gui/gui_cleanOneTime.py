import _thread
import time

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import (QCheckBox, QHBoxLayout, QLabel,
                             QMainWindow, QPushButton, QVBoxLayout, QWidget)

from code import code_startOneTime
from gui import gui_persoanlLineEdit


class Clean(QMainWindow):
    def __init__(self, icon):
        super().__init__()
        self.setWindowIcon(icon)
        self.setMinimumSize(QSize(600, 100))
        self.setMaximumSize(QSize(600, 100))

    def initUI(self):
        self.setWindowTitle(self.data.languageClass.rString("cleanTrayIcon"))

        # Create textbox
        self.textbox = gui_persoanlLineEdit.LineEdit(self)
        self.textbox.set_data(self.data)
        self.textbox.resize(480, 30)

        # Create a button in the window
        self.button = QPushButton(self.data.languageClass.rString("start"), self)
        self.button.clicked.connect(self.start)

        self.cb = QCheckBox(self.data.languageClass.rString("cleanTrayIcon_message_1"), self)
        self.cb1 = QCheckBox(self.data.languageClass.rString("cleanTrayIcon_message_2"), self)

        self.text = QLabel(self.data.languageClass.rString("cleanTrayIcon_message"), self)

        self.text2 = QLabel(self.data.languageClass.rString("ok"), self)
        self.text2.setVisible(False)

        VerticalLayout = QVBoxLayout()
        HorizontalLayout = QHBoxLayout()

        HorizontalLayout.addWidget(self.cb)
        HorizontalLayout.addWidget(self.cb1)
        HorizontalLayout.addWidget(self.text2)
        HorizontalLayout.addWidget(self.button)

        VerticalLayout.addWidget(self.textbox)
        VerticalLayout.addLayout(HorizontalLayout)
        VerticalLayout.addWidget(self.text)

        myQWidget = QWidget()
        self.setCentralWidget(myQWidget)
        myQWidget.setLayout(VerticalLayout)

        self.show()

    def set_data(self, data):
        self.data = data

    def start(self):
        self.data.debug_class.add(self.data.languageClass.rString("cleanTrayIcon_message_debug") + ": path: " + self.textbox.text() + ": clean: " + str(self.cb.isChecked()) + ": open: " + str(self.cb1.isChecked()))
        code_startOneTime.startOneTime(self.textbox.text(), self.cb.isChecked(), self.cb1.isChecked())
        self.text2.setVisible(True)
        _thread.start_new_thread(self.c, ())

    def c(self):
        time.sleep(5)
        self.text2.setVisible(False)

    def closeEvent(self, event):
        self.hide()
        event.ignore()
