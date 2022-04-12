"""

@Author: Jayesh Dahiwale
@Date: 2022-04-12 13:11:00
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-12 13:11:00
@Title : Quadratic

"""
import logging

logging.basicConfig(filename="sample.log", level=logging.INFO, format="%(levelname)s:%(message)s")

"""This function calculates the roots of quadratic eqn """


def quadratic_roots():
    coefficient = input("Enter the coeff of Quadratic eqn separated by comma :").split(",")
    a = int(coefficient[0])
    b = int(coefficient[1])
    c = int(coefficient[2])
    delta = b * b - 4 * a * c
    if delta < 0:
        print("Root not exist")
        logging.info("Root not exist")
        return
    root_one = (-b + delta ** 0.5) / (2 * a)
    root_two = (-b - delta ** 0.5) / (2 * a)
    logging.info(f"1st Root is {root_one} & Second root is {root_two}")
    print(f"1st Root is {root_one} & Second root is {root_two}")


if __name__ == "__main__":
    quadratic_roots()
