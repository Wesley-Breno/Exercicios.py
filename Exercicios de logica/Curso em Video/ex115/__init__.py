import json  # Importando o JSON para fazer mostrar/editar dados
from time import sleep  # Importando o sleep para fazer o programa 'dormir' antes de ir para o proximo passo


def menu():
    """
    Funcao que mostra um menu com tres opcoes...
    1 > Ver pessoas cadastradas no arquivos JSON
    2 > Cadastrar novas pessoas no arquivo
    3 > Sair do sistema (encerrar loop)
    :return: Retorna a opcao escolhida pelo usuario
    """
    while True:
        print('--' * 17)
        print('\t\tMENU PRINCIPAL')
        print('--' * 17)
        print('1 › Ver pessoas cadastradas\n'
              '2 › Cadastrar novas pessoas\n'
              '3 › Sair do sistema')
        print('--' * 17)

        try:
            opcao_escolhida = int(input('Sua opcao: '))

        except:
            print('\n\n\t\t[\033[;31mERRO\033[m]: Escolha uma das opcoes mostradas.\n\n')
            sleep(2)

        else:
            # Se for uma das opcoes mostradas
            if opcao_escolhida == 1 or opcao_escolhida == 2 or opcao_escolhida == 3:
                return opcao_escolhida

            else:
                print('\n\n\t\t[\033[;31mERRO\033[m]: Escolha uma das opcoes mostradas.\n')
                sleep(2)


def mostrar_pessoas(arquivo):
    """
    Funcao que recebe o nome de um arquivo JSON e mostra as pessoas que estao
    cadastradas nele. Caso o arquivo nao exista, aparecera um erro.
    :param arquivo: Nome do arquivo.
    :return: None
    """
    pessoas = dict()  # Dicionario que vai receber os dados do arquivo .json

    try:  # Tentando pegar os dados do arquivo .json
        with open(arquivo, 'r+') as file:
            pessoas.update(json.load(file))

    except:
        print('\n\n\t\t[\033[;31mERRO\033[m]: Nao foi possivel mostrar as pessoas.\n\n')

    else:
        print('--' * 17)
        print('\t\t\033[;1mTodas as pessoas\033[m')

        for chave, valor in pessoas.items():  # Mostrando o ID da pessoa, nome e idade.
            print(f'\nPessoa {chave}')
            for chaves, valores in valor.items():
                print('\t', chaves, f': {valores}')
        print('--' * 17)


def adicionar_pessoas(arquivo):
    """
    Funcao que recebe o nome de um arquivo JSON e adiciona um ID
    como dicionario e dentro o nome e idade de uma pessoa. Caso o
    arquivo nao exista, ele sera criado.
    :param arquivo: Nome do arquivo
    :return: None
    """
    pessoas = dict()  # Dicionario que vai receber os dados do arquivo .json
    contador = None  # Sera responsavel por adicionar o ID do novo usuario.

    try:  # Tentando pegar os dados do arquivo .json se ele existir.
        with open(arquivo, 'r+') as file:
            pessoas.update(json.load(file))

    except FileNotFoundError:  # Caso o arquivo .json nao exista, ele sera criado.
        with open(arquivo, 'x') as file:
            file.close()

        contador = 0  # Iniciando com o primeiro ID valido 0.

    finally:
        print('\n\n\t\t\033[;37mDigite [ 0 ] pra parar de adicionar\033[m\n')

        while True:  # Enquanto o usuario nao digitar zero.
            print()
            print('__' * 17)
            try:
                nome = str(input('Digite o nome da pessoa: '))
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
                    pessoas.update({contador: {'nome': nome, 'idade': idade}})

                else:
                    contador = 0
                    for key in pessoas.keys():  # Contando os IDs/Chaves dos clientes e somando mais um para adicionar.
                        contador += 1

                    contador += 1
                    pessoas.update({contador: {'nome': nome, 'idade': idade}})

    with open(arquivo, 'w+') as file:  # Reescrevendo o arquivo .json com o novo cliente.
        json.dump(pessoas, file, indent=4)
        file.close()
