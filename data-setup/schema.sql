-- Habilita a extensão uuid-ossp
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Cria enum com tipos de profissionais
CREATE TYPE tipo_profissional AS ENUM (
    'Veterinário',
    'Cuidador',
    'Administrador'
);

-- Cria a tabela de profissionais
CREATE TABLE IF NOT EXISTS profissionais (
    id uuid PRIMARY KEY UNIQUE DEFAULT uuid_generate_v4(),
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    senha VARCHAR(60) NOT NULL,
    tipo_profissional tipo_profissional NOT NULL,
    data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Cria a table de endereços
CREATE TABLE IF NOT EXISTS enderecos (
    id uuid PRIMARY KEY UNIQUE DEFAULT uuid_generate_v4(),
    cidade VARCHAR(100) NOT NULL,
    estado VARCHAR(100) NOT NULL,
    rua VARCHAR(100) NOT NULL,
    casa VARCHAR(100) NOT NULL,
    cep VARCHAR(10) NOT NULL
);

-- Cria a tabela de tutores
CREATE TABLE IF NOT EXISTS tutores (
   id VARCHAR(16) PRIMARY KEY UNIQUE,
   nome VARCHAR(100) NOT NULL,
   email VARCHAR(60) NOT NULL UNIQUE,
   telefone VARCHAR(12) NOT NULL UNIQUE,
   endereco_id uuid NOT NULL,

   CONSTRAINT fk_endereco FOREIGN KEY (endereco_id) REFERENCES enderecos(id)
);

-- Cria enum com espécies de animais
CREATE TYPE especie AS ENUM (
    'Cachorro',
    'Gato'
);

-- Cria enum com o sexo dos animais
CREATE TYPE sexo AS ENUM (
    'Macho',
    'Fêmea'
);

-- Cria a tabela de pets
CREATE TABLE IF NOT EXISTS pets (
    id uuid PRIMARY KEY UNIQUE DEFAULT uuid_generate_v4(),
    nome VARCHAR(100) NOT NULL,
    especie especie NOT NULL,
    sexo sexo NOT NULL,
    raca VARCHAR(100) NOT NULL,
    peso REAL NOT NULL,
    data_nascimento DATE NOT NULL,
    castrado BOOLEAN NOT NULL,
    data_castracao DATE,
    vacinas TEXT,
    informacoes_adicionais TEXT,
    tutor_id VARCHAR(16) NOT NULL,

    CONSTRAINT fk_tutor FOREIGN KEY (tutor_id) REFERENCES tutores(id)
);

-- Cria enum com os tipos de serviço
CREATE TYPE tipo_de_servico AS ENUM (
    'Banho',
    'Tosa',
    'Consulta'
);

-- Cria a tabela de seviços
CREATE TABLE IF NOT EXISTS servicos (
    id uuid PRIMARY KEY UNIQUE DEFAULT uuid_generate_v4(),
    tipo_de_servico tipo_de_servico NOT NULL,
    pet_id uuid NOT NULL,
    profissional_id uuid NOT NULL,
    observacoes TEXT,
    valor_de_servico REAL NOT NULL,
    data_realizacao TIMESTAMP,

    CONSTRAINT fk_profissional FOREIGN KEY (profissional_id) REFERENCES profissionais(id),
    CONSTRAINT fk_pet FOREIGN KEY (pet_id) REFERENCES pets(id)
);

-- Cria enum com os status de agendamento
CREATE TYPE status AS ENUM (
    'Agendado',
    'Cancelado',
    'Realizado'
);

-- Cria a tabela de agendamentos
CREATE TABLE IF NOT EXISTS agendamentos (
    id uuid PRIMARY KEY UNIQUE DEFAULT uuid_generate_v4(),
    data_agendamento TIMESTAMP NOT NULL,
    tutor_id VARCHAR(16) NOT NULL,
    profissional_id uuid NOT NULL,
    servico_id uuid NOT NULL,
    status_agendamento status NOT NULL,
    data_criacao_agendamento TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_profissional FOREIGN KEY (profissional_id) REFERENCES profissionais(id),
    CONSTRAINT fk_tutor FOREIGN KEY (tutor_id) REFERENCES tutores(id),
    CONSTRAINT fk_servico FOREIGN KEY (servico_id) REFERENCES servicos(id)
);

-- Cria enum com os tipos de consulta
CREATE TYPE tipo_de_consulta AS ENUM (
    'Rotina',
    'Emergência',
    'Retorno'
);

-- Cria a tabela de exames
CREATE TABLE IF NOT EXISTS exames (
    id uuid PRIMARY KEY UNIQUE DEFAULT uuid_generate_v4(),
    animal_id uuid NOT NULL,
    dados_exame bytea,
    data_exame TIMESTAMP,
    observacoes TEXT,
    data_criacao TIMESTAMP
);

-- Cria a tabela de consultas
CREATE TABLE IF NOT EXISTS consultas (
    id uuid PRIMARY KEY UNIQUE DEFAULT uuid_generate_v4(),
    servico_associado uuid NOT NULL,
    tipo tipo_de_consulta NOT NULL,
    exames_ssociados uuid,
    id_consulta_associada uuid,
    motivo_da_consulta TEXT,
    situacao_do_animal TEXT,
    exame_fisico TEXT,
    diagnostico TEXT,
    tratamento TEXT,
    solicitacao_retorno BOOLEAN,
    data_criacao TIMESTAMP
);
