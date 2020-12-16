from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'schema': 'jahyadi'}
    user_id=Column(Integer, primary_key=True)
    jahyadi_coin = Column(Integer)
    updated_time = Column(DateTime)

    def __init__(self, user_id, jahyadi_coin, updated_time):
        self.user_id = user_id
        self.jahyadi_coin = jahyadi_coin
        self.updated_time = updated_time