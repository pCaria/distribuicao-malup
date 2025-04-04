from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Enum, Boolean, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base
import enum

class Permissao(Base):
    __tablename__ = "permissao"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(50), unique=True, nullable=False)  # Ex: 'admin', 'funcionario', 'visualizador'

    usuarios = relationship("Usuario", back_populates="permissao")


class Usuario(Base):
    __tablename__ = "usuario"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    senha_hash = Column(String(255), nullable=False)
    FK_permissao_ID = Column(Integer, ForeignKey("permissao.id"))
    criado_em = Column(DateTime, default=datetime.now())

    permissao = relationship("Permissao", back_populates="usuarios")
    logs_acesso = relationship("LogAcesso", back_populates="usuario")


class LogAcesso(Base):
    __tablename__ = "log_acesso"

    id = Column(Integer, primary_key=True, index=True)
    FK_usuario_ID = Column(Integer, ForeignKey("usuario.id"))
    ip = Column(String(45))
    data_hora = Column(DateTime, default=datetime.now())
    acao = Column(String(255))  # Ex: 'Login', 'Alteração de Orçamento'

    usuario = relationship("Usuario", back_populates="logs_acesso")

# Enum para tipos de clientes
class TipoCliente(Base):
    __tablename__ = 'tipo_cliente'

    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False, unique=True)

# Enum para tipos de taxa
class TipoTaxaEnum(str, enum.Enum):
    administrativa = "administrativa"
    urgencia = "urgencia"

class Cliente(Base):
    __tablename__ = "cliente"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    telefone = Column(String(20))
    cnpj = Column(String(20))
    FK_tipo_cliente_ID = Column(Integer, ForeignKey('tipo_cliente.id'), nullable=False)
    
    tipo_cliente = relationship("TipoCliente")
    orcamentos = relationship("Orcamento", back_populates="cliente")

class Orcamento(Base):
    __tablename__ = "orcamento"

    id = Column(Integer, primary_key=True, index=True)
    FK_cliente_ID = Column(Integer, ForeignKey("cliente.id"), nullable=False)
    data_orcamento = Column(DateTime, default=datetime.now())
    status = Column(Enum('Pendente', 'Aprovado', 'Recusado', 'Fechado'), default='Pendente', nullable=False)
    data_fechamento = Column(DateTime, nullable=True)

    cliente = relationship("Cliente", back_populates="orcamentos")
    servicos = relationship("OrcamentoServico", back_populates="orcamento")

class Servico(Base):
    __tablename__ = "serviço"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255), nullable=False)
    descricao = Column(String(255))

    produtos = relationship("ServicoProduto", back_populates="servico")
    orcamentos = relationship("OrcamentoServico", back_populates="servico")

class Produto(Base):
    __tablename__= "produto"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255), nullable=False)
    descricao = Column(String(255))

    precos = relationship("ValorProduto", back_populates="produto")
    servicos_produto = relationship("ServicoProduto", back_populates="produto")

class OrcamentoServico(Base):
    __tablename__ = "orcamento_serviço"

    id = Column(Integer, primary_key=True, index=True)
    FK_orcamento_ID = Column(Integer, ForeignKey("orcamento.id"), nullable=False)
    FK_servico_ID = Column(Integer, ForeignKey("serviço.id"), nullable=False)

    orcamento = relationship("Orcamento", back_populates="servicos")
    servico = relationship("Servico", back_populates="orcamentos")
    produtos = relationship("OrcamentoProduto", back_populates="orcamento_servico")

class ServicoProduto(Base):
    __tablename__= "serviço_produto"

    id = Column(Integer, primary_key=True, index=True)
    FK_servico_ID = Column(Integer, ForeignKey("serviço.id"), nullable=False)
    FK_produto_ID = Column(Integer, ForeignKey("produto.id"), nullable=False)

    servico = relationship("Servico", back_populates="produtos")
    produto = relationship("Produto", back_populates="servicos_produto")

class OrcamentoProduto(Base):
    __tablename__ = "orcamento_produto"

    id = Column(Integer, primary_key=True, index=True)
    FK_orcamento_servico_ID = Column(Integer, ForeignKey("orcamento_serviço.id"), nullable=False)
    FK_produto_ID = Column(Integer, ForeignKey("produto.id"), nullable=False)
    quantidade = Column(Integer, nullable=False)
    preco_unitario = Column(Float, nullable=False)
    desconto = Column(Float, default=0.0)
    preco_final = Column(Float, nullable=False)

    orcamento_servico = relationship("OrcamentoServico", back_populates="produtos")
    produto = relationship("Produto")

class ValorProduto(Base):
    __tablename__ = "valor_produto"

    id = Column(Integer, primary_key=True, index=True)
    FK_produto_ID = Column(Integer, ForeignKey("produto.id"), nullable=False)
    FK_tipo_cliente_ID = Column(Integer, ForeignKey('tipo_cliente.id'), nullable=False)
    preco = Column(Float, nullable=False)

    tipo_cliente = relationship("TipoCliente")
    produto = relationship("Produto", back_populates="precos")

# Modelo para armazenar os valores das taxas por tipo de cliente
class TaxaValor(Base):
    __tablename__ = "taxa_valor"

    id = Column(Integer, primary_key=True, index=True)
    FK_tipo_cliente_ID = Column(Integer, ForeignKey('tipo_cliente.id'), nullable=False)
    tipo_taxa = Column(Enum(TipoTaxaEnum), nullable=False)
    valor = Column(Float, nullable=False)  # Pode ser percentual ou fixo dependendo da lógica

    tipo_cliente = relationship("TipoCliente")
    