# from fastapi import APIRouter, Depends, HTTPException, status
# from sqlalchemy.orm import Session
# from database import get_db
# from routers.auth import obter_usuario_autenticado  # Importa a função que valida o token do usuário

# router = APIRouter()

# @router.get("/dashboard")
# def get_dashboard_data(current_user: dict = Depends(obter_usuario_autenticado), db: Session = Depends(get_db)):
#     """
#     Retorna os dados necessários para o dashboard do usuário autenticado.
#     """
#     if not current_user:
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Usuário não autenticado")

#     # Simulação de dados que podem ser retornados
#     data = {
#         "total_clientes": 150,
#         "total_orcamentos": 75,
#         "total_vendas": 50,
#         "mensagem": f"Bem-vindo, {current_user['nome']}!",
#     }

#     return data
