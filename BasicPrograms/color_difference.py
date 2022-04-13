"""

@Author: Jayesh Dahiwale
@Date: 2022-04-13 07:38:00
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-12 19:00:00
@Title : Color_difference

"""

import logging

logging.basicConfig(filename="sample.log", level=logging.INFO, format="%(levelname)s:%(message)s")

""" This function return the color present in first set not present in other set"""


def color_difference():
    color_list_one = set(["White", "Black", "Red"])
    color_list_two = set(["Red", "Green"])
    differnce = color_list_one.difference(color_list_two)
    logging.info(differnce)

if __name__ == "__main__":
    color_difference()