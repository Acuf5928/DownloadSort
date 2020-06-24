import argparse
import os


def startOneTime(path, clean, openF):
    from code_clean import start as clean_download_folder
    from code_order import Order
    from code_data import Data as db

    if os.path.isdir(path):
        try:
            if path[-1] != "\\" and os.name == "nt":
                path = path + "\\"

            if path[-1] != "/" and os.name != "nt":
                path = path + "/"

            data = db(db="db_general.json")

            if clean:
                folder_to_clean = path
                time_difference = data.clean_time_difference()
                clean_download_folder(folder_to_clean + "**", time_difference, data)

            # avvio la pulizia
            order = Order(data)
            order.set_folderPath(path)
            order.set_openFile(openF)
            order.start()

        except Exception as es:
            print(es)


if __name__ == "__main__":
    parser = argparse.ArgumentParser("usage prog -p <folder path>")
    parser.add_argument('-p', dest='path', type=str, help='specify folder path')
    parser.add_argument('-c', dest='clean', type=str, help='specify if you want delete old file [true/false]')
    parser.add_argument('-o', dest='open', type=str, help='specify if you want open file [true/false]')
    options = parser.parse_args()

    try:
        if isinstance(options.open, str) == False or isinstance(options.path, str) == False or isinstance(options.clean, str) == False:
            raise Exception

    except:
        print(parser.print_help())
        exit()

    print("\nOptions:\nPath: " + options.path.lower() + "\nClean: " + options.clean.lower() + "\nOpen file: " + options.open.lower() + "\n")

    if input("Continue? [Y/n]\t") == "Y":
        if options.open.lower() == "true":
            openF = True
        else:
            openF = False

        if options.clean.lower() == "true":
            clean = True
        else:
            clean = False

        startOneTime(options.path.lower(), clean, openF)
