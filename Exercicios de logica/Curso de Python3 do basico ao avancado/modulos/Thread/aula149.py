from threading import Thread  # Classe responsavel por fazer o thread
from threading import Lock  # Classe que sera usada para fazer apenas um cliente usar a funcao 'comprar' por vez
from time import sleep  # Funcao que fara o programa esperar para executar o proximo comando


class Ingressos:
    def __init__(self, estoque):
        self.estoque = estoque  # Quantidade de ingressos disponiveis para vender
        self.lock = Lock()  # Colocando a classe Lock() em uma variavel para poder usa-lo

    def comprar(self, quantidade):
        self.lock.acquire()  # 'Fechando' a funcao para apenas um cliente usar de cada vez

        if self.estoque < quantidade:  # Se nao tiver ingressos suficientes para a venda
            print(f'\nNao é possivel realizar a compra de {quantidade} ingressos\n'
                  f'temos \033[;31m{self.estoque}\033[m ingressos no nosso estoque.')
            self.lock.release()  # 'Reabrindo' a funcao para o proximo cliente/thread
            return

        sleep(1)

        self.estoque -= quantidade
        print(f'\nVoce acaba de comprar \033[;32m{quantidade}\033[m ingressos\n'
              f'Temos {self.estoque} ingressos em nosso estoque.')
        self.lock.release()  # 'Reabrindo' a funcao para o proximo cliente/thread


cinema = Ingressos(20)

threads = []  # Lista onde ficara cada thread que sera executado
for c in range(20):  # Fazendo 20 threads com quantidades diferentes de ingressos que sera pedido na classe
    t = Thread(target=cinema.comprar, args=(c, ))
    threads.append(t)

for t in threads:  # Iniciando cada thread
    t.start()

executando = True
while executando:  # Enquanto tiver threads sendo executados
    executando = False

    for t in threads:
        if t.is_alive():  # Se tiver um thread executando ainda
            executando = True
            break

print('Ola')  # Printar na tela assim que todos os threads forem executados
