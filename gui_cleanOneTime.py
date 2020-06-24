import sys
import time
import _thread
import code_data
import code_startOneTime
import gui_persoanlLineEdit
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QCoreApplication, QDir, QSize, Qt, pyqtSlot
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
                             QLineEdit, QListWidget, QListWidgetItem,
                             QMainWindow, QMenu, QPushButton, QSystemTrayIcon,
                             QVBoxLayout, QWidget, QListWidget, QAction,
                             QErrorMessage, QMessageBox,
                             QFileDialog)

class clean(QMainWindow):
    def __init__(self, icon):
        super().__init__()
        self.setWindowIcon(icon)
        self.setMinimumSize(QSize(600, 100))
        self.setMaximumSize(QSize(600, 100))

    def initUI(self):
        self.setWindowTitle(self.data.language_class.r_string(self.data.s_language(), "cleanTrayIcon"))

        # Create textbox
        self.textbox = gui_persoanlLineEdit.LineEdit(self)
        self.textbox.set_data(self.data)
        self.textbox.resize(480, 30)

        # Create a button in the window
        self.button = QPushButton(self.data.language_class.r_string(self.data.s_language(), "start"), self)
        self.button.clicked.connect(self.start)
        
        self.cb = QCheckBox(self.data.language_class.r_string(self.data.s_language(), "cleanTrayIcon_message_1"), self)
        self.cb1 = QCheckBox(self.data.language_class.r_string(self.data.s_language(), "cleanTrayIcon_message_2"), self)

        self.text = QLabel(self.data.language_class.r_string(self.data.s_language(), "cleanTrayIcon_message"), self)
        
        self.text2 = QLabel(self.data.language_class.r_string(self.data.s_language(), "ok"), self)
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
        self.data.debug_class.add(str(time.asctime( time.localtime(time.time()) )) + ": "+ self.data.language_class.r_string(self.data.s_language(), "cleanTrayIcon_message_debug") + ": path: " + self.textbox.text() + ": clean: " + str(self.cb.isChecked()) + ": open: " + str(self.cb1.isChecked())) 
        code_startOneTime.startOneTime(self.textbox.text(), self.cb.isChecked(), self.cb1.isChecked())
        self.text2.setVisible(True)
        _thread.start_new_thread(self.c, ())
    
    def c(self):
        time.sleep(5)
        self.text2.setVisible(False)
        
    def closeEvent(self, event):
        self.hide()
        event.ignore()
       