#!/usr/bin/env python

import sub
import logging

logger = logging.getLogger("spam")
# create handler
fh = logging.FileHandler("test.log")
fh.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.WARNING)

# create formatter
ft1 = logging.Formatter('%(asctime)s - %(name)s -  \
        %(levelname)s - %(message)s')
# handler set format
fh.setFormatter(ft1)
ch.setFormatter(ft1)

logger.addHandler(ch)
logger.addHandler(fh)

logger.debug("this is debug")
logger.info("this is info")
logger.warn("this is warn")
logger.error("this is error")
logger.fatal("this is fatal")

sub.foo()
