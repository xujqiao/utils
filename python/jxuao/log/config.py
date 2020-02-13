#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys
import logging
import logging.config


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

pwd = os.path.dirname(os.path.abspath(__file__))
filepath = pwd + "/logging.conf"
logging.config.fileConfig(filepath)
logger = logging.getLogger("cse")

__all__ = ["logger"]

if __name__ == '__main__':
    logger.info("hello")