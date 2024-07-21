from src.database.repositories.profissional_repository import ProfissionalRepository
from src.types.profissional_data import ProfissionalData
from src.types.requests import CreateProfissionalRequest


class Controller:

    profissional_repository: ProfissionalRepository = ProfissionalRepository()

    def get_profissionais(self):
        profissionais = self.profissional_repository.get_all()

        return [
            ProfissionalData(
                id=str(profissional.id),
                nome=profissional.nome,
                email=profissional.email,
                tipo_profissional=profissional.tipo_profissional,
                data_cadastro=str(profissional.data_cadastro)
            ) for profissional in profissionais
        ]
    
    def create_profissional(self, request: CreateProfissionalRequest):
        profissional = self.profissional_repository.create(
            nome=request.nome,
            email=request.email,
            senha=request.senha,
            tipo_profissional=request.tipo_profissional
        )

        return ProfissionalData(
            id=str(profissional.id),
            nome=profissional.nome,
            email=profissional.email,
            tipo_profissional=profissional.tipo_profissional,
            data_cadastro=str(profissional.data_cadastro)
        )
