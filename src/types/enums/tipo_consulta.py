from sqlalchemy import Enum as SQLAlchemyEnum


TipoDeConsulta = SQLAlchemyEnum("Retorno", "Rotina", "Emergência", name="tipo_de_consulta")
