# Aqui fica algumas funcoes que irei usar em alguns exercicios. :)

def pular(n=1):
    """
    Funcao que sera usada para pular linhas sem o uso exagerado
    de prints ou estruturas de repeticao.
    :param n: Serve para colocar a quantidade de linhas que serao puladas.
    :return: None
    """
    for c in range(0, n):
        print()


def erro(msg=''):
    """
    Função para mostrar uma mensagem de erro.
    :param msg: Usada para mostrar uma mensagem de erro especifica.
    :return: None
    """
    if len(msg) <= 0:
        pular(2)
        print('__' * 14)
        print('[\033[1;31mERROR\033[m]\nTente novamente.')
        print('__' * 14)
        input('\nPressione \033[1;4menter\033[m para continuar.')
        pular(2)
    else:
        pular(2)
        print('__' * 14)
        print(f'[\033[1;31mERROR\033[m]\n{msg}')
        print('__' * 14)
        input('\nPressione \033[1;4menter\033[m para continuar.')
        pular(2)


def press_enter(msg=0):
    """
    Vai fazer uma pausa na execuçao do codigo
    e pedir para o usuario pressionar enter para continuar.
    :param msg: Sera uma mensagem personalizada.
    :return: None
    """
    if msg == 0:
        input('pressione \033[;1mEnter\033[m para continuar.')
    else:
        input(f'pressione \033[;1mEnter\033[m {msg}')


def titulo(msg):
    """
    Função para criar um titulo.
    :param msg: String que sera o titulo.
    :return: None
    """
    pular(2)
    print('-=-' * 15)
    print(f'\033[;1m{msg:^45}\033[m')
    print('-=-' * 15)
    pular(2)

