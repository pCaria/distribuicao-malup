from fastapi import APIRouter, Depends, HTTPException, Header
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from database import get_db
from models import Usuario
from schemas import UsuarioLogin
from auth import verificar_senha, criar_token_acesso, obter_usuario_autenticado

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")

@router.post("/auth/token")
def login(usuario:UsuarioLogin, db: Session = Depends(get_db)):
    user = db.query(Usuario).filter(Usuario.email == usuario.username).first()
    if not user or not verificar_senha(usuario.password, user.senha_hash):
        raise HTTPException(status_code=401, detail="Usuário ou senha incorretos")

    token = criar_token_acesso(dados={"sub": user.email})

    return {"access_token": token, "token_type": "bearer"}

@router.get("/auth/me")
async def read_headers(authorization: str = Header(None), db: Session = Depends(get_db)):
    token = authorization.split()[1]
    if token is None:
        raise HTTPException(status_code=401, detail="Token ausente")
    payload = obter_usuario_autenticado(token)

    user = db.query(Usuario).filter(Usuario.email == payload["sub"]).first()

    if not user:
        raise HTTPException(status_code=404, detail= "Usuário não Encontrado.")

    return user