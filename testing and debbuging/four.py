import logging

logging.basicConfig(level=logging.INFO, filename="log.log", filemode="w", format="%(asctime)s - %(levelname)s - %(message)s")
# logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)
hander = logging.FileHandler("test.log")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
hander.setFormatter(formatter)
logger.addHandler(hander)
logger.info("This is a custom logger message")