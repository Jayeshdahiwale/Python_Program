"""

@Author: Jayesh Dahiwale
@Date: 2022-04-11 21:30:00
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-11 21:45:30
@Title : Power of Two

"""
"""
It gives the power of two of the numbers till given input number
"""


def power_of_two():
    number = int(input("Enter the number between 0 and 31: "))
    for i in range(number):
        print(2 ** i)


power_of_two()
