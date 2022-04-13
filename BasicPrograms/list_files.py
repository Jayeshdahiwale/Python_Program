"""

@Author: Jayesh Dahiwale
@Date: 2022-04-13 07:38:00
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-12 19:00:00
@Title : List All File

"""

import logging
from os import listdir
from os.path import isfile, join

logging.basicConfig(filename="sample.log", level=logging.INFO, format="%(levelname)s:%(message)s")

"""Below function list all the the files in  directory"""

def list_files():
    files_list = [f for f in listdir(r"C:\Users\SR COMPUTER\Documents\BridzeLabs\CFP\Python_Program\BasicPrograms") if isfile(join(r"C:\Users\SR COMPUTER\Documents\BridzeLabs\CFP\Python_Program\BasicPrograms", f))]
    logging.info(files_list);

if __name__ == "__main__":
    list_files()