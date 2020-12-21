from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class AllowedSay(Base):
    __tablename__ = 'allowed_say'
    __table_args__ = {'schema': 'jahyadi'}
    user_id=Column(Integer, primary_key=True)

    def __init__(self, user_id):
        self.user_id = user_id