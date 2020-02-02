#!/usr/bin/python3
# -*- coding: utf-8 -*-

from functools import wraps
from exceptions import NotTheSameException, NotExistException


def dict_safe_get(d, k, default=None):
    """
    先检查是否存在，再获取
    :param d: 传入的dict
    :param k: 获取的key
    :param default: 如果key不能存在，返回的默认值
    :return: 如果没有默认值，即为None，则抛出异常
    """
    if k in d:
        return d[k]
    elif default is not None:
        return default
    else:
        raise NotExistException("dict does not contain key [{}]".format(k))


def is_same_decorator(sames=None):
    """
    检查value和should是否类型和值均一致
    不一致则抛出异常
    :param sames: 待检查的值
    :return: void
    :raise: raise NotTheSameException
    """
    def decorator(func):
        @wraps(func)
        def wrapper_func(*args):
            result = func(*args)
            if type(result) == type(sames) and result == sames:
                pass
            else:
                raise NotTheSameException(result, "is not same as", sames)
        return wrapper_func
    return decorator

