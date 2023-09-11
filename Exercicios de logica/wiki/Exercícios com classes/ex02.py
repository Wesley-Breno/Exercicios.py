"""
Classe Quadrado: Crie uma classe que modele um quadrado:

Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
"""


class Quadrado:
    def __init__(self, tamanho_do_lado):
        self.tamanho_do_lado = tamanho_do_lado

    def mudar_valor_do_lado(self, novo_valor):
        self.tamanho_do_lado = novo_valor
        print(f'O novo tamanho dos lados é {self.tamanho_do_lado}')

    def retorna_valor_do_lado(self):
        return self.tamanho_do_lado

    def calcular_area(self):
        print(f'Area calculada: {self.tamanho_do_lado**2:.1f}')


if __name__ == '__main__':
    quadrado1 = Quadrado(5)
    quadrado1.calcular_area()
    quadrado1.mudar_valor_do_lado(10)
    quadrado1.calcular_area()
    quadrado1_retorno = quadrado1.retorna_valor_do_lado()
    print(f'Retorno: {quadrado1_retorno}')
    