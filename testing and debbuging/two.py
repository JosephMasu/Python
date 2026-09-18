import logging

logging.basicConfig(level=logging.INFO, filename="log.log", filemode="w", format="%(asctime)s - %(levelname)s - %(message)s")
# logging.basicConfig(level=logging.INFO)

x = 2

logging.info(f"This is a debug message, x = {x}")