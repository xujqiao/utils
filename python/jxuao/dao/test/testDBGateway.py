#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time

from dao.dbgateway import *
from dao.utils import *
from dao.dbconfig import *
from dao.test.Resource import *


def insert(session, id) -> None:
    r = Resource(id=id, authors="你好", title="我了个去", url="www.baidu.com")
    session.add(r)
    session.commit()


def query(session, id) -> str:
    rs = session.query(Resource).filter_by(id=id).one()
    return obj2json(rs)


def query2(session) -> list:
    rs = session.query(Resource) \
        .filter(Resource.id > 100) \
        .filter(Resource.title.contains("123")) \
        .filter(Resource.authors.isnot("1234123")) \
        .all()
    return [r for r in rs]


if __name__ == '__main__':
    basic, pool = get_configs_from_file("config.json")
    print(pool.pool_size)
    db = DBGateway(basic, pool)

    start_id = 1007
    end_id = 11007
    start_time = time.time()
    try:
        for id in range(start_id, end_id):
            db.execute(query, id)
    finally:
        end_time = time.time()
    print(end_time, start_time)
    print((end_id - start_id) / (end_time - start_time))


