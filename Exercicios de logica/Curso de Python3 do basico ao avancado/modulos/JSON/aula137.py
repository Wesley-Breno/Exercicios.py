"""
Programa que adiciona clientes e transforma os dados em JSON,
se o usuario quiser ver os clientes o programa deve converter
o arquivo JSON em Python e printar na tela.
"""

import json  # Importando o modulo json para usar os dados json


def adicionar_cliente():
    """
    Funcao que é responsavel por adicionar clientes e adiciona-los no arquivo .json.
    Se o arquivo .json nao existir, a funcao ira criar.

    :return: None
    """
    clientes = dict()  # Dicionario que vai receber os dados do arquivo .json
    contador = None  # Sera responsavel por adicionar o ID do novo usuario.

    try:  # Tentando pegar os dados do arquivo .json se ele existir.
        with open('clientes.json', 'r+') as file:
            clientes.update(json.load(file))

    except FileNotFoundError:  # Caso o arquivo .json nao exista, ele sera criado.
        with open('clientes.json', 'x') as file:
            file.close()

        contador = 0  # Iniciando com o primeiro ID valido 0.

    finally:
        print('\n\n\t\t\033[;37mDigite [ 0 ] pra parar de adicionar\033[m\n\n')

        while True:  # Enquanto o usuario nao digitar zero.
            print()
            print('__' * 16)
            try:
                nome = str(input('Digite o nome do cliente: '))
                if nome == '0':
                    break

                idade = int(input('Digite a idade: '))
                if idade == 0:
                    break

            except:
                print('\n\n\t\t[\033[;31mERRO\033[m]: Por favor, digite os dados corretamente.\n\n')

            else:
                if contador == 0:  # Se o arquivo foi criado agora, O id comecara valendo 1.
                    contador += 1
                    clientes.update({contador: {'nome': nome, 'idade': idade}})

                else:
                    contador = 0
                    for key in clientes.keys():  # Contando os IDs/Chaves dos clientes e somando mais um para adicionar.
                        contador += 1

                    contador += 1
                    clientes.update({contador: {'nome': nome, 'idade': idade}})

    with open('clientes.json', 'w+') as file:  # Reescrevendo o arquivo .json com o novo cliente.
        json.dump(clientes, file, indent=4)
        file.close()


def remover_cliente(id):
    """
    Funcao responsavel por remover cliente com base no ID informado.

    :param id: Identificacao do cliente, numero que esta antes dos dados dele
    Exemplo: 1: {cliente}, 2: {cliente}

    :return: None
    """
    clientes = dict()  # Dicionario que vai receber os dados do arquivo .json

    try:  # Lendo o arquivo para ver se ele existe.
        with open('clientes.json', 'r+') as file:
            file.close()

    except:
        print('\n\n\t\tNao existe nenhum cliente cadastrado.\n\n')

    else:
        with open('clientes.json', 'r+') as file:  # Colocando os dados do arquivo na variavel.
            clientes.update(json.load(file))

        try:  # Tentando apagar cliente com base no ID.
            clientes.pop(str(id))

        except KeyError:
            print('\n\n\t\t[\033[;31mERRO\033[m]: Verifique a chave do cliente informada.\n\n')

        else:  # Reescrevendo o arquivo com o cliente apagado.
            with open('clientes.json', 'w+') as file:
                json.dump(clientes, file, indent=4)


def mostrar_clientes():
    """
    Funcao responsavel por pegar os dados de clientes em um arquivo .json
    e mostrar na tela seu ID e seus dados.

    :return: None
    """
    clientes = dict()  # Dicionario que vai receber os dados do arquivo .json

    try:  # Tentando pegar os dados do arquivo .json
        with open('clientes.json', 'r+') as file:
            clientes.update(json.load(file))

    except:
        print('\n\n\t\t[\033[;31mERRO\033[m]: Nao foi possivel mostrar os clientes.\n\n')

    else:
        print('\n\n\t\t\033[;1mTodos os clientes\033[m\n\n')

        for chave, valor in clientes.items():
            print(f'\nCliente {chave}')
            for chaves, valores in valor.items():
                print('\t', chaves, f': {valores}')
