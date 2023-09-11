"""
Classe Pessoa: Crie uma classe que modele uma pessoa:

Atributos: nome, idade, peso e altura
Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a
idade dela menor que 21 anos, ela deve crescer 0,5 cm.
"""


class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        if self.idade < 21:
            self.altura += 0.5
            self.idade += 1
            print(f'{self.nome} envelheceu 1 ano e cresceu 0,5 centimetros')
        else:
            self.idade += 1
            print(f'{self.nome} envelheceu 1 ano')

    def engordar(self):
        self.peso += 1
        print(f'{self.nome} engordou 1kg')

    def emagrecer(self):
        self.peso -= 1
        print(f'{self.nome} emagreceu 1kg')

    def crescer(self):
        self.altura += 1
        print(f'{self.nome} cresceu 1 centimetro')


pessoa1 = Pessoa('Wesley', 19, 54, 169)
pessoa1.crescer()
pessoa1.engordar()
pessoa1.emagrecer()
pessoa1.envelhecer()
print(f'\n[{pessoa1.nome}]\n'
      f'Altura: {pessoa1.altura}\n'
      f'Idade: {pessoa1.idade}\n'
      f'Peso: {pessoa1.peso}')
