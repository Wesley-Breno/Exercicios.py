from datetime import datetime    # Importando o datetime para poder pegar a data atual.


class Pessoa:    # Criando a classe Pessoa.
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))    # Variavel da classe onde ficara o ano atual.

    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo    # Saber se a pessoa esta comendo ou nao.
        self.falando = falando    # Saber se a pessoa esta falando ou nao.

    def comer(self, comida):    # Metodo para fazer a pessoa comer.
        if self.comendo is False:    # Se a pessoa nao estiver comendo.
            print(f'{self.nome} está comendo {comida}.')
            self.comendo = True
        else:
            print(f'{self.nome} ainda nao terminou de comer.')

    def parar_comer(self):    # Metodo para fazer a pessoa parar de comer.
        if self.comendo:    # Se a pessoa estiver comendo.
            print(f'{self.nome} parou de comer.')
            self.comendo = False
        else:
            print(f'{self.nome} nao comeu nada ainda.')

    def falar(self, assunto):    # Metodo para fazer a pessoa falar.
        if self.comendo:    # Se a pessoa estiver comendo.
            print(f'{self.nome} nao pode falar enquanto come.')
        else:
            if self.falando:
                print(f'{self.nome} ainda esta falando.')
            else:
                print(f'{self.nome} comecou a falar sobre {assunto}')
                self.falando = True

    def parar_falar(self):    # Metodo para fazer a pessoa parar de falar.
        if self.falando:    # Se a pessoa estiver falando.
            print(f'{self.nome} parou de falar...')
            self.falando = False
        else:
            print(f'{self.nome} nao falou nada.')

    def ano_nascimento(self):    # Metodo para mostrar na tela o ano de nascimento da pessoa.
        ano = Pessoa.ano_atual - self.idade
        print(f'O ano de nascimento de {self.nome} é em {ano}')


p1 = Pessoa('Werli', 18)
p2 = Pessoa('Junior', 21)
p3 = Pessoa('Vanessa', 39)
