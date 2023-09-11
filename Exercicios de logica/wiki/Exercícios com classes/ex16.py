"""
Crie uma "porta escondida" no programa do programa do bichinho virtual que mostre os valores exatos dos atributos do
objeto. Consiga isto mostrando o objeto quando uma opção secreta, não listada no menu, for informada na escolha do
usuário. Dica: acrescente um método especial str() à classe Bichinho.
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

    def _mostrar_atributos(self):
        print(f'''
        [Atributos]
Nome: {self.nome}
Fome: {self.fome}
Saude: {self.saude}
Idade: {self.idade}
Humor: {self.humor}''')

    def obter_nome(self):
        return self.nome

    def obter_fome(self):
        return self.fome

    def obter_saude(self):
        return self.saude

    def obter_idade(self):
        return self.idade


if __name__ == '__main__':
    bixin = Tamagochi('Jose')
    bixin._mostrar_atributos()
    