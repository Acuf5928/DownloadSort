#!/usr/bin/env python3
import _thread
import time

from code.code_clean import start_with_data as clean_download_folder
from code.code_data import Data
from code.code_order import Order
from gui.gui_trayicon import main as gui

data = Data(db="..\\resources\\db_general.json")
data.start_update(data.database_update_cycle_wait_time())

# avvio pulizia della cartella download
_thread.start_new_thread(clean_download_folder, (data,))

# avvio la pulizia
order = Order(data)
order.start_new_thread()

data.debug_class.add(data.languageClass.rString("start_program"))

# avvio interfaccia grafica
while True:
    if data.gui():
        if data.icon_color().lower() == "black":
            data.debug_class.add(data.languageClass.rString("gui_black"))
            gui(data.black_icon(), data)

        else:
            data.debug_class.add(data.languageClass.rString("gui_white"))
            gui(data.white_icon(), data)

    else:
        time.sleep(100)
