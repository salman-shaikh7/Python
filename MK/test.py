#basic python function

def add(a, b):
    return a + b

import logging
logging.basicConfig(level=logging.INFO)

from loguru import logger
def main():
    result = add(5, 3)
    logging.info(f"The result of adding 5 and 3 is: {result}")
    logger.info(f"The result of adding 5 and 3 is: {result}")

main()




