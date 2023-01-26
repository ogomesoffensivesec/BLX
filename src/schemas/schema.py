from pydantic import BaseModel
from typing import Optional, List
from fastapi import FastAPI, File, UploadFile




class Usuario(BaseModel):
    id: Optional[str] = None
    name: str
    email: str
    tel: int 


class Produto(BaseModel):
    id: Optional[str] = None
    name: str    
    price: float
    description: str
    disponivel: bool = False
    #file: UploadFile = File(...)
    
    class Config:
        orm_mode = True
    
class Pedido(BaseModel):
    id: Optional[str] = None
    usuario: Usuario
    produto: Produto
    quantidade: int
    local: str
    obs: Optional[str] = 'Sem Observações.'
    entrega: bool = False
    