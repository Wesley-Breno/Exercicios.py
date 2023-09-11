from abc import ABC, abstractmethod  # Importando o abstractmethod para fazer um metodo abstrato.


class Banco:
    """
    Classe banco onde sera responsavel por adicionar usuarios no banco e
    mostrar informacoes
    """
    contas = []  # Numero da conta de cada usuario
    clientes = []  # Nome de cada cliente
    agencia = 111  # Agencia do banco

    def mostrar_info(self, pessoa):
        """
        Função responsavel por mostrar informacoes do usuario desejado.
        :param pessoa: Usuario que sera mostrado as informacoes
        :return: None
        """
        if pessoa.nome in self.clientes:  # Se o usuario estiver cadastrado no banco.
            print('\n\t\t', pessoa.nome.title(), '\n')
            print('Agencia: ', pessoa.conta.agencia)
            print('N. conta: ', pessoa.conta.numero_conta)
            print('Saldo:', pessoa.conta.saldo)
        else:
            print('Houve um erro ao mostrar informacoes do cliente, possivel erro:\n'
                  '* Cliente nao foi registrado\n')

    def adicionar_conta(self, pessoa):
        """
        Funcao responsavel por adicionar o usuario no banco, o numero da conta do usuario e seu
        nome ficarao salvos em uma lista.
        :param pessoa: Usuario que sera adicionado ao banco.
        :return: None
        """
        # Se o usuario for maior de idade, a agencia for igual a do banco e ele ainda nao tiver sido cadastrado.
        if pessoa.idade >= 18 and pessoa.conta.agencia == Banco.agencia and pessoa.conta.numero_conta not in Banco.contas:
            self.contas.append(pessoa.conta.numero_conta)
            self.clientes.append(pessoa.nome)
            print(f'{pessoa.nome.title()} \033[;32mregistrado\033[m.')

        else:
            print('Houve um erro ao executar o cadastro, possiveis erros:\n'
                  '* Usuario menor de 18 anos.\n'
                  '* Agencia incompativel com a do banco.\n'
                  '* Conta ja criada.')


class Conta(ABC):
    """
    Classe conta que sera o 'pai' das classes ContaPoupanca e ContaCorrente.
    A classe é responsavel por fazer o metodo abstrato sacar, e o metodo depositar.
    """
    def __init__(self, agencia, numero_conta, saldo):
        """
        Dados da conta do usuario.
        :param agencia: Numero da agencia
        :param numero_conta: Numero da conta, como se fosse uma identificacao
        :param saldo: Saldo/dinheiro que o usuario tem
        """
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f'Deposito: \033[;32m+\033[m{valor}')

    @abstractmethod
    def sacar(self, valor):
        ...


class ContaCorrente(Conta):
    """
    Classe ContaCorrente, responsavel apenas para sacar como se fosse um
    cartao de credito, o usuario tem um limite para sacar, caso nao tenha saldo na conta.
    """
    def sacar(self, valor, limite=100):
        """
        Funçao abstrata para sacar dinheiro como se fosse um cartao
        de credito.
        :param valor: Valor que vai ser sacado
        :param limite: Limite que o usuario tem para sacar
        :return: None
        """
        # Se a agencia do usuario for igual a do banco, se a conta estiver cadastrada no banco.
        if self.agencia == Banco.agencia and self.numero_conta in Banco.contas:
            if valor <= (self.saldo + limite):  # Se o valor que o usuario quer sacar for menor/igual ao saldo + limite
                self.saldo -= valor
                print(f'Saque: \033[;31m-\033[m{valor}')

            else:
                print('Impossivel sacar, saldo insuficiente.'
                      f'\nSeu limite de credito é de: {limite}')

        else:
            print('\nHouve um erro ao executar o saque, possiveis erros:\n'
                  '* Agencia incompativel com a do banco.\n'
                  '* Conta nao registrada no banco.')


class ContaPoupanca(Conta):
    """
    Classe ContaPoupanca, responsavel apenas por sacar normalmente.
    """
    def sacar(self, valor):
        """
        Função que sera resonsavel por sacar o dinheiro
        :param valor: Valor que vai ser sacado
        :return: None
        """
        # Se a agencia do usuario for igual a do banco, se a conta estiver cadastrada no banco.
        if self.agencia == Banco.agencia and self.numero_conta in Banco.contas:
            if valor <= self.saldo:  # Se o valor que o usuario quer sacar for menor ou igual ao saldo da sua conta.
                self.saldo -= valor
                print(f'Saque: \033[;31m-\033[m{valor}')

            else:
                print('Impossivel sacar, saldo insuficiente.')

        else:
            print('\nHouve um erro ao executar o saque, possiveis erros:\n'
                  '* Agencia incompativel com a do banco.\n'
                  '* Conta nao registrada no banco.')
