from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime

# Os Schemas definem a estrutura dos dados que serão enviados e recebidos pela API.

# Schemas Permissao:

class PermissaoBase(BaseModel):
    nome: str

class PermissaoCreate(PermissaoBase):
    pass

class PermissaoOut(PermissaoBase):
    id: int

    class Config:
        from_attributes = True

# Schemas Usuário

class UsuarioBase(BaseModel):
    nome: str
    email: EmailStr

class UsuarioCreate(UsuarioBase):
    senha: str

class UsuarioOut(UsuarioBase):
    id: int
    criado_em: datetime
    permissao: Optional[PermissaoOut] = None

    class Config:
        from_attributes = True

# Schemas Log_Acesso

class LogAcessoBase(BaseModel):
    ip: str
    acao: str

class LogAcessoOut(LogAcessoBase):
    id: int
    data_hora: datetime

    class Config:
        from_attributes = True

# Schemas Cliente

class ClienteBase(BaseModel):
    id: Optional[int] = None
    nome: Optional[str] = None

class ClienteCreate(ClienteBase):
    id: int
    nome: str
    email: EmailStr
    telefone: str
    cnpj: str
    tipo: str


class ClienteOut(ClienteBase):
    id: int
    nome: str
    email: EmailStr
    telefone: str
    cnpj: str
    tipo: str

    class Config:
        from_attributes = True

# Schemas Orcamento

class OrcamentoBase(BaseModel):
    cliente_id: int


class OrcamentoCreate(OrcamentoBase):
    pass


class OrcamentoOut(OrcamentoBase):
    id: int
    data_orcamento: datetime
    status: str
    data_fechamento: Optional[datetime]  # Para armazenar o histórico de orçamentos

    class Config:
        from_attributes = True

# Schemas Servico

class ServicoBase(BaseModel):
    nome: str
    descricao: Optional[str] = None

class ServicoCreate(ServicoBase):
    pass


class ServicoOut(ServicoBase):
    id: int

    class Config:
        from_attributes = True

#Schemas Produto

class ProdutoBase(BaseModel):
    nome: str


class ProdutoCreate(ProdutoBase):
    pass


class ProdutoOut(ProdutoBase):
    id: int

    class Config:
        from_attributes = True

# Schemas Taxa

class TaxaBase(BaseModel):
    tipo_cliente: str


class TaxaOut(TaxaBase):
    id: int
    tipo_taxa: str
    valor: float

    class Config:
        from_attributes = True