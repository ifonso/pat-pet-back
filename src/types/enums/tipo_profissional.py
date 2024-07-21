from sqlalchemy import Enum as SQLAlchemyEnum


TipoProfissional = SQLAlchemyEnum("Veterinário", "Cuidador", "Administrador", name="tipo_profissional")
