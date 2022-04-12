"""

@Author: Jayesh Dahiwale
@Date: 2022-04-12 18:41:00
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-12 19:00:00
@Title : Display Colors

"""
import logging

logging.basicConfig(filename="sample.log", level=logging.INFO, format="%(levelname)s:%(message)s")
""" This function displays the first color and last color"""


def display_colors():
    colors = ["Red", "Green", "White", "Black"]
    logging.info(colors[0])
    logging.info(colors[len(colors) - 1])
    print(colors[0])
    print(colors[len(colors) - 1])


if __name__ == "__main__":
    display_colors()
