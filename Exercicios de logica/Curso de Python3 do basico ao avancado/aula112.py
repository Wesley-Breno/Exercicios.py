class Eletronico:    # Classe 'pai', onde tem o nome, e se o eletronico esta ligado ou nao.
    def __init__(self, nome):
        self.nome = nome
        self._ligado = False

    def ligar(self):
        if self._ligado:    # Se o eletronico ja estiver ligado.
            print('Ja esta ligado')
            return    # Usando o return para encerrar apartir daqui, caso o eletronico ja esteja ligado.

        self._ligado = True    # Se nao...
        print('Ligado')

    def desligar(self):
        if not self._ligado:    # Se o eletronico ja estiver desligado.
            print('Ja esta desligado')
            return

        # Else:
        self._ligado = False
        print('Desligado')


class LogMixin:    # Classe feita para fazer o arquivo .log.
    @staticmethod
    def write(msg):    # Escrevendo a mensagem que vai ficar na INFO/ERROR.
        with open('log.log', 'a+') as f:
            f.write(msg)
            f.write('\n')

    def log_info(self, msg):    # Vai guardar a informacao no arquivo .log.
        self.write(f'INFO: {msg}')

    def log_error(self, msg):    # Vai guardar o erro no arquivo .log.
        self.write(f'ERROR: {msg}')


class SmartPhone(Eletronico, LogMixin):    # Classe que sera um 'SmartPhone'.
    def __init__(self, nome):    # Nome do SmartPhone e se esta conectado a internet ou nao.
        super().__init__(nome)
        self._conectado = False

    def conectar(self):    # Fazer o SmartPhone se conectar a internet.
        if self._ligado:
            if self._conectado:    # Se o SmartPhone ja estiver conectado, mostra o erro e o adicionara no arquivo .log.
                erro = f'{self.nome} Ja esta com internet'
                print(erro)    # Mostrando o erro
                self.log_error(erro)    # Adicionando o erro no arquivo .log.
                return

            self._conectado = True    # Conectando a internet.
            info = f'{self.nome} Agora esta com internet'
            print(info)    # Mostrando a informacao.
            self.log_info(info)    # Adicionando a informacao no arquivo .log.
            return

        erro = f'{self.nome} ainda nao esta ligado.'    # Se o SmartPhone ainda nao estiver ligado.
        print(erro)
        self.log_error(erro)

    def desconectar(self):    # Fazer o SmartPhone se desconectar da internet.
        if self._ligado:
            if not self._conectado:    # Se o SmartPhone ja estiver desconectado.
                erro = f'{self.nome} Ja desligou a internet'
                print(erro)
                self.log_error(erro)
                return

            self._conectado = False    # Desconectando o SmartPhone da internet.
            info = f'{self.nome} Agora a internet esta desligada'
            print(info)
            self.log_info(info)
            return

        erro = f'{self.nome} ainda nao esta ligado.'    # Se o SmartPhone estiver desligado.
        print(erro)
        self.log_error(erro)


nokia = SmartPhone('Nokia-Tijolao')
nokia.desligar()
nokia.ligar()
nokia.conectar()
nokia.conectar()
nokia.desconectar()
nokia.desligar()
