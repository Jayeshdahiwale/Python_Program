"""

@Author: Jayesh Dahiwale
@Date: 2022-04-11 21:17:00
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-11 21:30:30
@Title : Flip_Coin

"""
"""
This function returns whether the year is leap or not
"""


def leap_year():
    year = int(input("Enter the year :"))
    if year // 1000 < 1:
        print("Enter the four digit number")
        return leap_year()
    if year % 400 == 0:
        print("This is a leap year")
    elif year % 100 == 0:
        print("This is not a leap year")
    elif year % 4 == 0:
        print("This is a leap year")
    else:
        print("This is not a leap year")

leap_year()