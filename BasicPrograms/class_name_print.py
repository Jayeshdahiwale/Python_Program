"""

@Author: Jayesh Dahiwale
@Date: 2022-04-12 18:41:00
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-12 19:00:00
@Title : BuilIn Discritpiton

"""
import logging

logging.basicConfig(filename="sample.log", level=logging.INFO, format="%(levelname)s:%(message)s")


def builtin_description():
    name = abs
    print(abs.__module__)
    print(abs.__doc__)


if __name__ == "__main__":
    builtin_description()
