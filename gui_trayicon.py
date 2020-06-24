import sys

from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QMenu)

import gui_aboutme
import gui_cleanOneTime
import gui_debug
import gui_settings


class SystemTrayIcon(QtWidgets.QSystemTrayIcon):

    def __init__(self, icon, parent=None):
        QtWidgets.QSystemTrayIcon.__init__(self, icon, parent)
        self.menu = QMenu(parent)
        self.icon = icon

    def set_data(self, data):
        self.data = data

    def set_menu(self):
        self.menu.clear()
        Debug = self.menu.addAction(self.data.language_class.r_string(self.data.s_language(), "debug"))
        Debug.triggered.connect(self.debug)

        settingAction = self.menu.addAction(self.data.language_class.r_string(self.data.s_language(), "settings"))
        settingAction.triggered.connect(self.settings)

        cleanOneTime = self.menu.addAction(self.data.language_class.r_string(self.data.s_language(), "cleanTrayIcon"))
        cleanOneTime.triggered.connect(self.cleanOneTime)

        self.pause = self.menu.addAction(self.data.language_class.r_string(self.data.s_language(), "pause"))
        self.pause.triggered.connect(self.set_pause)

        aboutme = self.menu.addAction(self.data.language_class.r_string(self.data.s_language(), "aboutme"))
        aboutme.triggered.connect(self.aboutme)

        exitAction = self.menu.addAction(self.data.language_class.r_string(self.data.s_language(), "exit"))
        exitAction.triggered.connect(self.exit)

        self.setContextMenu(self.menu)

    def set_pause(self):
        if self.data.order() == True:
            self.data.set_order(False)
            self.pause.setText(self.data.language_class.r_string(self.data.s_language(), "pause"))

        elif self.data.order() == False:
            self.data.set_order(True)
            self.pause.setText(self.data.language_class.r_string(self.data.s_language(), "resume"))

    def debug(self):
        self.window = gui_debug.Debug(self.icon)
        self.window.set_data(self.data)
        self.window.initUI()
        self.window.show()

    def settings(self):
        self.window = gui_settings.Settings(self.icon)
        self.window.set_data(self.data)
        self.window.initUI()
        self.window.set_main(self)
        self.window.show()

    def cleanOneTime(self):
        self.window = gui_cleanOneTime.clean(self.icon)
        self.window.set_data(self.data)
        self.window.initUI()
        self.window.show()

    def aboutme(self):
        self.window = gui_aboutme.AboutMe(self.icon)
        self.window.set_data(self.data)
        self.window.initUI()
        self.window.show()

    def exit(self):
        sys.exit()


def main(image, data):
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    trayIcon = SystemTrayIcon(QIcon(image), w)
    trayIcon.set_data(data)
    trayIcon.set_menu()
    trayIcon.show()
    sys.exit(app.exec_())
