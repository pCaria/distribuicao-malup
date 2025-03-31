import auth
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import clientes, orcamentos, servicos, dashboard, authRoute

app = FastAPI(title= "Sistema de Administração de Orçamentos")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite requisições de qualquer origem
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(authRoute.router)
# app.include_router(dashboard.router)
app.include_router(clientes.router)
app.include_router(orcamentos.router)
app.include_router(servicos.router)