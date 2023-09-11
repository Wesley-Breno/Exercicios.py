"""
Criar uma classe que recebe nome e sobrenome
e fazer virar um dicionario.
"""

from dataclasses import dataclass, asdict  # Importando o modulo dataclasses com o decorador dataclass e a função asdict


@dataclass
class Pessoa:
    nome: str
    sobrenome: str


pessoa1 = Pessoa('wesley', 'breninho')
print(asdict(pessoa1))  # Printando na tela as variaveis da classe Pessoa e os valores como um dicionario.
