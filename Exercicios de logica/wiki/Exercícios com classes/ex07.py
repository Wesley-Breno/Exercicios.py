"""
Classe Bichinho Virtual:
Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):
 * Atributos: Nome, Fome, Saúde e Idade b.
 * Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade
Obs: Existe mais uma informação que devemos levar em consideração, o Humor do nosso tamagushi, este humor é uma
combinação entre os atributos Fome e Saúde, ou seja, um campo calculado, então não devemos criar um atributo para
armazenar esta informação por que ela pode ser calculada a qualquer momento.
"""


class Tamagochi:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 0
        self.saude = 100
        self.idade = 1
        self.__humor = 100

    def alterar_nome(self, novo_nome: str):
        self.nome = novo_nome

    def altera_fome(self, nova_fome: int):
        if nova_fome <= 0:
            nova_fome = 0
        if nova_fome >= 100:
            nova_fome = 100

        self.fome = nova_fome
        self.calcula_humor()

    def altera_saude(self, nova_saude: int):
        if nova_saude <= 0:
            nova_saude = 0
        if nova_saude >= 100:
            nova_saude = 100

        self.saude = nova_saude
        self.calcula_humor()

    def altera_idade(self, nova_idade: int):
        if nova_idade <= 0:
            nova_idade = 0

        self.idade = nova_idade

    def calcula_humor(self):
        if self.fome == 0 and self.saude == 100:
            self.__humor += 1
        else:
            self.__humor -= 1

        if self.__humor >= 100:
            self.__humor = 100
        if self.__humor <= 0:
            self.__humor = 0

    def obter_nome(self):
        return self.nome

    def obter_fome(self):
        return self.fome

    def obter_saude(self):
        return self.saude

    def obter_idade(self):
        return self.idade


if __name__ == '__main__':
    a = Tamagochi('Josicleiton')
    a.altera_fome(99)
    a.altera_saude(100)
    a.alterar_nome('Aldair')
    a.altera_fome(0)
    a.altera_idade(13)
