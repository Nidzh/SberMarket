from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship

from db.database import Base


class Category(Base):
    __tablename__ = 'categorys'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    shop = Column(String)
    name = Column(String)

