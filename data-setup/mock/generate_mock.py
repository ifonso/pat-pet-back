import json

from enum import Enum
from faker import Faker


class TipoProfissional(Enum):
    VETERINARIO = "Veterinário"
    ADMINISTRADOR = "Administrador"
    CUIDADOR = "Cuidador"

if __name__ == "__main__":
    fake = Faker()
    profissionais = []

    for _ in range(100):
        profissionais.append({
            "nome": fake.name(),
            "email": fake.email(),
            "senha": "123456",
            "tipo_profissional": fake.random_element(elements=[type.value for type in TipoProfissional])
        })
    
    with open("profissionais.json", "w", encoding='utf-8') as f:
        json.dump(profissionais, f, indent=4)
