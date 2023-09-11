"""
Especificar os tipoes de objetos a serem criados usando uma instancia-prototipo e criar novos objetos pela
copia desse prototipo.
"""
from __future__ import annotations
from typing import List
from copy import deepcopy


class StringReprMixin:
    def __str__(self):
        params = ', '.join(
            [f'{k}={v}' for k, v in self.__dict__.items()]
        )
        return f'{self.__class__.__name__}({params})'

    def __repr__(self):
        return self.__str__()


class Address(StringReprMixin):
    def __init__(self, street: str, number: str) -> None:
        self.street = street
        self.number = number


class Person(StringReprMixin):
    def __init__(self, firstname: str, lastname: str) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.addresses: List[Address] = []

    def add_addresses(self, address: Address) -> None:
        self.addresses.append(address)

    def clone(self) -> Person:
        return deepcopy(self)


if __name__ == '__main__':
    luiz = Person('Luiz', 'Miranda')
    endereco_luiz = Address('Rua da moeda', '145')
    luiz.add_addresses(endereco_luiz)

    esposa_luiz = luiz.clone()
    esposa_luiz.firstname = 'Leticia'

    print(luiz)
    print(esposa_luiz)
