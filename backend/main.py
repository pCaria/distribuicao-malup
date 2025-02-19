from fastapi import FastAPI
from backend.routers import clientes, orcamentos, servicos

app = FastAPI(title= "Sistema de Administração de Orçamentos")

app.include_router(clientes.router)
app.include_router(orcamentos.router)
app.include_router(servicos.router)