"""
Crie uma Fazenda de Bichinhos instanciando vários objetos bichinho e mantendo o controle deles através de uma lista.
Imite o funcionamento do programa básico, mas ao invés de exigis que o usuário tome conta de um único bichinho, exija
que ele tome conta da fazenda inteira. Cada opção do menu deveria permitir que o usuário executasse uma ação para todos
os bichinhos (alimentar todos os bichinhos, brincar com todos os bichinhos, ou ouvir a todos os bichinhos). Para tornar
o programa mais interessante, dê para cada bichinho um nivel inicial aleatório de fome e tédio.
"""
from time import sleep
from random import randint


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
        print(f'Brincando com {self.nome}...')
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
        [Situacao da {self.nome}]
Nome: {self.nome}
Fome: {self.fome}
Saude: {self.saude}
Idade: {self.idade}
Humor: {self.humor}''')
        sleep(3)

    def obter_nome(self):
        return self.nome

    def obter_fome(self):
        return self.fome

    def obter_saude(self):
        return self.saude

    def obter_idade(self):
        return self.idade


if __name__ == '__main__':
    # Definindo os animais da fazenda
    galinha = Tamagochi('Galinha')
    galinha.fome = randint(0, 100)
    galinha.humor = randint(0, 100)

    papagaio = Tamagochi('Papagaio')
    papagaio.fome = randint(0, 100)
    papagaio.humor = randint(0, 100)

    boi = Tamagochi('Boi')
    boi.fome = randint(0, 100)
    boi.humor = randint(0, 100)

    animais_da_fazenda = [galinha, papagaio, boi]

    # Iniciando o cuidado de todos os animais e parando so quando o usuario decidir
    while True:
        acao = input("""
    \t\t[Fazenda]
[ 1 ] - Alimentar todos os animais
[ 2 ] - Brincar com todos os animais
[ 3 ] - Ouvir todos os animais
[ 4 ] - Encerrar cuidados

Realizar a acao: """)

        if acao in ['1', '2', '3', '4']:  # Se o usuario escolheu uma das acoes
            if acao == '4':
                print('\n\n\t\tCuidados aos animais foi encerrado por hoje!\n\n')
                break

            if acao == '1':
                [animal.dar_comida(10) for animal in animais_da_fazenda]
                print('\n\n\t\tOs animais foram alimentados!\n\n')

            if acao == '2':
                [animal.brincar(5) for animal in animais_da_fazenda]
                print('\n\n\t\tVoce brincou com os animais!\n\n')

            if acao == '3':
                print('\n\n\t\t[Mostrando os atributos dos animais]\n')
                [animal._mostrar_atributos() for animal in animais_da_fazenda]

        else:
            print('\n\n\t\t[ERRO]: Escolha uma das acoes a serem feitas\n\n')
