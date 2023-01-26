from sqlalchemy.orm import Session
from src.schemas import schema
from src.infra.slqalchemy.models import models

class RepositorioUsuario():
    
    
    def __init__(self, db:Session):
        self.db = db
        
    def criar(self, usuario: schema.Usuario):
        db_usuario = models.Usuario(
            name=usuario.name,
            email=usuario.email,
            tel = usuario.tel
            
        )
        self.db.add(db_usuario)
        self.db.commit()
        self.db.refresh(db_usuario)
        
        return db_usuario
    
    def listar(self):
        usuarios_recovery_db = self.db.query(models.Usuario).all()
        return usuarios_recovery_db
    
    def remover(self):
        pass