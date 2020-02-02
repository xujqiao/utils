#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json
from utils import *


class DBBasicConfig:
    """
    DB配置类
    """
    KEY_HOST = "host"
    KEY_PORT = "port"
    KEY_USERNAME = "username"
    KEY_PASSWORD = "password"
    KEY_DBNAME = "db_name"
    KEY_CHARSET = "charset"
    DEFAULT_CHARSET = "utf8"

    def __init__(self):
        self._host = ""
        self._port = 0
        self._username = ""
        self._password = ""
        self._dbname = ""
        self._charset = self.DEFAULT_CHARSET

    def fromfile(self, filepath, charset="utf8"):
        with open(filepath, encoding=charset) as myf:
            config_dict = json.load(myf)
            self.fromdict(config_dict)

    def fromdict(self, config_dict):
        self._host = dict_safe_get(config_dict, DBBasicConfig.KEY_HOST)
        self._port = dict_safe_get(config_dict, DBBasicConfig.KEY_PORT)
        self._username = dict_safe_get(config_dict, DBBasicConfig.KEY_USERNAME)
        self._password = dict_safe_get(config_dict, DBBasicConfig.KEY_PASSWORD)
        self._dbname = dict_safe_get(config_dict, DBBasicConfig.KEY_DBNAME)
        self._charset = dict_safe_get(config_dict, DBBasicConfig.KEY_CHARSET, default=DBBasicConfig.DEFAULT_CHARSET)

    def __str__(self):
        return "&".join([str(key) + "=" + str(value) for key, value in self.__dict__.items()])


if __name__ == '__main__':
    filepath = "./config.json"
    config = DBBasicConfig()
    config.fromfile(filepath)
    print(config)
