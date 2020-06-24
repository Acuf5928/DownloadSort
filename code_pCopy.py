import os
import sys
import subprocess
import time
from shutil import copy, move


# Copia o sposta il file dato
# TO-DO Migliore documentazione sulla funzione pCopy
def pCopy(destination, source, data, createFolder=False, openFile=False, resolveConflict=True, secureMode=True, eliminateSource=True, firefoxWorkaround=True):
    sep = os.sep

    if os.path.isfile(destination):
        data.debug_class.add(str(time.asctime(time.localtime(time.time()))) + ": " + data.language_class.r_string(data.s_language(), "error_pcopy_1"), 1)
        return

    if not os.path.isfile(source):
        data.debug_class.add(str(time.asctime(time.localtime(time.time()))) + ": " + data.language_class.r_string(data.s_language(), "error_pcopy_2"), 1)
        return

    if not os.path.exists(source):
        return

    if firefoxWorkaround:
        try:
            if os.path.getsize(source) == 0:
                return
        except Exception:
            pass

    if not os.path.exists(destination):
        if createFolder:
            try:
                checkFolder(destination)
                data.debug_class.add(str(time.asctime(time.localtime(time.time()))) + ": " + data.language_class.r_string(data.s_language(), "pcopy_1"))
            except Exception as ex:
                data.debug_class.add(str(time.asctime(time.localtime(time.time()))) + ": " + data.language_class.r_string(data.s_language(), "error_pcopy_3") + "\n" +str(ex), 1)
        else:
            data.debug_class.add(str(time.asctime(time.localtime(time.time()))) + ": " + data.language_class.r_string(data.s_language(), "error_pcopy_4"), 1)
            return

    if destination[-1] != sep:
        destination += sep

    name = source.split(sep)[-1]
    destinationPath = destination + name

    if os.path.exists(destinationPath):
        if resolveConflict:
            ext = name.split(".")[-1]
            temp = name.split(".")
            name = temp[0]

            for a in range(1, len(temp) - 1):
                name = name + "." + temp[a]

            n = 1

            destinationPath = destination + name + "(" + str(n) + ")." + ext

            while os.path.exists(destinationPath):
                n += 1
                destinationPath = destination + name + "(" + str(n) + ")." + ext
            data.debug_class.add(str(time.asctime(time.localtime(time.time()))) + ": " + data.language_class.r_string(data.s_language(), "pcopy_2") + destinationPath)

        elif secureMode:
            data.debug_class.add(str(time.asctime(time.localtime(time.time()))) + ": " + data.language_class.r_string(data.s_language(), "pcopy_3"))
            return

        else:
            data.debug_class.add(str(time.asctime(time.localtime(time.time()))) + ": " + data.language_class.r_string(data.s_language(), "pcopy_4"))

    if not eliminateSource:
        copy(source, destinationPath)
        data.debug_class.add(str(time.asctime(time.localtime(time.time()))) + ": " + data.language_class.r_string(data.s_language(),"pcopy_5") + source + data.language_class.r_string(data.s_language(), "destination") + destinationPath)

    else:
        move(source, destinationPath)
        data.debug_class.add(str(time.asctime(time.localtime(time.time()))) + ": " + data.language_class.r_string(data.s_language(),"pcopy_6") + source + data.language_class.r_string(data.s_language(), "destination") + destinationPath)

    if openFile:
        try:
            if sys.platform == "win32":
                os.startfile(destinationPath)
            else:
                opener = "open" if sys.platform == "darwin" else "xdg-open"
                subprocess.call([opener, destinationPath])
        except Exception as es:
            data.debug_class.add(str(time.asctime(time.localtime(time.time()))) + ": " + data.language_class.r_string(data.s_language(), "error_pcopy_5") + str(es), 1)

        data.debug_class.add(str(time.asctime(time.localtime(time.time()))) + ": " + data.language_class.r_string(data.s_language(), "pcopy_7") + destinationPath)

    return destinationPath


# se la cartella data non esiste la crea
def checkFolder(path):
    if not os.path.isdir(path):
        os.makedirs(path)
