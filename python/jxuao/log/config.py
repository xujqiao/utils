#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
import logging.config

filepath = "./logging.conf"
logging.config.fileConfig(filepath)
logger = logging.getLogger("cse")


if __name__ == '__main__':
    logger.info("hello")