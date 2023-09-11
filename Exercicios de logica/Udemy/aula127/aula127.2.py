"""
Criar uma classe que recebe numeros e depois transformalos em tupla usando
o modulo dataclasses.
"""

from dataclasses import dataclass, astuple  # Importando o modulo dataclasses com o decorador dataclass e o astuple


@dataclass
class Numeros:
    n1: int
    n2: int
    n3: int


nums = Numeros(1, 2, 3)
print(astuple(nums))  # Printando na tela os valores da classe em uma tupla.
