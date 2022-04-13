"""

@Author: Jayesh Dahiwale
@Date: 2022-04-13 07:38:00
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-12 19:00:00
@Title : List_to_String

"""

import logging

logging.basicConfig(filename="sample.log", level=logging.INFO, format="%(levelname)s:%(message)s")

"""Below function takes the argument list of elemenets and convert them to string"""


def list_to_string(list_elements):
    logging.info("".join(list_elements))


if __name__=="__main__":
    list_to_string(["J","a","y","e","s","h"])