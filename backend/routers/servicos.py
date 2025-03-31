from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas
from database import get_db

router = APIRouter(prefix="/servicos", tags=["Servico"])

@router.post("/", response_model=schemas.ServicoOut)
def criar_servico(servico: schemas.ServicoCreate, db: Session = Depends(get_db)):
    novo_servico = models.Servico(**servico.model_dump())
    db.add(novo_servico)
    db.commit()
    db.refresh(novo_servico)
    return novo_servico