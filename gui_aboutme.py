import sys
import time
import _thread
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QCoreApplication, QDir, QSize, Qt, pyqtSlot
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
                             QLineEdit, QListWidget, QListWidgetItem,
                             QMainWindow, QMenu, QPushButton, QSystemTrayIcon,
                             QVBoxLayout, QWidget, QListWidget, QAction,
                             QErrorMessage, QMessageBox,
                             QFileDialog)

class AboutMe(QMainWindow):
    def __init__(self, icon):
        QMainWindow.__init__(self)
        self.setWindowIcon(icon)
        self.setMinimumSize(QSize(950, 250))
        self.setMaximumSize(QSize(950, 250))

    def initUI(self):
        self.setWindowTitle(self.data.language_class.r_string(self.data.s_language(), "aboutme"))

        #Creo i diversi layout
        myQWidget = QWidget()
        self.setCentralWidget(myQWidget)
        VerticalLayoutBS = QVBoxLayout()
        
        #Creo i campi di testo
        with open("README.md", "r") as file:
            text = file.readlines()

        for element in text:
            self.element = QLabel(element, self)
            VerticalLayoutBS.addWidget(self.element)
        
        myQWidget.setLayout(VerticalLayoutBS)
    
    def set_data(self, data):
        self.data = data
        
    def closeEvent(self, event):
        self.hide()
        event.ignore()
