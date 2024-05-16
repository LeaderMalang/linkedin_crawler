import logging
from webdriver_manager.core.logger import set_logger

def set_logging():
  logger = logging.getLogger("custom_logger")
  logger.setLevel(logging.DEBUG)
  logger.addHandler(logging.StreamHandler())
  logger.addHandler(logging.FileHandler("custom.log"))

  set_logger(logger)