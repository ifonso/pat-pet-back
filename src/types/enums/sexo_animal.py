from sqlalchemy import Enum as SQLAlchemyEnum


SexoAnimal = SQLAlchemyEnum("Macho", "Fêmea", name="sexo")
