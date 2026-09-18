import logging

logging.basicConfig(level=logging.INFO, filename="log.log", filemode="w", format="%(asctime)s - %(levelname)s - %(message)s")
# logging.basicConfig(level=logging.INFO)

try:
    x = 1 / 0

except ZeroDivisionError as e:
    logging.error(f"An error occurred: {e}", exc_info=True)
