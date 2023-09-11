class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    @property
    def nome(self):
        return self.__nome

    def ano_nascimento(self):
        ano = self.ano_atual - self.__idade
        return ano


lista_pessoas = []
for c in range(4):
    print()
    lista_pessoas.append(Pessoa(str(input(f'Digite o nome da {c + 1}° pessoa: ')),
                                int(input('Digite a idade: '))))

print(f'\n\n\033[;1m{"Listagem de pessoas":^45}\033[m')
for p in lista_pessoas:
    print()
    print(f'Nome: \t{p.nome.title()}\nA. nascimeto: \t{p.ano_nascimento()}')
