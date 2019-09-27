import datetime


def current():
    return datetime.datetime.utcnow().timestamp()
