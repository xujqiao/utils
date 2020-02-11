#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
import os
import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from dao.exceptions import *
from dao.dbconfig import DBPoolConfig, DBBasicConfig
from dao.test.Resource import *

# 相对路径的添加，保证了此处模块导入路径不变
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class DBGateway:
    def __init__(self, basic, pool):
        self._basic = basic
        self._pool = pool
        self._dbsession = None
        self._init()

    def _init_orm(self):
        engine = create_engine(
            self._basic.dsn,
            encoding=self._basic.charset,
            max_overflow=self._pool.max_overflow,
            pool_pre_ping=self._pool.pool_pre_ping,
            pool_size=self._pool.pool_size,
            pool_recycle=self._pool.pool_recycle,
            pool_reset_on_return=self._pool.pool_reset_on_return,
            pool_timeout=self._pool.pool_timeout,
            pool_use_lifo=self._pool.pool_use_lifo
        )
        self._dbsession = sessionmaker(bind=engine)
        if self._dbsession is None:
            raise InitFailException("dbsession is None")

    def _init(self):
        if self._basic is None or \
                (not isinstance(self._basic, DBBasicConfig) and DBBasicConfig.__name__ not in str(type(self._basic))):
            """
            由于在导入路径里添加了相对路径，而basic又从外部传入
            此处DBBasicConfig的type是dao.dbconfig.DBBasicConfig
            而传入的basic的type可能是xxxx.dao.dbconfig.DBBasicConfig
            因为调用的代码不一定在dao目录下，可能在dao的上层目录中，因此就会包含上层目录，
            导致isinstance返回False
            """
            raise InitFailException("basic is None or not type of DBBasicConfig")
        if self._pool is None or \
                (not isinstance(self._pool, DBPoolConfig) and DBPoolConfig.__name__ not in str(type(self._pool))):
            """
            同上
            """
            raise InitFailException("pool is None or not type of DBBasicConfig")
        self._init_orm()

    def execute(self, callback, *args, **kw):
        session = self._dbsession()
        try:
            result = callback(session, *args, **kw)
        finally:
            session.close()
        return result


__all__ = ["DBGateway"]


def main():
    engine = create_engine("postgresql://spring:spring_123@127.0.0.1:5432/spring")
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    #     # resource = Resource(id=1006, authors="你好", title="我了个去", url="www.baidu.com")
    #     # session.add(resource)
    #     # session.commit()
    #     resources = session.query(Resource).order_by()
    sql = """
    select
        count(1) as total,
        count(case when title = '我了个去' then 1 else null end) as valid,
        count(case when title != '我了个去' then 1 else null end) as invalid
    from learn_resource
    """
    result = session.execute(sql)
    for r in result:
        print(r)

    session.close()


if __name__ == '__main__':
    main()
