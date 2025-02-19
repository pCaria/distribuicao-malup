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
    senha_hash: str
    permissao: Optional[int] = None

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
    nome: str

class ClienteCreate(ClienteBase):
    email: EmailStr
    telefone: str
    cnpj: str
    tipo: str


class ClienteOut(ClienteBase):
    id: int
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


class ServicoCreate(ServicoBase):
    descricao: Optional[str] = None


class ServicoOut(ServicoBase):
    id: int
    descricao: Optional[str] = None

    class Config:
        from_attributes = True

#Schemas Produto

class ProdutoBase(BaseModel):
    nome: str


class ProdutoCreate(ProdutoBase):
    descricao: Optional[str] = None


class ProdutoOut(ProdutoBase):
    id: int
    descricao: Optional[str] = None

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