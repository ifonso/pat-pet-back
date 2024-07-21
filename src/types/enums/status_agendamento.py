from sqlalchemy import Enum as SQLAlchemyEnum


StatusAgendamento = SQLAlchemyEnum("Agendado", "Cancelado", "Realizado", name="status")
