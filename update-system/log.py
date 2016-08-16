import logging
from datetime import datetime

def getlogger():

    logger = logging.getLogger()

    now = datetime.now()
    filename="/var/log/update-system.{}-{}-{}.log".format(now.year, now.month,
            now.day)
    # set formatter
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s [%(levelname)s] - [%(module)s %(funcName)s() line:%(lineno)d ]: %(message)s',"%Y-%m-%d %H:%M:%S") 

    # set fh 
    fh = logging.FileHandler(filename, encoding="UTF-8")
    fh.setFormatter(formatter)
    fh.setLevel(logging.DEBUG)
    # set ch
    ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    ch.setLevel(logging.INFO)
    # set logger with ch and fh
    logger.addHandler(ch)
    logger.addHandler(fh)

    return logger

#def svn_log():
#    logger_filename="/var/log/svn.log"
#
#    logger = logging.getLogger()
#    logger.setLevel(logging.DEBUG)
#   # formatter = logging.Formatter('%(asctime)s [%(levelname)s] - %(filename)
#    formatter = logging.Formatter('%(asctime)s [%(levelname)s] - [%(module)s %(funcName)s() line:%(lineno)d ]: %(message)s',"%Y-%m-%d %H:%M:%S")
#    fh = logging.FileHandler(logger_filename,encoding = "UTF-8")
#    fh.setLevel(logging.DEBUG)
#    fh.setFormatter(formatter)
#
#    ch = logging.StreamHandler()
#    ch.setLevel(logging.WARNING)
#    ch.setFormatter(formatter)
#
#    logger.addHandler(fh)
#    logger.addHandler(ch)
#    return logger

logger = getlogger()

