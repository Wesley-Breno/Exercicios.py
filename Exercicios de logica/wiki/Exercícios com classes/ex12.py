"""
Classe Conta de Investimento: Faça uma classe contaInvestimento que seja semelhante a classe contaBancaria, com a
diferença de que se adicione um atributo taxaJuros. Forneça um construtor que configure tanto o saldo inicial como a
taxa de juros. Forneça um método adicioneJuros (sem parâmetro explícito) que adicione juros à conta. Escreva um programa
que construa uma poupança com um saldo inicial de R$1000,00 e uma taxa de juros de 10%. Depois aplique o método
adicioneJuros() cinco vezes e imprime o saldo resultante.
"""


class ContaInvestimento:
    def __init__(self, saldo, juros):
        self.taxa_juros = juros
        self.saldo = saldo

    def adicionar_juros(self):
        self.saldo = self.saldo + (self.saldo * self.taxa_juros / 100)  # Adicionando a porcentagem dos juros

    def imprimir_saldo(self):
        print(f'O seu saldo é de: {self.saldo:.2f}')


if __name__ == '__main__':
    conta1 = ContaInvestimento(1000, 10)
    [conta1.adicionar_juros() for _ in range(5)]
    conta1.imprimir_saldo()
