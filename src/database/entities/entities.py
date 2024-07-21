import uuid

from src.database.settings.base import Base

from sqlalchemy import Column, String, Float, Date, Boolean, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID, BYTEA
from sqlalchemy.sql import func

from src.types.enums.especies_animal import EspeciesAnimal
from src.types.enums.sexo_animal import SexoAnimal
from src.types.enums.tipo_profissional import TipoProfissional
from src.types.enums.tipo_servico import TipoServico
from src.types.enums.status_agendamento import StatusAgendamento
from src.types.enums.tipo_consulta import TipoDeConsulta


class Endereco(Base):
    __tablename__ = "enderecos"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    cidade = Column(String(100), nullable=False)
    estado = Column(String(100), nullable=False)
    rua = Column(String(100), nullable=False)
    casa = Column(String(100), nullable=False)
    cep = Column(String(10), nullable=False)

    def __repr__(self) -> str:
        return f"Endereco(cidade={self.cidade}, estado={self.estado}, rua={self.rua}, casa={self.casa}, cep={self.cep})"


class Tutor(Base):
    __tablename__ = "tutores"

    id = Column(String(16), primary_key=True, unique=True, index=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(60), nullable=False, unique=True)
    telefone = Column(String(12), nullable=False, unique=True)
    endereco_id = Column(UUID(as_uuid=True), ForeignKey("enderecos.id"), nullable=False)
    
    endereco = relationship("Endereco")

    def __repr__(self) -> str:
        return f"Endereco(cidade={self.cidade}, estado={self.estado}, rua={self.rua}, casa={self.casa}, cep={self.cep})"


class Pet(Base):
    __tablename__ = "pets"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    nome = Column(String(100), nullable=False)
    especie = Column(EspeciesAnimal, nullable=False)
    sexo = Column(SexoAnimal, nullable=False)
    raca = Column(String(100), nullable=False)
    peso = Column(Float, nullable=False)
    data_nascimento = Column(Date, nullable=False)
    castrado = Column(Boolean, nullable=False),
    data_castracao = Column(Date)
    vacinas = Column(Text)
    informacoes_adicionais = Column(Text)
    tutor_id = Column(UUID(as_uuid=True), ForeignKey("tutores.id"), nullable=False)

    tutor = relationship("Tutor")

    def __repr__(self) -> str:
        return f"Pet(nome={self.nome}, especie={self.especie}, sexo={self.sexo}, raca={self.raca}, peso={self.peso}, data_nascimento={self.data_nascimento})"


class Profissional(Base):
    __tablename__ = "profissionais"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    senha = Column(String(60), nullable=False)
    tipo_profissional = Column(TipoProfissional, nullable=False)
    data_cadastro = Column(DateTime, default=func.now())

    def __repr__(self) -> str:
        return f"Profissional(nome={self.nome}, email={self.email}, tipo_profissional={self.tipo_profissional})"


class Servico(Base):
    __tablename__ = "servicos"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    tipo_de_servico = Column(TipoServico, nullable=False)
    observacoes = Column(Text)
    valor_de_servico = Column(Float, nullable=False)
    data_realizacao = Column(DateTime)
    pet_id = Column(UUID(as_uuid=True), ForeignKey("pets.id"), nullable=False)
    profissional_id = Column(UUID(as_uuid=True), ForeignKey("profissionais.id"), nullable=False)

    pet = relationship("Pet")
    profissional = relationship("Profissional")

    def __repr__(self) -> str:
        return f"Servico(tipo_de_servico={self.tipo_de_servico}, observacoes={self.observacoes}, valor_de_servico={self.valor_de_servico}, data_realizacao={self.data_realizacao})"


class Agendamento(Base):
    __tablename__ = "agendamentos"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    data_agendamento = Column(DateTime, nullable=False)
    tutor_id = Column(String(16), ForeignKey("tutores.id"), nullable=False)
    profissional_id = Column(UUID(as_uuid=True), ForeignKey("profissionais.id"), nullable=False)
    servico_id = Column(UUID(as_uuid=True), ForeignKey("servicos.id"), nullable=False)
    status_agendamento = Column(StatusAgendamento, nullable=False)
    data_criacao_agendamento = Column(DateTime, nullable=False, default=func.now())

    tutor = relationship("Tutor")
    profissional = relationship("Profissional")
    servico = relationship("Servico")

    def __repr__(self) -> str:
        return f"Agendamento(data_agendamento={self.data_agendamento}, tutor_id={self.tutor_id}, profissional_id={self.profissional_id}, servico_id={self.servico_id}, status_agendamento={self.status_agendamento}, data_criacao_agendamento={self.data_criacao_agendamento})"


class Exame(Base):
    __tablename__ = "exames"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    animal_id = Column(UUID(as_uuid=True), nullable=False)
    dados_exame = Column(BYTEA)
    data_exame = Column(DateTime)
    observacoes = Column(Text)
    data_criacao = Column(DateTime)


class Consulta(Base):
    __tablename__ = "consultas"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    servico_associado = Column(UUID(as_uuid=True), ForeignKey("servicos.id"), nullable=False)
    tipo = Column(TipoDeConsulta, nullable=False)
    exames_ssociados = Column(UUID(as_uuid=True), ForeignKey("exames.id"))
    id_consulta_associada = Column(UUID(as_uuid=True), ForeignKey("consultas.id"))
    motivo_da_consulta = Column(Text)
    situacao_do_animal = Column(Text)
    exame_fisico = Column(Text)
    diagnostico = Column(Text)
    tratamento = Column(Text)
    solicitacao_retorno = Column(Boolean)
    data_criacao = Column(DateTime)
    
    servico = relationship("Servico")
    exame = relationship("Exame", foreign_keys=[exames_ssociados])
    consulta_associada = relationship("Consulta", remote_side=[id])
