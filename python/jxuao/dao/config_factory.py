#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os

from dao.exceptions import FileNotExistException
from dao.dbconfig import DBBasicConfig,DBPoolConfig


def get_basic_config_from_file(filepath, charset="utf8"):
    if not os.path.isfile(filepath):
        raise FileNotExistException("file [{}] does not exist".format(filepath))
    basic_config = DBBasicConfig()
    basic_config.fromfile(filepath, charset)
    return basic_config


def get_pool_config_from_file(filepath, charset="utf8"):
    if not os.path.isfile(filepath):
        raise FileNotExistException("file [{}] does not exist".format(filepath))
    pool_config = DBPoolConfig()
    pool_config.fromfile(filepath, charset)
    return pool_config


def get_configs_from_file(filepath, charset="utf8"):
    if not os.path.isfile(filepath):
        raise FileNotExistException("file [{}] does not exist".format(filepath))
    basic_config = DBBasicConfig()
    basic_config.fromfile(filepath, charset)
    pool_config = DBPoolConfig()
    pool_config.fromfile(filepath, charset)
    return basic_config, pool_config


if __name__ == '__main__':
    filepath = "test/config.json"
    config = get_basic_config_from_file(filepath)
    print(config)


