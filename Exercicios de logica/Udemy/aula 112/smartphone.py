from eletronico import Eletronico
from log import LogMixin


class SmartPhone(Eletronico, LogMixin):  # Classe com herança multipla
    def __init__(self, nome):
        Eletronico.__init__(self, nome)  # Pegando todos os atributos/metodos de Eletronico
        self._conectado = False

    def conectar(self):
        if not self._ligado:
            erro = f'Incapaz de conectar, {self._nome} esta desligado.'
            print(erro)
            self.log_erro(erro)  # Adicionando o erro ocorrido no arquivo.log
            return

        if not self._conectado:
            self._conectado = True
            info = f'{self._nome} conectado a internet.'
            print(info)
            self.log_info(info)  # Adicionando a informação ocorrida no arquivo.log
            return

        erro = f'{self._nome} ja esta conectado a internet.'
        print(erro)
        self.log_erro(erro)

    def desconect(self):
        if not self._ligado:
            erro = f'Incapaz de desconectar, {self._nome} esta desligado.'
            print(erro)
            self.log_erro(erro)
            return

        if self._conectado:
            self._conectado = False
            info = f'{self._nome} desconectado da internet.'
            print(info)
            self.log_info(info)
            return

        erro = f'{self._nome} ja esta desconectado da internet.'
        print(erro)
        self.log_erro(erro)
