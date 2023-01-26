from sqlalchemy import Integer, String, Float, Column, Boolean
from src.infra.slqalchemy.config.database import Base

class Produto(Base):
    
    __tablename__ = "produtos"
    
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(Float)
    description = Column(String)
    disponivel = Column(Boolean)
    
    
class Usuario(Base):
    __tablename__ = "usuarios"
    
    id = Column(Integer, primary_key=True, index=True)
    name =  Column(String)
    email =  Column(String)
    tel =  Column(Integer)
   