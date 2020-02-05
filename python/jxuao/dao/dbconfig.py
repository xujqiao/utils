#!/usr/bin/python3
# -*- coding: utf-8 -*-

from dao.utils import *


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

    def __init__(self):
        self.schema = ""
        self.host = ""
        self.port = 0
        self.username = ""
        self.password = ""
        self.dbname = ""
        self.charset = self.DEFAULT_CHARSET
        self.dsn = ""

    def fromfile(self, filepath, charset="utf8"):
        with open(filepath, encoding=charset) as myf:
            config_dict = json.load(myf)
            self.fromdict(config_dict)

    def fromdict(self, config_dict):
        self.schema = dict_safe_get(config_dict, DBBasicConfig.KEY_SCHEMA)
        self.host = dict_safe_get(config_dict, DBBasicConfig.KEY_HOST)
        self.port = dict_safe_get(config_dict, DBBasicConfig.KEY_PORT)
        self.username = dict_safe_get(config_dict, DBBasicConfig.KEY_USERNAME)
        self.password = dict_safe_get(config_dict, DBBasicConfig.KEY_PASSWORD)
        self.dbname = dict_safe_get(config_dict, DBBasicConfig.KEY_DBNAME)
        self.charset = dict_safe_get(config_dict, DBBasicConfig.KEY_CHARSET, default=DBBasicConfig.DEFAULT_CHARSET)
        self.dsn = "%s://%s:%s@%s:%d/%s?client_encoding=%s" % \
                   (self.schema, self.username, self.password, self.host, self.port, self.dbname, self.charset)

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

    def __init__(self):
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
        self.max_overflow = self.DEFAULT_MAX_OVERFLOW
        self.pool_pre_ping = self.DEFAULT_POOL_PRE_PING
        self.pool_size = self.DEFAULT_POOL_SIZE
        self.pool_recycle = self.DEFAULT_POOL_RECYCLE
        self.pool_reset_on_return = self.DEFAULT_POOL_RESET_ON_RETURN
        self.pool_timeout = self.DEFAULT_POOL_TIMEOUT
        self.pool_use_lifo = self.DEFAULT_POOL_USE_LIFO

    def fromfile(self, filepath, charset="utf8"):
        with open(filepath, encoding=charset) as myf:
            config_dict = json.load(myf)
            self.fromdict(config_dict)

    def fromdict(self, config_dict):
        self.max_overflow = \
            dict_safe_get(config_dict, self.KEY_MAX_OVERFLOW, default=DBPoolConfig.DEFAULT_MAX_OVERFLOW)
        self.pool_pre_ping = \
            dict_safe_get(config_dict, self.KEY_POOL_PRE_PING, default=DBPoolConfig.DEFAULT_POOL_PRE_PING)
        self.pool_size = \
            dict_safe_get(config_dict, self.KEY_POOL_SIZE, default=DBPoolConfig.DEFAULT_POOL_SIZE)
        self.pool_recycle = \
            dict_safe_get(config_dict, self.KEY_POOL_RECYCLE, default=DBPoolConfig.DEFAULT_POOL_RECYCLE)
        self.pool_reset_on_return = \
            dict_safe_get(config_dict, self.KEY_POOL_RESET_ON_RETURN, default=DBPoolConfig.DEFAULT_POOL_RESET_ON_RETURN)
        self.pool_timeout = \
            dict_safe_get(config_dict, self.KEY_POOL_TIMEOUT, default=DBPoolConfig.DEFAULT_POOL_TIMEOUT)
        self.pool_use_lifo = \
            dict_safe_get(config_dict, self.KEY_POOL_USE_LIFO, default=DBPoolConfig.DEFAULT_POOL_USE_LIFO)

    def __str__(self):
        return "{}: {}".format(
            self.__class__.__name__,
            "&".join([str(key) + "=" + str(value) for key, value in self.__dict__.items()])
        )
