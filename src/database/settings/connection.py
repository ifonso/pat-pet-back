import os

from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import Engine, create_engine

__host = os.getenv("PSQL_HOST", "127.0.0.1")
__port = os.getenv("PSQL_PORT", "5432")
__database = os.getenv("PSQL_DB", "patpet")
__user = os.getenv("PSQL_USER", "backend")
__password = os.getenv("PSQL_PASS", "admin")

class __DatabaseConnectionHandler:

    __connection_string: str
    __engine: Engine
    __session: Session | None

    @property
    def session(self) -> Session:
        if self.__session == None:
            raise Exception("Session does not exist.")
        
        return self.__session

    def __init__(self, connection_string: str) -> None:
        self.__connection_string = connection_string
        self.__engine = create_engine(url=self.__connection_string)
        self.__session = None

    def __enter__(self):
        session_maker = sessionmaker()
        self.__session = session_maker(bind=self.__engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.session != None:
            self.session.close()


db_connection_handler = __DatabaseConnectionHandler(f"postgresql+psycopg2://{__user}:{__password}@{__host}:{__port}/{__database}")
