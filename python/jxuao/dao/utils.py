#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys
import json
from functools import wraps
from dao.exceptions import NotTheSameException, NotExistException

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def dict_safe_get(d, k, default=None):
    """
    先检查是否存在，再获取
    :param d: 传入的dict
    :param k: 获取的key
    :param default: 如果key不存在，返回的默认值
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
            if isinstance(result, sames) and result == sames:
                pass
            else:
                raise NotTheSameException(result, "is not same as", sames)
        return wrapper_func
    return decorator


def dict2obj(d, clazz):
    obj = clazz()
    for k, v in d.items():
        obj.__setattr__(k, v)
    return obj


def json2obj(string, clazz):
    return dict2obj(json.loads(string), clazz)


def json2objs(string, clazz):
    objs = list()
    for d in json.loads(string):
        objs.append(dict2obj(d, clazz))
    return objs


def obj2dict(obj):
    fields = {}
    for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
        fields[field] = obj.__getattribute__(field)
    return fields


def obj2json(obj):
    return json.dumps(obj2dict(obj))


def objs2json(objs):
    results = []
    for obj in objs:
        results.append(obj2dict(obj))
    return json.dumps(results)

