from sqlalchemy import Column, String, Float, Integer, ForeignKey, Enum
from db import base
from enum import Enum as enumerador

class Product(base):
    __tablename__ = "products"

    class states(enumerador):
        ACTIVE = 'A'
        INACTIVE = 'I'
    
    id = Column(String, primary_key=True)
    description = Column(String)
    price =  Column(Float)
    quantity = Column(Integer)
    statusP = Column(Enum(states))
