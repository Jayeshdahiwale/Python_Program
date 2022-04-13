"""

@Author: Jayesh Dahiwale
@Date: 2022-04-13 07:38:00
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-12 19:00:00
@Title : Check_Value_Present

"""

import logging

logging.basicConfig(filename="sample.log", level=logging.INFO, format="%(levelname)s:%(message)s")

""" Below function checks whether the given value is preset in the group of value"""


def check_value_present():
    group_of_values = [int(i) for i in input("Enter the group of values sep by comma :").split(",")]
    value = int(input("Enter the value :"))

    if value in group_of_values:
        logging.info(f"The value is present in group")
    else:
        logging.info(f"The value is not present in group")


if __name__ == "__main__":
    check_value_present()