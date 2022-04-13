"""

@Author: Jayesh Dahiwale
@Date: 2022-04-13 07:38:00
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-12 19:00:00
@Title : Days Difference

"""

from datetime import date
import logging

logging.basicConfig(filename="sample.log", level=logging.INFO, format="%(levelname)s:%(message)s")

"""Below function calculates the difference between the given dates"""


def days_difference():
    f_date = [int(i) for i in input("Enter the first date in (yyyy,mm,dd) format :").split(",")]
    l_date = [int(i) for i in input("Enter the last date in (yyyy,mm,dd) format :").split(",")]
    f_date = date(f_date[0],f_date[1],f_date[2])
    l_date = date(l_date[0],l_date[1],l_date[2])
    delta = l_date - f_date
    logging.info(f"The difference between the dates is {delta.days} days")


if __name__ == "__main__":
    days_difference()
