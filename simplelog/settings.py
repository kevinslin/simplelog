import logging

SIMPLELOG = "simplelog"
SIMPLE_FORMAT = "[%(levelname)s]: %(asctime)s: %(message)s"
SIMPLE_FORMATTER = logging.Formatter(fmt = SIMPLE_FORMAT, datefmt = "%H:%m.%S")
