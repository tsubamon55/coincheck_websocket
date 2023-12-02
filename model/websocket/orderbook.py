from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Float, Integer, String
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


class Transaction(Base):
    __tablename__ = 'orderbook'
    timestamp = Column(Integer)
    txid = Column(String(16), primary_key=True)
    trade_pair = Column(String(16))
    rate = Column(Float)
    amount = Column(Float)
    buy_or_sell = Column(String(8))
    taker_txid = Column(String(16))
    maker_txid = Column(String(16))


def init():
    Base.metadata.create_all(bind=engine)
