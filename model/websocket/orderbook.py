from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, DateTime, Float, Integer, String
import pymysql

import settings

pymysql.install_as_MySQLdb()

user = settings.username
password = settings.password
host = settings.host
db_name = settings.db_name

# engineの設定
engine = create_engine(f'mysql://{user}:{password}@{host}/{db_name}')

SessionClass = sessionmaker(engine)  # セッションを作るクラスを作成
session = SessionClass()

# テーブルを作成する
Base = declarative_base()


class Transaction(object):
    __tablename__ = 'orderbook'
    timestamp = Column(Integer)
    txid = Column(Integer)
    trade_pair = Column(String(16))
    rate = Column(Float)
    amount = Column(Float)
    buy_or_sell = Column(String)
    taker_txid = Column(Integer)
    maker_txid = Column(Integer)


Base.metadata.create_all(bind=engine)
