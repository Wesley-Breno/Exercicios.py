from conta import Conta


class ContaPoupanca(Conta):  # Classe filha herdando da classe pai.
    def __init__(self, agencia, conta, saldo):  # Pegando os atributos da classe pai
        super().__init__(agencia, conta, saldo)  # Pegando os valores

    def sacar(self, valor):  # Vai sacar o dinheiro e nao precisa de limite, apenas o saldo da conta.
        if isinstance(valor, (int, float)):
            if valor <= self._saldo:
                self._saldo -= valor
                print(f'\nSaque de R\033[;32m$\033[m{valor} realizado com \033[;32msucesso\033[m')
                return

            print('\nSaldo \033[;31minsuficiente\033[m\n')
            return

        print('\n\033[;31mERRO\033[m: O valor a ser sacado deve ser numerico\n')
