#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json
import calendar
import datetime
import time


class Fmt:
    YEAR = "%Y"  # 1998 w/t centry
    year = "%y"  # 98 w/o centry
    MONTH = "%m"  # 1-12
    MONTH_FULL = "%B"  # August
    month = "%b"  # Aug
    DAY = "%d"  # 1-31
    HOUR = "%H"  # 24 hours
    hour = "%I"  # 12 hours
    AMPM = "%p"  # AM or PM
    MINUTE = "%M"  # 1-59
    SECOND = "%S"  # 1-59
    MICROSECOND = "%f"  # ms
    WEEK = "%A"  # Sunday
    week = "%a"  # Sun
    week_seq = "%w"  # 0 for Sunday, 6 for Saturday


DEFAULT_DATETIME_FORMAT = "{}-{}-{} {}:{}:{}".format(
    Fmt.YEAR, Fmt.MONTH, Fmt.DAY, Fmt.HOUR, Fmt.MINUTE, Fmt.SECOND
)


def now_ts() -> float:
    """
    :return: seconds
    """
    return time.time()


def now_dt() -> datetime:
    return datetime.datetime.now()


def now_string(fmt: str = DEFAULT_DATETIME_FORMAT) -> str:
    assert isinstance(fmt, str)
    return now_dt().strftime(fmt)


def ts2string(ts: float, fmt: str = DEFAULT_DATETIME_FORMAT) -> str:
    assert isinstance(fmt, str)
    dt = datetime.datetime.fromtimestamp(ts)
    return dt2string(dt, fmt)


def string2ts(dt_string: str, fmt: str = DEFAULT_DATETIME_FORMAT) -> float:
    assert isinstance(dt_string, str)
    assert isinstance(fmt, str)
    return datetime.datetime.timestamp(string2dt(dt_string, fmt))


def dt2string(dt: datetime.datetime, fmt: str = DEFAULT_DATETIME_FORMAT) -> str:
    assert isinstance(dt, datetime.datetime)
    assert isinstance(fmt, str)
    return dt.strftime(fmt)


def string2dt(dt_string: str, fmt: str = DEFAULT_DATETIME_FORMAT) -> datetime.datetime:
    assert isinstance(dt_string, str)
    assert isinstance(fmt, str)
    return datetime.datetime.strptime(dt_string, fmt)


def datetimedelta(base_dt: datetime.datetime = now_dt(), **kw) -> datetime.datetime:
    """
    :param base_dt:
    :param kw: only valid fields: "seconds", "minutes", "hours", "days", "months", "years"
    :return:
    """
    assert isinstance(base_dt, datetime.datetime)
    kwargs = {field: kw[field] for field in ["seconds", "minutes", "hours", "days", "months", "years"] if field in kw}
    return base_dt + datetime.timedelta(**kwargs)


if __name__ == '__main__':
    print(calendar.February)
    for day in calendar.day_name:
        print(day)

    for month in calendar.month_name:
        print(month)

    print(calendar.firstweekday())
    print(calendar.weekday(2020, 3, 1))
    c = calendar.Calendar()
    print(json.dumps(c.yeardayscalendar(2020)))
    print(calendar.timegm([2020, 1, 5, 13, 14, 50]))
    print(now_string())
    delta = datetime.timedelta(hours=-3)
    now = now_dt()
    print(dt2string(now + delta))
    print(datetimedelta(hours=-3).strftime(DEFAULT_DATETIME_FORMAT))
