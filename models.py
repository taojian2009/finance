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

Model = declarative_base()


class Asset(Model):
    __tablename__ = "asset"
    id = Column(Integer, primary_key=True)
    amount = Column(Float)
    asset_type = Column(String)
    date = Column(Date)


class Outcome(Model):
    __tablename__ = "outcome"
    id = Column(Integer, primary_key=True)
    amount = Column(Float)
    source = Column(String)
    category = Column(String)
    date = Column(Date)


class Income(Model):
    __tablename__ = "income"
    id = Column(Integer, primary_key=True)
    income = Column(Float)
    source = Column(String)
    date = Column(Date)
