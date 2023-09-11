"""
Aprimore a classe do exercício anterior para adicionar o método aumentarSalario (porcentualDeAumento) que aumente o
salário do funcionário em uma certa porcentagem.

Exemplo de uso:
  harry=funcionário("Harry",25000)
  harry.aumentarSalario(10)
"""


class Funcionario:
    def __init__(self, nome: str, salario: float):
        self.nome = nome
        self.salario = salario

    def aumentar_salario(self, porcentagem: float):
        self.salario = self.salario + (self.salario * porcentagem / 100)

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
    print(f'Salario atual: R$ {salario_funcionario1:.2f}')
    funcionario1.aumentar_salario(10)
    salario_funcionario1 = funcionario1.get_salario()
    print(f'Salario com aumento de 10%: R$ {salario_funcionario1:.2f}')
