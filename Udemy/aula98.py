from datetime import datetime


class Pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def falar(self, assunto):
        if self.falando:
            print('Voce ja esta falando')
            return

        if self.comendo:
            print(f'{self.nome} Nao seja mal educado! termine de comer para falar.')
            return

        print(f'{self.nome} esta falando sobre {assunto}')
        self.falando = True

    def parar_de_falar(self):
        if not self.falando:
            print(f'{self.nome}Ja parou de falar faz um tempo.')
            return

        print(f'{self.nome} parou de falar.')
        self.falando = False

    def comer(self, comida):
        if self.comendo:
            print(f'{self.nome} ja esta comendo.')
            return

        print(f'{self.nome} esta comendo {comida}')
        self.comendo = True

    def parar_de_comer(self):
        if not self.comendo:
            print(f'{self.nome} ja parou de comer.')
            return

        print(f'{self.nome} parou de comer.')
        self.comendo = False

    def pegar_ano_nascimento(self):
        return self.ano_atual - self.idade


p1 = Pessoa('Werlindo', 18)
p2 = Pessoa('Adalberto', 33)
print(p1.pegar_ano_nascimento())
print(p2.pegar_ano_nascimento())
