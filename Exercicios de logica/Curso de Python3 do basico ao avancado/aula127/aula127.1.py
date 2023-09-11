"""
Criar uma classe que recebe nome e sobrenome,
depois criar uma funçao com __post_init__ que
vai ter uma variavel e fazer retornar o nome e sobrenome juntos.
"""

from dataclasses import dataclass  # Importando o decorador dataclass do modulo dataclasses


@dataclass  # Criando a classe com dataclass
class Pessoa:
    # Nome e sobrenome com o dataclass agindo
    nome: str
    sobrenome: str

    # Funcao que vai criar uma variavel onde ira ficar o nome completo
    def __post_init__(self):
        self.nome_completo = f'{self.nome} {self.sobrenome}'


p = Pessoa('werli', 'breno')
print(p.nome_completo)
