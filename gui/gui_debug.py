import _thread
import time

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import (QCheckBox, QHBoxLayout, QMainWindow, QPushButton, QVBoxLayout, QWidget, QListWidget, QMessageBox,
                             QFileDialog)


class Debug(QMainWindow):
    def __init__(self, icon):
        QMainWindow.__init__(self)
        self.setWindowIcon(icon)
        self.setMinimumSize(QSize(700, 400))
        self.setMaximumSize(QSize(700, 400))
        self.index = 0
        self.ContinueRefresh = True
        self.view_error = False

    def initUI(self):
        self.setWindowTitle(self.data.languageClass.rString("debug"))

        # Creo i campi di testo
        self.text1 = QListWidget()

        self.checkbox = QCheckBox((self.data.languageClass.rString("view_only_error")), self)
        self.checkbox.stateChanged.connect(self.error_select)

        # Setup OK button
        self.button1 = QPushButton(self.data.languageClass.rString("clean"), self)
        self.button1.clicked.connect(self.clean)

        self.button2 = QPushButton(self.data.languageClass.rString("update"), self)
        self.button2.clicked.connect(self.update)

        self.button3 = QPushButton(self.data.languageClass.rString("save_on_file"), self)
        self.button3.clicked.connect(self.save)

        self.exit_button = QPushButton(self.data.languageClass.rString("exit"), self)
        self.exit_button.clicked.connect(self.closeEvent)

        # Creo i diversi layout
        myQWidget = QWidget()
        self.setCentralWidget(myQWidget)

        VerticalLayoutA = QVBoxLayout()
        HorizontalLayoutA = QHBoxLayout()

        HorizontalLayoutA.addWidget(self.button1)
        HorizontalLayoutA.addWidget(self.button2)
        HorizontalLayoutA.addWidget(self.button3)
        HorizontalLayoutA.addWidget(self.exit_button)

        VerticalLayoutA.addWidget(self.text1)
        VerticalLayoutA.addWidget(self.checkbox)
        VerticalLayoutA.addLayout(HorizontalLayoutA)

        myQWidget.setLayout(VerticalLayoutA)

        _thread.start_new_thread(self.update_rec, ())

    def set_data(self, data):
        self.data = data

    def error_select(self):
        if not self.checkbox.isChecked():
            self.view_error = False
        else:
            self.view_error = True

        self.index = 0
        self.text1.clear()
        self.update()

    def save(self):
        try:
            with open(self.saveFileDialog(), "a") as ptrfile:
                for element in self.data.debug_class.return_data():
                    ptrfile.write(element + "\n")
            QMessageBox.question(
                self,
                self.data.languageClass.rString("title"),
                self.data.languageClass.rString("save_complete"),
                QMessageBox.Cancel)

            self.data.debug_class.add(self.data.languageClass.rString("export_file"))

        except Exception as ex:
            self.data.debug_class.add(self.data.languageClass.rString("export_error") + str(ex), 1)

    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self, self.data.languageClass.rString("debug"), "", "All files(*)", options=options)
        return fileName

    def update_rec(self, sec=5):
        self.index = 0

        while self.ContinueRefresh:
            self.update()
            time.sleep(sec)

    def update(self):
        tempIndex = 0
        for item in self.data.debug_class.return_data().items():
            if tempIndex == self.index:
                if self.view_error and item[1] == 1:
                    self.text1.addItem(item[0])
                    self.index += 1

                if not self.view_error:
                    self.text1.addItem(item[0])
                    self.index += 1

            tempIndex += 1

        if self.index == 0:
            self.text1.clear()
            self.text1.addItem(self.data.languageClass.rString("no_element"))

    def clean(self):
        self.index = 0
        self.text1.clear()
        self.data.debug_class.clean()
        self.update()

    def closeEvent(self, event):
        self.ContinueRefresh = False
        self.hide()

        try:
            event.ignore()
        except:
            pass