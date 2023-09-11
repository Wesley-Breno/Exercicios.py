"""
Classe Retangulo: Crie uma classe que modele um retangulo:

Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. Depois, deve
criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.
"""


class Retangulo:
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura

    def mudar_valor_dos_lados(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura

    def retornar_valor_dos_lados(self):
        return self.comprimento, self.largura

    def calcular_area(self):
        return self.comprimento * self.largura

    def calcular_perimetro(self):
        return (self.comprimento * 2) + (self.largura * 2)


if __name__ == '__main__':
    comprimento = float(input('Informe o comprimento do local em metros: '))
    largura = float(input('Informe a largura do local em metros: '))

    obj1 = Retangulo(comprimento, largura)
    pisos = obj1.calcular_area()
    rodapes = obj1.calcular_perimetro()

    print(f'Total de pisos necessarios: {pisos}')
    print(f'Total de rodapes necessarios: {rodapes}')
