#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
from dao.exceptions import *
from dao.config_factory import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dao.test.Resource import *


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
        if self._basic is None or not isinstance(self._basic, DBBasicConfig):
            raise InitFailException("basic is None or not type of DBBasicConfig")
        if self._pool is None or not isinstance(self._pool, DBPoolConfig):
            raise InitFailException("pool is None or not type of DBBasicConfig")
        self._init_orm()

    def execute(self, callback, *args, **kw):
        session = self._dbsession()
        try:
            result = callback(session, *args, **kw)
        finally:
            session.close()
        return result


__all__ = [DBGateway]


def main():
    engine = create_engine("postgresql://spring:spring_123@127.0.0.1:5432/spring")
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
#     # resource = Resource(id=1006, authors="你好", title="我了个去", url="www.baidu.com")
#     # session.add(resource)
#     # session.commit()
    resources = session.query(Resource).order_by()

    session.close()
