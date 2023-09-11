class Pessoa:  # Classe pai
    def __init__(self, nome, idade):  # Atributos da classe pai
        self.nome = nome
        self.idade = idade

    def falar(self):
        print(f'{self.nome} esta falando...')


class ClienteVip(Pessoa):  # Classe filha
    def __init__(self, nome, idade, id):  # Todos os atributos que estao na classe
        Pessoa.__init__(self, nome, idade)  # Pegando os valores da classe pai
        self.id = id  # Atributo que foi criado so para a classe ClienteVip


c = ClienteVip('werlindo', 18, 420)
print(f'ID cliente vip: {c.id}')
