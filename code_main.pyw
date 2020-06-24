#!/usr/bin/env python3
import time
import _thread

from code_clean import start_with_data as clean_download_folder
from gui_trayicon import main as gui
from code_order import order
from code_data import data

data = data(db = "db_general.json")
data.start_update(data.database_update_cycle_wait_time())

#avvio pulizia della cartella download
_thread.start_new_thread(clean_download_folder, (data, ))

#avvio la pulizia
order = order(data)
order.start_new_thread()

data.debug_class.add(str(time.asctime( time.localtime(time.time()) )) + ": " + data.language_class.r_string(data.s_language(), "start_program")) 

#avvio interfaccia grafica
while True:
    if data.gui():
        if data.icon_color().lower() == "black":
            data.debug_class.add(str(time.asctime( time.localtime(time.time()) )) + ": "+ data.language_class.r_string(data.s_language(), "gui_black")) 
            gui(data.black_icon(), data)
    
        else:
            data.debug_class.add(str(time.asctime( time.localtime(time.time()) )) + ": "+ data.language_class.r_string(data.s_language(), "gui_white"))
            gui(data.white_icon(), data)

    else:
        time.sleep(100)