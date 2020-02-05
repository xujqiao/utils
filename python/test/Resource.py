#!/usr/bin/python3
# -*- coding: utf-8 -*-
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Resource(Base):
    __tablename__ = "learn_resource"

    id = Column("id", Integer, primary_key=True)
    authors = Column("author", String(20))
    title = Column(String(100))
    url = Column(String(100))

    def __str__(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
