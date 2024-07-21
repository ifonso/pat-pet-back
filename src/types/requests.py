from pydantic import BaseModel


class CreateProfissionalRequest(BaseModel):
    nome: str
    email: str
    tipo_profissional: str
    senha: str
