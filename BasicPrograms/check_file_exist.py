"""

@Author: Jayesh Dahiwale
@Date: 2022-04-13 07:38:00
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-12 19:00:00
@Title : Check File Exist

"""

import logging

logging.basicConfig(filename="sample.log", level=logging.INFO, format="%(levelname)s:%(message)s")

"""Below function check whether the file exists or not"""


def check_file_exist():

    try:
        my_file = open('main.py')
        my_file.close()
        logging.info("File found!")
    except FileNotFoundError:
        logging.error("File not found!")


if __name__ == "__main__":
    check_file_exist()