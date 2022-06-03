# Aqui fica algumas funcoes que irei usar em alguns exercicios. :)

from time import sleep

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
        print('__' * 16)
        print('[\033[1;31mERROR\033[m]\nTente novamente.')
        print('__' * 16)
        input('\nPressione \033[1;4menter\033[m para continuar.')
        pular(2)
    else:
        pular(2)
        print('__' * 16)
        print(f'[\033[1;31mERROR\033[m]\n\n{msg}')
        print('__' * 16)
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


def encerrar(msg=0):
    """
    Funcao que faz uma pergunta ao usuario para saber se ele
    quer encerrar o programa ou nao, usando apenas uma letra
    para considerar o SIM e o NAO.

    :param msg: Parametro para trocar a palavra 'programa' por outra.
    EX: 'Deseja encerrar o JOGO?'

    :return: retorna 1 se o usuario deseja encerrar,
    retorna 0 se ele nao quiser encerrar.
    """
    if msg == 0:
        while True:
            try:
                pular(3)
                print('__' * 15)
                print('Deseja encerrar o programa?\n[\033[;1mS\033[m = Sim] - [\033[;1mN\033[m = Nao]')
                pergunta = str(input('-> ')).upper()[0]
                print('__' * 15)
            except:
                erro('Informe um dado valido.')
            else:
                if pergunta == 'S' or pergunta == 'N':
                    if pergunta == 'S':
                        return 1
                    else:
                        return 0
                else:
                    erro('Informe um dado valido.')
    else:
        while True:
            try:
                pular(3)
                print('__' * 15)
                print(f'Deseja encerrar o {msg}?\n[\033[;1mS\033[m = Sim] - [\033[;1mN\033[m = Nao]')
                pergunta = str(input('-> ')).upper()[0]
                print('__' * 15)
            except:
                erro('Informe um dado valido.')
            else:
                if pergunta == 'S' or pergunta == 'N':
                    if pergunta == 'S':
                        return 1
                    else:
                        return 0
                else:
                    erro('Informe um dado valido.')


def programa_encerrado(string='Programa'):
    """
    Funcao para mostrar uma mensagem de adeus para o usuario
    quando o programa/jogo for encerrado.

    :param string: Variavel para trocar a palavra "Programa" por outra como "jogo" e etc.
    :return: Null
    """
    pular(3)
    print(f'{f"{string} encerrado com sucesso.":^45}')
    print(f'{"Ate logo ♥":^45}')
    pular(3)


def linha(tipo='__', vezes=12):
    """
    Funcao que vai escrever na tela, por padrao ou escolha do programador, uma linha na tela
    com o tamanho que ele quiser.

    :param tipo: Parametro onde fica o tipo de string que sera repetida.
    :param vezes: Parametro onde fica quantas vezes vai se repetir.
    :return:
    """
    print(f'{tipo}' * vezes)
