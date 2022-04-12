"""

@Author: Jayesh Dahiwale
@Date: 2022-04-12 11:22:00
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-12 22:00:00
@Title : Distance Calculater

"""
import logging

logging.basicConfig(filename="sample.log", level=logging.INFO, format="%(levelname)s:%(message)s")

"""
Below function calculate the euclidean distance of a point from origin
"""
def distance():
    try:
        inputs = input("Enter the two integers separated by comma :").split(",")
        x = int(inputs[0])
        y = int(inputs[1])
    except Exception as e:
        logging.info(e)
        print("Please enter two numbers in integer format")
        return distance()
    print(f"The distance from origin is {(x ** 2 + y ** 2) ** 0.5}")
    logging.info(f"The distance from origin is {(x ** 2 + y ** 2) ** 0.5}")


if __name__ == "__main__":
    distance()
