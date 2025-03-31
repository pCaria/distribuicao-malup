from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas
from database import get_db

router = APIRouter(prefix="/clientes/orcamentos", tags=["Orcamentos"])

@router.post("/", response_model=schemas.OrcamentoOut)
def criar_orcamento(orcamento: schemas.OrcamentoCreate, db: Session = Depends(get_db)):
    novo_orcamento = models.Orcamento(**orcamento.model_dump())
    db.add(novo_orcamento)
    db.commit()
    db.refresh(novo_orcamento)
    return novo_orcamento