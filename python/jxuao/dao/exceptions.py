#/usr/bin/python3
# -*- coding: utf-8 -*-


class NotTheSameException(Exception):
    pass


class FileNotExistException(Exception):
    pass


class NotExistException(Exception):
    pass


class MissingConfigException(Exception):
    pass


class InitFailException(Exception):
    pass
