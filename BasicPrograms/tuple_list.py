"""

@Author: Jayesh Dahiwale
@Date: 2022-04-12 18:41:00
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-12 19:00:00
@Title : tuple_list

"""
import logging

logging.basicConfig(filename="sample.log", level=logging.INFO, format="%(levelname)s:%(message)s")


def tuple_list():
    numbers = input("enter the numbers separated by commas :").split(",")
    tuple_numbers = tuple(numbers)
    list_numbers = list(numbers)
    print(tuple_numbers,list_numbers)
    logging.info(tuple_numbers)
    logging.info(list_numbers)

if __name__== "__main__":
    tuple_list()
