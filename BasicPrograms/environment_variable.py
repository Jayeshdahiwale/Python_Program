"""

@Author: Jayesh Dahiwale
@Date: 2022-04-13 07:38:00
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-12 19:00:00
@Title : Environment Variable

"""

import logging
import os

logging.basicConfig(filename="sample.log", level=logging.INFO, format="%(levelname)s:%(message)s")


def access_env_var():
    # Access all environment variables
    logging.info('*----------------------------------*')
    logging.info(os.environ)
    logging.info('*----------------------------------*')
    logging.info('*----------------------------------*')
    logging.info(os.environ['PATH'])
    logging.info('*----------------------------------*')



if __name__ == "__main__":
    access_env_var()