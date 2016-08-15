import logging

logger = logging.getLogger("sub")

def foo():
    logger.warn(__name__)
    logger.debug("this is debug")
    logger.info("this is info")
    logger.warn("this is warn")
    logger.error("this is error")
    logger.fatal("this is fatal")

