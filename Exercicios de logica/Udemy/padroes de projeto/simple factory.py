"""
Aprendendo sobre criacao de uma simple factory
"""

from abc import ABC, abstractmethod


class Veiculo(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None:
        pass


class CarroLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print('Carro de luxo esta buscando o cliente...')


class CarroPopular(Veiculo):
    def buscar_cliente(self) -> None:
        print('Carro popular esta buscando o cliente...')


class MotoLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print('Moto de luxo esta buscando o cliente...')


class MotoPopular(Veiculo):
    def buscar_cliente(self) -> None:
        print('Moto popular esta buscando o cliente...')


class VeiculoFactory:
    """
    Factory que recebe o tipo de objeto que o usuario quer e o chama.
    """
    def __init__(self, tipo):
        self.carro = self.get_carro(tipo)  # Recebendo o tipo de objeto e chamando.

    @staticmethod
    def get_carro(tipo: str) -> Veiculo:  # Chamando o objeto.

        if tipo == 'luxo':
            return CarroLuxo()

        if tipo == 'popular':
            return CarroPopular()

        if tipo == 'moto luxo':
            return MotoLuxo()

        if tipo == 'moto popular':
            return MotoPopular()

        assert 0, 'Veiculo nao existe.'

    def buscar_cliente(self):  # Iniciando metodo abstrato do objeto pela factory.
        self.carro.buscar_cliente()


if __name__ == '__main__':
    from random import choice
    carros_disponiveis = ['luxo', 'popular', 'moto luxo', 'moto popular']

    for i in range(10):  # Chamando varios tipos de objetos 10 vezes
        carro = VeiculoFactory(choice(carros_disponiveis))
        carro.buscar_cliente()
