from sqlalchemy import Column, Integer, String, Float
from database import Base

class product(Base):
    __tablename__ = "product"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    description = Column(String(255))
    price = Column(Float)
