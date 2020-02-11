#!/usr/bin/python3
# -*- coding: utf-8 -*-
from sqlalchemy import Column, String, Integer, Boolean, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base

BaseClass = declarative_base()


class Base(BaseClass):
    def __str__(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Resource(Base):
    __tablename__ = "learn_resource"

    id = Column("id", Integer, primary_key=True)
    authors = Column("author", String(20))
    title = Column(String(100))
    url = Column(String(100))


class CaptchaRecord(Base):
    __tablename__ = "t_captcha_record"

    id = Column("f_id", Integer, primary_key=True, autoincrement=True)
    website = Column("f_website", String(128))
    is_success = Column("f_is_success", Boolean)
    result = Column("f_result", String(16))
    absolute_path = Column("f_absolute_path", String(512))
    upload_ip = Column("f_upload_ip", String(32))
    create_time = Column("f_create_time", TIMESTAMP, index=True)
    update_time = Column("f_update_time", TIMESTAMP)

