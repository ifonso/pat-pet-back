from src.database.entities.entities import Profissional
from src.database.settings.connection import db_connection_handler

from sqlalchemy.exc import IntegrityError, SQLAlchemyError


class ProfissionalRepository:

    def create(self, nome: str, email: str, senha: str, tipo_profissional: str) -> Profissional:
        with db_connection_handler as db:
            try:
                novo_profissional = Profissional(
                    nome=nome,
                    email=email,
                    senha=senha,
                    tipo_profissional=tipo_profissional
                )

                db.session.add(novo_profissional)
                db.session.commit()
            
            except IntegrityError:
                db.session.rollback()
                raise ValueError("Email já cadastrado.")

            except SQLAlchemyError as e:
                db.session.rollback()
                raise RuntimeError("Erro no banco de dados: " + str(e))

            except Exception as e:
                db.session.rollback()
                raise RuntimeError("Erro inesperado: " + str(e))
    
    def get_by_id(self, id: str) -> Profissional | None:
        with db_connection_handler as db:
            try:
                return db.session.query(Profissional).filter(Profissional.id == id).first()
            
            except SQLAlchemyError as e:
                raise RuntimeError("Erro no banco de dados: " + str(e))
    
    def get_all(self) -> list[Profissional]:
        with db_connection_handler as db:
            try:
                return db.session.query(Profissional).all()
            
            except SQLAlchemyError as e:
                raise RuntimeError("Erro no banco de dados: " + str(e))
    
    def delete_by_id(self, id: str) -> None:
        with db_connection_handler as db:
            try:
                rows_deleted = db.session.query(Profissional).filter(Profissional.id == id).delete()
                db.session.commit()

                if rows_deleted == 0:
                    raise ValueError(f"Nenhum profissional encontrado com ID: {id}")
            
            except SQLAlchemyError as e:
                db.session.rollback()
                raise RuntimeError("Erro no banco de dados: " + str(e))
            
            except Exception as e:
                db.session.rollback()
                raise RuntimeError("Erro inesperado: " + str(e))
