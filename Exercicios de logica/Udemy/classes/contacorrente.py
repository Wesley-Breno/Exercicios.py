from conta import Conta


class ContaCorrente(Conta):  # Classe filha herdando de classe pai.
    def __init__(self, agencia, conta, saldo, limite=100):  # Colocando os atributos da classe pai e fazendo seu propio atributo.
        super().__init__(agencia, conta, saldo)  # Pegando os valores.
        self._limite = limite

    def sacar(self, valor):  # O valor so ira ser sacado se o valor for menor ou igual ao limite e o saldo somados.
        if isinstance(valor, (int, float)):
            if (self._limite + self._saldo) >= valor:
                self._saldo -= valor
                print(f'\nSaque de R\033[;32m$\033[m{valor} realizado com \033[;32msucesso\033[m')
                return

            print(f'\nSaldo \033[;31minsuficiente\033[m\nLimite de saque: {self._limite}')
            return

        print('\n\033[;31mERRO\033[m: O valor a ser sacado deve ser numerico\n')
