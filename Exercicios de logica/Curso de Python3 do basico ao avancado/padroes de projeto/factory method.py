"""
Aprendendo sobre factory method
Neste exemplo é usado o factory method para retornar um tipo especifico de carro para usuarios da zona sul e outros
tipos especificos de carros para usuarios da zona norte.
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


class VeiculoFactory(ABC):
    """
    Factory que recebe o tipo de carro que o usuario quer.
    """
    def __init__(self, tipo):
        self.carro = self.get_carro(tipo)  # Recebendo o tipo de carro.

    @staticmethod
    @abstractmethod
    def get_carro(tipo: str) -> Veiculo: pass

    def buscar_cliente(self):  # Metodo que sera responsavel por 'chamar' o carro.
        self.carro.buscar_cliente()


class ZonaNorteVeiculoFactory(VeiculoFactory):

    @staticmethod
    def get_carro(tipo: str) -> Veiculo:  # Chamando o carro com base no tipo especificado.

        if tipo == 'luxo':
            return CarroLuxo()

        if tipo == 'popular':
            return CarroPopular()

        if tipo == 'moto luxo':
            return MotoLuxo()

        if tipo == 'moto popular':
            return MotoPopular()

        assert 0, 'Veiculo nao existe.'


class ZonaSulVeiculoFactory(VeiculoFactory):

    @staticmethod
    def get_carro(tipo: str) -> Veiculo:  # Chamando o unico carro que tem na zona sul.
        if tipo == 'popular':
            return CarroPopular()

        assert 0, 'Veiculo nao existe.'


if __name__ == '__main__':
    from random import choice
    veiculos_disponiveis_zona_norte = ['luxo', 'popular', 'moto luxo', 'moto popular']
    veiculos_disponiveis_zona_sul = ['popular']

    print('\n\t\tZona norte\n')
    for i in range(10):  # Chamando varios tipos de carros 10 vezes
        carro = ZonaNorteVeiculoFactory(choice(veiculos_disponiveis_zona_norte))
        carro.buscar_cliente()

    print('\n\t\tZona sul\n')
    for i in range(10):  # Chamando o unico carro que tem na zona sul 10 vezes.
        carro2 = ZonaSulVeiculoFactory(choice(veiculos_disponiveis_zona_sul))
        carro2.buscar_cliente()
