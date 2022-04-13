"""

@Author: Jayesh Dahiwale
@Date: 2022-04-13 07:38:00
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-12 19:00:00
@Title : Calender

"""
import calendar
import logging

logging.basicConfig(filename="sample.log", level=logging.INFO, format="%(levelname)s:%(message)s")

"""Below function prints the calender using month nd year"""


def calender():
    y = int(input("Input the year : "))
    m = int(input("Input the month : "))
    logging.info(calendar.month(y, m))


if __name__ == "__main__":
    calender()
