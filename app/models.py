from sqlalchemy import ForeignKey, Integer,Column,String,func
from sqlalchemy.orm import relationship
from .get_db import Base




class Book(Base):
    __tablename__="book"
    id=Column(Integer,primary_key=True,autoincrement=True)
    bh=Column(String(50),nullable=False)
    bname=Column(String(50),nullable=False)
    price=Column(String(50),nullable=False)

    