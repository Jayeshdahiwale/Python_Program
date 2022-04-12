"""

@Author: Jayesh Dahiwale
@Date: 2022-04-12 12:41:00
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-12 12:50:00
@Title : Stopwatch

"""
import time
import logging

logging.basicConfig(filename="sample.log", level=logging.INFO, format="%(levelname)s:%(message)s")

""" This function calculate the time taken to execute program"""


def stop_watch():
    try:
        start = input("Press 1 to start the stopWatch :")
        if start != "1":
            raise Exception("Entered wrong key.Press valid key")
    except Exception as e:
        print(e)
        logging.info(e)
        return stop_watch()
    begin = time.time()
    stop = input("Enter any key to stop the stopwatch: ")
    end = time.time()
    print(f"total time taken {end - begin}")
    logging.info(f"total time taken {end - begin}")


if __name__ == "__main__":
    stop_watch()
