"""
Classe Conta Corrente:
Crie uma classe para implementar uma conta corrente. A classe deve possuir os seguintes atributos: número da conta,
nome do correntista e saldo. Os métodos são os seguintes: alterarNome, depósito e saque; No construtor, saldo é
opcional, com valor default zero e os demais atributos são obrigatórios.
"""


class ContaCorrente:
    def __init__(self, numero_conta: int, nome_correntista: str, saldo: float = 0):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo

    def alterar_nome(self, novo_nome: str):
        print(f'Nome antigo: {self.nome_correntista}')
        print(f'Nome atual: {novo_nome}')
        print('O nome do correntista foi alterado com sucesso!')
        self.nome_correntista = novo_nome

    def deposito(self, depositar: float):
        self.saldo += depositar
        print(f'Deposito de R${depositar:.2f} feito com sucesso.')

    def saque(self, sacar: float):
        if sacar <= self.saldo:
            self.saldo -= sacar
            print(f'Saque de R${sacar:.2f} feito com sucesso.')
        else:
            print(f'Voce nao tem dinheiro suficiente para sacar R${sacar:.2f}')


if __name__ == '__main__':
    conta1 = ContaCorrente(123, 'Wesley')
    conta1.alterar_nome('Werlindo')
    conta1.deposito(7.50)
    conta1.saque(10)
    conta1.saque(7.50)
    conta1.saque(1)
    