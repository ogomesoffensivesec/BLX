from fastapi import FastAPI, Depends, status
from src.schemas.schema import Produto, Usuario
from src.infra.slqalchemy.repository.produto import RepositorioProduto
from src.infra.slqalchemy.repository.usuario import RepositorioUsuario
from sqlalchemy.orm import Session
from src.infra.slqalchemy.config.database import getDB, criar_bd

criar_bd()
app = FastAPI()



@app.post("/produtos", status_code=status.HTTP_201_CREATED, response_model=Produto)
def criar_produto(produto: Produto, db: Session = Depends(getDB)): 
     produto_criado = RepositorioProduto(db).criar(produto)
     return produto_criado
     
@app.get("/produtos")
def listar_produtos(db: Session = Depends(getDB)):
    produtos = RepositorioProduto(db).listar()
    return produtos 
    
    
@app.post("/usuarios", status_code=201, response_model=Usuario)
def criar_usuario(usuario: Usuario, db: Session = Depends(getDB)):
    usuarios = RepositorioUsuario(db).criar(usuario)
    return usuarios

@app.get("/usuarios")
def listar_usuarios(db: Session = Depends(getDB)):
    usuarios = RepositorioUsuario(db).listar()
    return usuarios
