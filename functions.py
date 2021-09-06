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
