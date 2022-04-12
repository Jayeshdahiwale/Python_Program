"""

@Author: Jayesh Dahiwale
@Date: 2022-04-12 13:38:00
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-12 13:38:00
@Title : WindChill

"""
import logging

logging.basicConfig(filename="sample.log", level=logging.INFO, format="%(levelname)s:%(message)s")


def windchill():
    temp = float(input("Enter the temperature lesser than  or equal to 50 : "))
    vel = float(input("Enter the velocity greater than or equal to 3 or less than or equal to 120: "))
    try:
        if temp > 50 or vel < 3 or vel > 120:
            raise Exception("Enter the correct parameters")
    except Exception as e:
        print(e)
        logging.info(e)
        return windchill()
    # w refers to windchill
    w = 35.74 + 0.6215 * temp + (0.4275 * temp - 35.75) * vel ** 0.16
    print(f"The windchill is {w}")
    logging.info(f"The windchill is {w}")


if __name__ == "__main__":
    windchill()
