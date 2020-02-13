#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys
from dao.utils import *
from dao.exceptions import FileNotExistException

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class DBBasicConfig:
    """
    DB配置类
    """
    KEY_SCHEMA = "schema"
    KEY_HOST = "host"
    KEY_PORT = "port"
    KEY_USERNAME = "username"
    KEY_PASSWORD = "password"
    KEY_DBNAME = "db_name"
    KEY_CHARSET = "charset"
    DEFAULT_CHARSET = "utf8"

    def __new__(cls, schema, host, port, username, password, dbname, charset):
        self = object.__new__(cls)
        self.schema = schema
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.dbname = dbname
        self.charset = charset
        self.dsn = "%s://%s:%s@%s:%d/%s?client_encoding=%s" % \
                   (self.schema, self.username, self.password, self.host, self.port, self.dbname, self.charset)
        return self

    @classmethod
    def fromfile(cls, filepath, charset="utf8"):
        with open(filepath, encoding=charset) as myf:
            d = json.load(myf)
            return cls.fromdict(d)

    @classmethod
    def fromdict(cls, d):
        schema = dict_safe_get(d, DBBasicConfig.KEY_SCHEMA)
        host = dict_safe_get(d, DBBasicConfig.KEY_HOST)
        port = dict_safe_get(d, DBBasicConfig.KEY_PORT)
        username = dict_safe_get(d, DBBasicConfig.KEY_USERNAME)
        password = dict_safe_get(d, DBBasicConfig.KEY_PASSWORD)
        dbname = dict_safe_get(d, DBBasicConfig.KEY_DBNAME)
        charset = dict_safe_get(d, DBBasicConfig.KEY_CHARSET, default=DBBasicConfig.DEFAULT_CHARSET)
        return cls(schema, host, port, username, password, dbname, charset)

    def __str__(self):
        return "{}: {}".format(
            self.__class__.__name__,
            "&".join([str(key) + "=" + str(value) for key, value in self.__dict__.items()])
        )


class DBPoolConfig:
    """
    DB连接池配置类

    """
    KEY_MAX_OVERFLOW = "max_overflow"
    KEY_POOL_PRE_PING = "pool_pre_ping"
    KEY_POOL_SIZE = "pool_size"
    KEY_POOL_RECYCLE = "pool_recycle"
    KEY_POOL_RESET_ON_RETURN = "reset_on_return"
    KEY_POOL_TIMEOUT = "pool_timeout"
    KEY_POOL_USE_LIFO = "pool_use_lifo"
    DEFAULT_MAX_OVERFLOW = 10
    DEFAULT_POOL_PRE_PING = False
    DEFAULT_POOL_SIZE = 5
    DEFAULT_POOL_RECYCLE = -1
    DEFAULT_POOL_RESET_ON_RETURN = "rollback"
    DEFAULT_POOL_TIMEOUT = 30
    DEFAULT_POOL_USE_LIFO = False

    def __new__(cls, max_overflow, pre_ping, size, recycle, reset_on_return, timeout, use_lifo):
        """
        :param max_overflow=10: the number of connections to allow in
            connection pool "overflow", that is connections that can be
            opened above and beyond the pool_size setting, which defaults
            to five. this is only used with :class:`~sqlalchemy.pool.QueuePool`.

        :param pool_pre_ping: boolean, if True will enable the connection pool
            "pre-ping" feature that tests connections for liveness upon
            each checkout.

            .. versionadded:: 1.2

            .. seealso::

                :ref:`pool_disconnects_pessimistic`

        :param pool_size=5: the number of connections to keep open
            inside the connection pool. This used with
            :class:`~sqlalchemy.pool.QueuePool` as
            well as :class:`~sqlalchemy.pool.SingletonThreadPool`.  With
            :class:`~sqlalchemy.pool.QueuePool`, a ``pool_size`` setting
            of 0 indicates no limit; to disable pooling, set ``poolclass`` to
            :class:`~sqlalchemy.pool.NullPool` instead.

        :param pool_recycle=-1: this setting causes the pool to recycle
            connections after the given number of seconds has passed. It
            defaults to -1, or no timeout. For example, setting to 3600
            means connections will be recycled after one hour. Note that
            MySQL in particular will disconnect automatically if no
            activity is detected on a connection for eight hours (although
            this is configurable with the MySQLDB connection itself and the
            server configuration as well).

            .. seealso::

                :ref:`pool_setting_recycle`

        :param pool_reset_on_return='rollback': set the
            :paramref:`.Pool.reset_on_return` parameter of the underlying
            :class:`.Pool` object, which can be set to the values
            ``"rollback"``, ``"commit"``, or ``None``.

            .. seealso::

                :paramref:`.Pool.reset_on_return`

        :param pool_timeout=30: number of seconds to wait before giving
            up on getting a connection from the pool. This is only used
            with :class:`~sqlalchemy.pool.QueuePool`.

        :param pool_use_lifo=False: use LIFO (last-in-first-out) when retrieving
            connections from :class:`.QueuePool` instead of FIFO
            (first-in-first-out). Using LIFO, a server-side timeout scheme can
            reduce the number of connections used during non- peak   periods of
            use.   When planning for server-side timeouts, ensure that a recycle or
            pre-ping strategy is in use to gracefully   handle stale connections.

              .. versionadded:: 1.3

              .. seealso::

                :ref:`pool_use_lifo`

                :ref:`pool_disconnects`
        """
        self = object.__new__(cls)
        self.max_overflow = max_overflow
        self.pool_pre_ping = pre_ping
        self.pool_size = size
        self.pool_recycle = recycle
        self.pool_reset_on_return = reset_on_return
        self.pool_timeout = timeout
        self.pool_use_lifo = use_lifo
        return self

    @classmethod
    def fromfile(cls, path, charset="utf8"):
        with open(path, encoding=charset) as myf:
            d = json.load(myf)
            return cls.fromdict(d)

    @classmethod
    def fromdict(cls, d):
        max_overflow = \
            dict_safe_get(d, DBPoolConfig.KEY_MAX_OVERFLOW, default=DBPoolConfig.DEFAULT_MAX_OVERFLOW)
        pre_ping = \
            dict_safe_get(d, DBPoolConfig.KEY_POOL_PRE_PING, default=DBPoolConfig.DEFAULT_POOL_PRE_PING)
        size = \
            dict_safe_get(d, DBPoolConfig.KEY_POOL_SIZE, default=DBPoolConfig.DEFAULT_POOL_SIZE)
        recycle = \
            dict_safe_get(d, DBPoolConfig.KEY_POOL_RECYCLE, default=DBPoolConfig.DEFAULT_POOL_RECYCLE)
        reset_on_return = \
            dict_safe_get(d, DBPoolConfig.KEY_POOL_RESET_ON_RETURN, default=DBPoolConfig.DEFAULT_POOL_RESET_ON_RETURN)
        timeout = \
            dict_safe_get(d, DBPoolConfig.KEY_POOL_TIMEOUT, default=DBPoolConfig.DEFAULT_POOL_TIMEOUT)
        use_lifo = \
            dict_safe_get(d, DBPoolConfig.KEY_POOL_USE_LIFO, default=DBPoolConfig.DEFAULT_POOL_USE_LIFO)

        return cls(max_overflow, pre_ping, size, recycle, reset_on_return, timeout, use_lifo)

    def __str__(self):
        return "{}: {}".format(
            self.__class__.__name__,
            "&".join([str(key) + "=" + str(value) for key, value in self.__dict__.items()])
        )


def get_configs_from_file(filepath, charset="utf8"):
    if not os.path.isfile(filepath):
        raise FileNotExistException("file [{}] does not exist".format(filepath))
    basic_config = DBBasicConfig.fromfile(filepath, charset)
    pool_config = DBPoolConfig.fromfile(filepath, charset)
    return basic_config, pool_config


__all__ = ["get_configs_from_file", "DBBasicConfig", "DBPoolConfig"]


if __name__ == '__main__':
    filepath = "../app/config.json"
    config = DBPoolConfig.fromfile(filepath)
    print(config)
    print(DBBasicConfig.__name__)
    print(DBBasicConfig.__class__)
