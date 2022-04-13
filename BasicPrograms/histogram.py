"""

@Author: Jayesh Dahiwale
@Date: 2022-04-13 07:38:00
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-12 19:00:00
@Title : Histogram

"""

import logging

logging.basicConfig(filename="sample.log", level=logging.INFO, format="%(levelname)s:%(message)s")

"""Below function takes the list of elements as an argument and return the histogram """


def histogram(items):
    for n in items:
        output = ''
        times = n
        while times > 0:
            output += '*'
            times = times - 1
        logging.info(output)


if __name__ == "__main__":
    histogram([2, 4, 7, 9])
