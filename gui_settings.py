import time

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import (QHBoxLayout, QLabel,
                             QLineEdit, QMainWindow, QPushButton, QVBoxLayout, QWidget, QErrorMessage, QMessageBox)

import code_data


class Settings(QMainWindow):
    def __init__(self, icon):
        QMainWindow.__init__(self)
        self.icon = icon
        self.setWindowIcon(self.icon)
        self.setMinimumSize(QSize(500, 500))
        self.setMaximumSize(QSize(500, 500))

    def initUI(self):
        self.setWindowTitle(self.data.language_class.r_string(self.data.s_language(), "settings"))

        # Creo i diversi layout
        myQWidget = QWidget()
        self.setCentralWidget(myQWidget)

        VerticalLayoutA = QVBoxLayout()
        HorizontalLayoutA = QHBoxLayout()
        VerticalLayoutBS = QVBoxLayout()

        # Creo i campi di testo
        self.text1 = QLabel("DownloadFolderPath: ", self)
        self.text2 = QLabel("order_cycle_wait_time: ", self)
        self.text4 = QLabel("clean_folder_path: ", self)
        self.text5 = QLabel("clean_time_difference: ", self)
        self.text6 = QLabel("clean_wait_time: ", self)
        self.text7 = QLabel("open_file_copied: ", self)
        self.text9 = QLabel("database_update_cycle_wait_time: ", self)
        self.text14 = QLabel("language: ", self)
        VerticalLayoutBS.addWidget(self.text1)
        VerticalLayoutBS.addWidget(self.text2)
        VerticalLayoutBS.addWidget(self.text4)
        VerticalLayoutBS.addWidget(self.text5)
        VerticalLayoutBS.addWidget(self.text6)
        VerticalLayoutBS.addWidget(self.text7)
        VerticalLayoutBS.addWidget(self.text9)
        VerticalLayoutBS.addWidget(self.text14)

        VerticalLayoutBD = QVBoxLayout()
        # Creo i campi da riempire
        self.textbox1 = QLineEdit()
        self.textbox2 = QLineEdit()
        self.textbox4 = QLineEdit()
        self.textbox5 = QLineEdit()
        self.textbox6 = QLineEdit()
        self.textbox7 = QLineEdit()
        self.textbox9 = QLineEdit()
        self.textbox14 = QLineEdit()
        VerticalLayoutBD.addWidget(self.textbox1)
        VerticalLayoutBD.addWidget(self.textbox2)
        VerticalLayoutBD.addWidget(self.textbox4)
        VerticalLayoutBD.addWidget(self.textbox5)
        VerticalLayoutBD.addWidget(self.textbox6)
        VerticalLayoutBD.addWidget(self.textbox7)
        VerticalLayoutBD.addWidget(self.textbox9)
        VerticalLayoutBD.addWidget(self.textbox14)

        HorizontalLayoutA.addLayout(VerticalLayoutBS)
        HorizontalLayoutA.addLayout(VerticalLayoutBD)

        self.textAllert = QLabel(self.data.language_class.r_string(self.data.s_language(), "after_restart"), self)

        HorizontalLayoutB = QHBoxLayout()
        VerticalLayoutCS = QVBoxLayout()

        self.text3 = QLabel("sep: ", self)
        self.text8 = QLabel("create_folder: ", self)
        self.text10 = QLabel("gui: ", self)
        self.text11 = QLabel("icon_color: ", self)
        self.text12 = QLabel("debug_clean_time: ", self)
        self.text13 = QLabel("debug_clean_element: ", self)
        VerticalLayoutCS.addWidget(self.text3)
        VerticalLayoutCS.addWidget(self.text8)
        VerticalLayoutCS.addWidget(self.text10)
        VerticalLayoutCS.addWidget(self.text11)
        VerticalLayoutCS.addWidget(self.text12)
        VerticalLayoutCS.addWidget(self.text13)

        VerticalLayoutCD = QVBoxLayout()
        self.textbox3 = QLineEdit()
        self.textbox8 = QLineEdit()
        self.textbox10 = QLineEdit()
        self.textbox11 = QLineEdit()
        self.textbox12 = QLineEdit()
        self.textbox13 = QLineEdit()
        VerticalLayoutCD.addWidget(self.textbox3)
        VerticalLayoutCD.addWidget(self.textbox8)
        VerticalLayoutCD.addWidget(self.textbox10)
        VerticalLayoutCD.addWidget(self.textbox11)
        VerticalLayoutCD.addWidget(self.textbox12)
        VerticalLayoutCD.addWidget(self.textbox13)

        HorizontalLayoutB.addLayout(VerticalLayoutCS)
        HorizontalLayoutB.addLayout(VerticalLayoutCD)

        HorizontalLayoutC = QHBoxLayout()

        self.button1 = QPushButton(self.data.language_class.r_string(self.data.s_language(), "save"), self)
        self.button1.clicked.connect(self.save_button)

        self.button2 = QPushButton(self.data.language_class.r_string(self.data.s_language(), "reset"), self)
        self.button2.clicked.connect(self.reset)

        self.exit_button = QPushButton(self.data.language_class.r_string(self.data.s_language(), "exit"), self)
        self.exit_button.clicked.connect(self.hide)

        HorizontalLayoutC.addWidget(self.button1)
        HorizontalLayoutC.addWidget(self.button2)
        HorizontalLayoutC.addWidget(self.exit_button)

        VerticalLayoutA.addLayout(HorizontalLayoutA)
        VerticalLayoutA.addWidget(self.textAllert)
        VerticalLayoutA.addLayout(HorizontalLayoutB)
        VerticalLayoutA.addLayout(HorizontalLayoutC)

        myQWidget.setLayout(VerticalLayoutA)

        self.textbox1.setText(str(self.data.DownloadFolderPath()))
        self.textbox2.setText(str(self.data.order_cycle_wait_time()))
        self.textbox3.setText(str(self.data.sep()))
        self.textbox4.setText(str(self.data.clean_folder_path()))
        self.textbox5.setText(str(self.data.clean_time_difference()))
        self.textbox6.setText(str(self.data.clean_wait_time()))
        self.textbox7.setText(str(self.data.open_file_copied()))
        self.textbox8.setText(str(self.data.create_folder()))
        self.textbox9.setText(str(self.data.database_update_cycle_wait_time()))
        self.textbox10.setText(str(self.data.gui()))
        self.textbox11.setText(str(self.data.icon_color()))
        self.textbox12.setText(str(self.data.debug_clean_time()))
        self.textbox13.setText(str(self.data.debug_clean_element()))
        self.textbox14.setText(str(self.data.s_language()))

    def reset(self):
        check = QMessageBox()
        check.setWindowIcon(self.icon)
        check.setWindowTitle(self.data.language_class.r_string(self.data.s_language(), "settings"))
        check.setText(self.data.language_class.r_string(self.data.s_language(), "cont"))
        check.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        check = check.exec()

        if check == QMessageBox.Yes:
            try:
                self.data.set_cont(False)
                self.imp_pred = code_data.data("db_general_defaulf.json")
                self.imp_pred.update(0)
                self.data.set_all(self.imp_pred.return_all())

            except Exception as ex:
                self.data.debug_class.add(str(time.asctime(time.localtime(time.time()))) + ": " + self.data.language_class.r_string(self.data.s_language(), "db_error") + str(ex), 1)

            finally:
                self.data.set_cont(True)
                self.data.start_update(self.data.database_update_cycle_wait_time())
                self.data.save()
                self.main.set_menu()
                self.initUI()

    def set_data(self, data):
        self.data = data

    def set_main(self, new):
        self.main = new

    def save_button(self):
        check = QMessageBox()
        check.setWindowIcon(self.icon)
        check.setWindowTitle(self.data.language_class.r_string(self.data.s_language(), "settings"))
        check.setText(self.data.language_class.r_string(self.data.s_language(), "cont2"))
        check.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        check = check.exec()

        if check == QMessageBox.Yes:
            self.data.set_cont(False)

            try:
                if self.textbox1.text() != self.data.DownloadFolderPath():
                    self.data.set_DownloadFolderPath(self.textbox1.text())

                if self.textbox3.text() != self.data.sep():
                    self.data.set_sep(self.textbox3.text())

                if self.textbox4.text().lower() == "true":
                    self.data.set_clean_folder_path(True)

                elif self.textbox4.text().lower() == "false":
                    self.data.set_clean_folder_path(False)

                if self.textbox7.text().lower() == "true":
                    self.data.set_open_file_copied(True)

                elif self.textbox7.text().lower() == "false":
                    self.data.set_open_file_copied(False)

                if self.textbox8.text().lower() == "true":
                    self.data.set_create_folder(True)

                elif self.textbox8.text().lower() == "false":
                    self.data.set_create_folder(False)

                if self.textbox10.text().lower() == "true":
                    self.data.set_gui(True)

                elif self.textbox10.text().lower() == "false":
                    self.data.set_gui(False)

                self.data.set_clean_time_difference(int(self.textbox5.text()))
                self.data.set_clean_wait_time(int(self.textbox6.text()))
                self.data.set_order_cycle_wait_time(int(self.textbox2.text()))
                self.data.set_database_update_cycle_wait_time(int(self.textbox9.text()))
                self.data.set_icon_color(self.textbox11.text())
                self.data.set_debug_clean_time(int(self.textbox12.text()))
                self.data.set_debug_clean_element(int(self.textbox13.text()))
                self.data.set_language(str(self.textbox14.text()))
                self.data.save()
                self.textAllert.setText(self.data.language_class.r_string(self.data.s_language(), "after_restart"))
                self.setWindowTitle(self.data.language_class.r_string(self.data.s_language(), "settings"))
                self.button1.setText(self.data.language_class.r_string(self.data.s_language(), "save"))
                self.button2.setText(self.data.language_class.r_string(self.data.s_language(), "reset"))
                self.exit_button.setText(self.data.language_class.r_string(self.data.s_language(), "exit"))
                close = QMessageBox()
                close.setWindowIcon(self.icon)
                close.setWindowTitle(self.data.language_class.r_string(self.data.s_language(), "settings"))
                close.setText(self.data.language_class.r_string(self.data.s_language(), "save_complete_2"))
                close.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                close = close.exec()

                if close == QMessageBox.Yes:
                    self.hide()

            except Exception as ex:
                self.data.debug_class.add(str(time.asctime(time.localtime(time.time()))) + ": " + self.data.language_class.r_string(self.data.s_language(), "db_error") + str(ex), 1)
                error_dialog = QErrorMessage()
                error_dialog.setWindowIcon(self.icon)
                error_dialog.setWindowTitle(self.data.language_class.r_string(self.data.s_language(), "settings"))
                error_dialog.showMessage(str(ex))

            finally:
                self.data.set_cont(True)
                self.data.start_update(self.data.database_update_cycle_wait_time())
                self.main.set_menu()

    def closeEvent(self, event):
        self.hide()
        event.ignore()
