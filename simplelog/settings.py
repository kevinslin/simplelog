import logging
from logging import NOTSET, INFO, DEBUG, WARNING, ERROR, CRITICAL

SIMPLELOG = "simplelog"
SIMPLE_FORMAT = "[%(levelname)s]: %(asctime)s: %(message)s"
DETAIL_FORMAT = "[%(levelname)s], %(filename)s:%(funcName)s(), %(asctime)s: %(message)s"
FMT_DATETIME = "%m/%d/%Y-%H:%M.%S" # hour:minute.seconds
SIMPLE_FORMATTER = logging.Formatter(fmt = SIMPLE_FORMAT, datefmt = FMT_DATETIME)
