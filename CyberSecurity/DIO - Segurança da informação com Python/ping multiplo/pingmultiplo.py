"""
Funcao que recebera um arquivo em txt com o endereco de cada host para fazer o teste.
"""

import os  # Importando modulo OS para executar o comando de teste
from time import sleep  # Importando a funcao sleep para fazer o programar 'esperar'


def verification(nome_arquivo: str, qtd_pacotes=1) -> None:
    """
    Funcao que recebera um arquivo em txt com os enderecos de cada host para fazer o teste.
    :param nome_arquivo: Nome/caminho do arquivo txt
    :param qtd_pacotes: Quantidade de pacotes que deseja enviar para testes
    :return: None
    """

    hosts = []

    with open(nome_arquivo) as file:
        for linha in file:
            hosts.append(linha.replace('\n', ''))  # Colocando cada host em uma lista

    for host in hosts:
        if qtd_pacotes == 1:  # Se o usuario nao informou a quantidade de pacotes que serao enviados
            print(os.system(f'ping -n 1 {host}'))  # Executando teste

        else:
            print(os.system(f'ping -n {qtd_pacotes} {host}'))

        sleep(3)
        print()


if __name__ == "__main__":
    verification('hosts.txt')
