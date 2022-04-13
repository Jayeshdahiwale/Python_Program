"""

@Author: Jayesh Dahiwale
@Date: 2022-04-13 07:38:00
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-12 19:00:00
@Title : External command caller

"""
import os
from subprocess import call
import logging

logging.basicConfig(filename="sample.log", level=logging.INFO, format="%(levelname)s:%(message)s")

"""Below function call the external command outside python"""


def call_ext_command():
    logging.info(os.system("ls -a"))

if __name__ == "__main__":
    call_ext_command()