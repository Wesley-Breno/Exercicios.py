from abc import ABC, abstractmethod  # Modulo importado para usar o @abstractmethod.


class Conta(ABC):  # Classe pai
    def __init__(self, agencia, conta, saldo):
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo

    @property  # Retornando os atributos para eles serem usados fora da classe.
    def agencia(self):
        return self._agencia

    @property
    def conta(self):
        return self._conta

    @property
    def saldo(self):
        return self._saldo

    @abstractmethod  # Metodo abstrato, que vai reagir de uma forma em diferentes classes filhas.
    def sacar(self, valor):
        pass

    def depositar(self, valor):  # Deposita um valor numerico na conta.
        if not isinstance(valor, (int, float)):
            print('\n\033[;31mERRO\033[m: O valor a ser depositado deve ser numerico\n')
            return

        self._saldo += valor
        print(f'\nDeposito de R\033[;32m$\033[m{valor} realizado com \033[;32msucesso\033[m\n')

    def informacoes(self):  # Mostra as informações da conta.
        print(f"""\n      INFORMACOES
        
    Agencia: {self._agencia}
    Conta: {self._conta}
    Saldo: {self._saldo}""")
