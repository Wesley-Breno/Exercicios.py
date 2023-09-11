class Arquivo:  # Criando o gerenciador de contexto
    def __init__(self, arq, mod):
        print('Abrindo arquivo...')
        self.arquivo = open(arq, mod)  # Abrindo o arquivo com o nome e pra que sera aberto

    def __enter__(self):  # Execuntando o algoritmo do with.
        print('Retornando o arquivo...')
        return self.arquivo

    def __exit__(self, exc_type, exc_val, exc_tb):  # Fechando arquivo.
        print('Fechando arquivo...')
        self.arquivo.close()
        return True


with Arquivo('oioi.txt', 'a+') as file:  # Abrindo arquivo, escrevendo no arquivo e fechando arquivo.
    file.write('oi :)\n')
    file.write('turu bo?')
