import code_helper
import time
import os
import _thread

def start_with_data(data):
    while True:
        if data.clean_folder_path() == True:
            folder_to_clean = data.DownloadFolderPath()
            time_difference = data.clean_time_difference()
            wait_time = data.clean_wait_time()
            start(folder_to_clean + "**", time_difference, data)
        time.sleep(wait_time)
    
def start(folder_to_clean, time_difference, data):
    '''Funzione che pulisce la cartella data come input eliminando i file più vecchi del tempo dato'''

    #ottengo la lista di file e cartelle
    files = code_helper.list_file(folder_to_clean, recursivee= True, folder = True)
        
    #ottengo l'orario attuale
    time_now = time.time()

    for file in files:
        #ottengo la differenza in sec tra creazione del file e l'orario attuale
        try:
            diff = time_now - code_helper.creation_date(file)
        except Exception as es:
            data.debug_class.add(str(time.asctime( time.localtime(time.time()) )) + ": " + data.language_class.r_string(data.s_language(), "clean_diff_error") + str(es), 1)
            break

        if diff > time_difference:
            #se la differenza supera il limite si prova a rimuovere il file
            try:
                os.remove(file)
                data.debug_class.add(str(time.asctime( time.localtime(time.time()) )) + ": " + data.language_class.r_string(data.s_language(), "clean_file_removed") + str(file))
                
            except Exception:
                #se fallisce provo ad agire come fosse una cartella
                try:
                    os.rmdir(file)
                    data.debug_class.add(str(time.asctime( time.localtime(time.time()) )) + ": " + data.language_class.r_string(data.s_language(), "clean_folder_removed") + str(file))

                except Exception:
                    pass
                #se la cartella ha dei file o cartelle all'interno l'eliminazione fallisce