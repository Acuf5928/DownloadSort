import _thread
import os
import time

import win32con
import win32event
import win32file

import code_helper
from code_pCopy import pCopy


class Order:
    def __init__(self, data):
        self.data = data

    def start_new_thread(self):
        _thread.start_new_thread(self.startBackground, ())

    def set_folderPath(self, path):
        self.folderPath = path

    def set_openFile(self, openF):
        self.open_file_copied = openF

    def startBackground(self):
        self.folderPath = os.path.abspath(self.data.DownloadFolderPath())
        self.change_handle = win32file.FindFirstChangeNotification(self.folderPath, 0, win32con.FILE_NOTIFY_CHANGE_FILE_NAME)
        self.folderPath += "\\"

        try:
            while True:
                result = win32event.WaitForSingleObject(self.change_handle, 500)

                if result == win32con.WAIT_OBJECT_0:
                    self.open_file_copied = self.data.open_file_copied()
                    self.start()

        except Exception as es:
            self.data.debug_class.add(self.data.language_class.r_string(self.data.s_language(), "copy_error") + "\n" + self.data.language_class.r_string(self.data.s_language(), "error") + str(es), 1)

        finally:
            win32file.FindCloseChangeNotification(self.change_handle)
            self.startBackground()

    def start(self):
        formati = self.data.formati()

        # ottengo la lista dei file presenti nella cartella download
        fileList = code_helper.list_file(self.folderPath + "*")

        # se non ci sono file da copiare mi fermo qui
        if len(fileList) <= 0:
            exit()

        # analizza i file e li copia nella cartella corretta
        for Type in formati:
            for ext in formati[Type]:
                for Element in fileList:
                    if Element.lower().endswith(ext):
                        try:
                            pCopy(self.folderPath + Type, Element, self.data, self.data.create_folder(), self.open_file_copied)
                            # self.data.debug_class.add(str(time.asctime(self.data.language_class.r_string(self.data.s_language(), "copy_file") + str(Element) + "\n" + self.data.language_class.r_string(self.data.s_language(), "dst") + str(folderPath + Type))
                            # commentata perchè riddondante, già presente in pcopy

                        except Exception as es:
                            self.data.debug_class.add(
                                self.data.language_class.r_string(self.data.s_language(), "copy_error") + str(Element) + "\n" + self.data.language_class.r_string(self.data.s_language(), "dst") + str(
                                    self.folderPath + Type) + self.data.language_class.r_string(self.data.s_language(), "error") + str(es), 1)
