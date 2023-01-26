from sqlalchemy.orm import Session
from src.schemas import schema
from src.infra.slqalchemy.models import models
class RepositorioProduto():
    
    def __init__(self, db: Session):
        self.db = db
        
    
    def criar(self, produto: schema.Produto):
        db_produto = models.Produto(name=produto.name,
                                    price=produto.price,
                                    description=produto.description,
                                    disponivel=produto.disponivel)
        self.db.add(db_produto)
        self.db.commit()
        self.db.refresh(db_produto)
        return db_produto
    
    def listar(self):
        produtos_recovery_db  = self.db.query(models.Produto).all()
        return produtos_recovery_db
    
    def remover(self):
        pass