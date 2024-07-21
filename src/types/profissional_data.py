from pydantic import BaseModel


class ProfissionalData(BaseModel):
    id: str
    nome: str
    email: str
    tipo_profissional: str
    data_cadastro: str
