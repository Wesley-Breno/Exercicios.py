class LogMixin:  # Classe mixin que cria um arq.log
    @staticmethod
    def escrever(msg):
        with open('arq.log', 'a+') as file:  # Metodo que vai escrever no arquivo
            file.write(msg)
            file.write('\n')

    def log_info(self, msg):  # Se for uma informacao
        self.escrever(f'INFO: {msg}')

    def log_erro(self, msg):  # Se for um erro
        self.escrever(f'ERRO: {msg}')
