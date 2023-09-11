"""
Classe Bichinho Virtual++:
Melhore o programa do bichinho virtual, permitindo que o usuário especifique
quanto de comida ele fornece ao bichinho e por quanto tempo ele brinca com o
bichinho. Faça com que estes valores afetem quão rapidamente os níveis de fome
e tédio caem.
"""
from time import sleep


class Tamagochi:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 0
        self.saude = 100
        self.idade = 1
        self.humor = 100

    def alterar_nome(self, novo_nome: str):
        self.nome = novo_nome

    def brincar(self, segundos: int):
        for segundo in range(0, segundos):
            if self.humor >= 100:
                self.humor = 100
            else:
                self.humor += 1
            sleep(1)

    def dar_comida(self, quantidade: int):
        if quantidade <= 0:
            quantidade = 0
        if quantidade >= 100:
            quantidade = 100

        if self.fome - quantidade >= 0:
            self.fome -= quantidade
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
            self.humor += 1
        else:
            self.humor -= 1

        if self.humor >= 100:
            self.humor = 100
        if self.humor <= 0:
            self.humor = 0

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
    a.fome = 99
    print(a.nome)

    print(a.idade)
    print(a.fome)
    print(a.saude)
    print(a.humor)
    print('--' * 12)

    a.dar_comida(50)
    print(a.nome)
    print(a.idade)
    print(a.fome)
    print(a.saude)
    print(a.humor)
    print('--' * 12)

    a.altera_saude(100)
    print(a.nome)
    print(a.idade)
    print(a.fome)
    print(a.saude)
    print(a.humor)
    print('--' * 12)

    a.alterar_nome('Aldair')
    print(a.nome)
    print(a.idade)
    print(a.fome)
    print(a.saude)
    print(a.humor)
    print('--' * 12)

    a.dar_comida(0)
    print(a.nome)
    print(a.idade)
    print(a.fome)
    print(a.saude)
    print(a.humor)
    print('--' * 12)

    a.altera_idade(13)
    print(a.nome)
    print(a.idade)
    print(a.fome)
    print(a.saude)
    print(a.humor)
    print('--' * 12)

    a.brincar(5)
    print(a.nome)
    print(a.idade)
    print(a.fome)
    print(a.saude)
    print(a.humor)
    print('--' * 12)
