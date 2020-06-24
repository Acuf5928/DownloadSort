#!/usr/bin/env python3
import _thread
import time

from code_clean import start_with_data as clean_download_folder
from code_data import Data
from code_order import Order
from gui_trayicon import main as gui

data = Data(db="db_general.json")
data.start_update(data.database_update_cycle_wait_time())

# avvio pulizia della cartella download
_thread.start_new_thread(clean_download_folder, (data,))

# avvio la pulizia
order = Order(data)
order.start_new_thread()

data.debug_class.add(data.language_class.r_string(data.s_language(), "start_program"))

# avvio interfaccia grafica
while True:
    if data.gui():
        if data.icon_color().lower() == "black":
            data.debug_class.add(data.language_class.r_string(data.s_language(), "gui_black"))
            gui(data.black_icon(), data)

        else:
            data.debug_class.add(data.language_class.r_string(data.s_language(), "gui_white"))
            gui(data.white_icon(), data)

    else:
        time.sleep(100)
