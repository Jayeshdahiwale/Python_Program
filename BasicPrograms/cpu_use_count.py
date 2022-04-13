"""

@Author: Jayesh Dahiwale
@Date: 2022-04-13 07:38:00
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-12 19:00:00
@Title : CPU using Count

"""

import logging
import multiprocessing

logging.basicConfig(filename="sample.log", level=logging.INFO, format="%(levelname)s:%(message)s")

"""This function calculates the total number of cpu count"""


def cpu_count():
    logging.info(multiprocessing.cpu_count())


if __name__ == "__main__":
    cpu_count()