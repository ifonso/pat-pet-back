from sqlalchemy import Enum as SQLAlchemyEnum


TipoServico = SQLAlchemyEnum("Banho", "Tosa", "Consulta", name="tipo_de_servico")
