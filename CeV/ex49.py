# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher,
# só que agora utilizando um laço for.

from functions import titulo, press_enter, pular, erro, programa_encerrado    # Funcoes que criei.
from time import sleep    # Funcao importada para fazer o programa demorar alguns segundos para continuar.

titulo('Tabuada 2.0')
press_enter('para escolher o numero.')

while True:    # Enquanto o usuario nao digitar o numero 0.
    try:
        pular(3)
        print(f'\033[;37m{"Digite [ 0 ] para encerrar.":^45}\033[m')
        print('__' * 24)
        numero = int(input('Digite o numero para mostrar sua tabuada...\nNumero: '))
    except:
        erro('Por favor\nDigite um valor valido.')
    else:
        if numero == 0:    # Se o usuario digitar zero, o programa encerra.
            break

        print('\033[;1m')    # Colocando todas os caracteres a seguir em negrito.
        print('__' * 24)
        print('\n\t| SOMA |\n')
        for c in range(1, 11):    # Soma
            print(f'{numero} + {c} = {numero + c}')
        sleep(1)    # Fazendo o programa demorar para continuar por 1 segundo.

        print('__' * 24)
        print('\n\tSUBTRACAO\n')
        for c in range(1, 11):    # Subtracao
            print(f'{numero} - {c} = {numero - c}')
        sleep(1)

        print('__' * 24)
        print('\n\tDIVISAO\n')
        for c in range(1, 11):  # Divisao
            print(f'{numero} / {c} = {numero / c}')
        sleep(1)

        print('__' * 24)
        print('\n\tMULTIPLICACAO\n')
        for c in range(1, 11):    # Multiplicacao
            print(f'{numero} x {c} = {c * numero}')
        print('\033[m')
        sleep(1)

        print('__' * 24)
        press_enter('para escolher outro numero.')

programa_encerrado()    # Mensagem de despedida para o usuario.
