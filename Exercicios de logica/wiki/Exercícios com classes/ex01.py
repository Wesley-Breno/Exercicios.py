"""
Classe Bola: Crie uma classe que modele uma bola:

Atributos: Cor, circunferência, material
Métodos: trocaCor e mostraCor
"""

from random import choice


class Bola:
    def __init__(self, cor, circuferencia, material):
        self.cor = cor
        self.circuferencia = circuferencia
        self.material = material

    def troca_cor(self):
        """
        Metodo que troca a cor da bola para Azul, Verde ou Vermelho.
        :return: None
        """
        cores = ['Azul', 'Verde', 'Vermelho']
        troca = choice(cores)

        while troca == self.cor:
            troca = choice(cores)

        self.cor = troca

    def mostra_cor(self):
        """
        Metodo que mostra na tela a cor atual da bola
        :return: None
        """
        print(f'A cor da bola é {self.cor}')


if __name__ == '__main__':
    bola = Bola('Amarelo', 12, 'Plastico')
    bola.mostra_cor()
    bola.troca_cor()
    bola.mostra_cor()
