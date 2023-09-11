"""
Faça um programa que mostre a tabuada de vários números,
um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.
"""

from time import sleep  # Modulo time com a funcao sleep para fazer o programa demorar a ser executado.

print('\n\n\n\t\033[;37m- Digite [ -1 ] para encerrar o programa -\033[m')

while True:  # Enquanto o usuario nao digitar um valor menor de 0.
    print('\n' * 4)
    print('__' * 22)
    try:
        numero = int(input('Digite o numero para ver sua tabuada: '))

    except:
        print('\n[\033[;31mERRO\033[m]: Por favor, insira um numero inteiro.\n')
        sleep(2)

    else:
        if numero < 0:  # Se o usuario escolheu encerrar.
            break

        print('__' * 22)

        for c in range(10):  # Multiplicando o valor por cada contagem do for.
            print(f'{numero} x {c + 1} = {numero * (c + 1)}')

        print('__' * 22)
        input('Pressione \033[;4menter\033[m para continuar.')

print('\n\n\t\t\033[;4mPrograma encerrado com sucesso\033[m\n\n')
