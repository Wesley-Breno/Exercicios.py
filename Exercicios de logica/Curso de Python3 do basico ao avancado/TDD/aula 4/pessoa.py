import requests


class Pessoa:
    """
    Classe que criada para fazer testes.
    """
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
        self.dados_obtidos = False

    def obter_todos_os_dados(self):
        resposta = requests.get('https://wiki.python.org.br/ListaDeExercicios')

        if resposta.ok:
            self.dados_obtidos = True
            return 'CONECTADO'

        else:
            self.dados_obtidos = False
            return 'ERRO 404'
