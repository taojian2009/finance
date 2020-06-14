from sqlalchemy import (
    create_engine,
    inspect,
    Column,
    String,
    Date,
    Float,
    Integer)
from datetime import datetime

import pandas as pd
from sqlalchemy.orm import sessionmaker

from sqlalchemy.ext.declarative import declarative_base

import pymysql

pymysql.install_as_MySQLdb()

db_url = "mysql://root:mysql@localhost:3306/finance?charset=utf8"
engine = create_engine(db_url)
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()


class FinanceManager(object):
    def __init__(self):
        pass

    @staticmethod
    def commit(objs):
        for obj in objs:
            session.add(obj)
        session.commit()
