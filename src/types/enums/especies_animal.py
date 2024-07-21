from sqlalchemy import Enum as SQLAlchemyEnum


EspeciesAnimal = SQLAlchemyEnum("Cachorro", "Gato", name="especie")
