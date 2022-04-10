import os
import logging
from utils.singelton import Singleton


class OneLineExceptionFormatter(logging.Formatter):
    def formatException(self, exc_info):
        result = super(OneLineExceptionFormatter, self).formatException(exc_info)
        return repr(result) # or format into one line however you want to

    def format(self, record):
        s = super(OneLineExceptionFormatter, self).format(record)
        return repr(s)


class Logger(metaclass=Singleton):
    log_file = os.environ.get("LOG_FILE", "/usr/local/var/logfile.log")
    log_level = os.environ.get("LOG_LEVEL", logging.DEBUG)

    def __init__(self):
        pass

    #
    # https://stackoverflow.com/questions/641420/how-should-i-log-while-using-multiprocessing-in-python
    def get_logger(self):
        import multiprocessing, logging
        logger = multiprocessing.get_logger()
        logger.setLevel(self.log_level)
        formatter = OneLineExceptionFormatter(
            "%(asctime)s — %(processName)s - %(thread)x — %(levelname)s — %(pathname)s - %(funcName)s:%(lineno)d — %(message)s")

        # Add rotating file handler
        # file_handler = RotatingFileHandler(self.log_file, maxBytes=10485760, backupCount=5)
        # file_handler.setFormatter(formatter)
        # logger.addHandler(file_handler)

        # Also add console handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        if not len(logger.handlers):
            # logger.addHandler(file_handler)
            logger.addHandler(console_handler)

        return logger
