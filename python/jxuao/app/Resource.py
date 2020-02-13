#!/usr/bin/python3
# -*- coding: utf-8 -*-

from dao.base import *


class Resource(Base):
    __tablename__ = "learn_resource"

    id = Column("id", Integer, primary_key=True)
    authors = Column("author", String(20))
    title = Column(String(100))
    url = Column(String(100))

