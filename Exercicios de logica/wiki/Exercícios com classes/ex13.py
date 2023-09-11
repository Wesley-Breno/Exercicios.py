"""
Classe Funcionário: Implemente a classe Funcionário. Um empregado tem um nome (um string) e um salário(um double).
Escreva um construtor com dois parâmetros (nome e salário) e métodos para devolver nome e salário. Escreva um pequeno
programa que teste sua classe.
"""


class Funcionario:
    def __init__(self, nome: str, salario: float):
        self.nome = nome
        self.salario = salario

    def get_nome(self):
        return self.nome

    def get_salario(self):
        return self.salario


if __name__ == '__main__':
    funcionario1 = Funcionario('Cesar', 2500)
    nome_funcionario1 = funcionario1.get_nome()
    salario_funcionario1 = funcionario1.get_salario()
    print(f"""
Nome do funcionario: {nome_funcionario1}
Salario do funcionario: R$ {salario_funcionario1:.2f}""")
    