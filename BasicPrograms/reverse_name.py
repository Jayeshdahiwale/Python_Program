"""

@Author: Jayesh Dahiwale
@Date: 2022-04-12 18:41:00
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-12 19:00:00
@Title : reverse_name

"""
import logging

logging.basicConfig(filename="sample.log", level=logging.INFO, format="%(levelname)s:%(message)s")


def reverse_name():
    full_name = input("Enter your first name & last name separated by space :").split(" ")
    reversed_names = []
    for name in full_name:
        reverse = []
        for i in reversed(range(len(name))):
            reverse.append(name[i])
        reversed_names.append("".join(reverse))
    print(" ".join(reversed_names))
    logging.info(" ".join(reversed_names))


if __name__ == "__main__":
    reverse_name()
