#!/usr/bin/python3
# -*- coding: utf-8 -*-

from dao.config_factory import *
from dao.dbgateway import DBGateway
from dao.utils import *

from Resource import *


def insert(session):
    r = Resource(id=1007, authors="你好", title="我了个去", url="www.baidu.com")
    session.add(r)
    session.commit()


def query(session):
    rs = session.query(Resource).order_by(Resource.title,Resource.authors).all()
    return objs2json(rs)


if __name__ == '__main__':
    basic, pool = get_configs_from_file("./config.json")
    db = DBGateway(basic, pool)
    print(db.execute(query))
