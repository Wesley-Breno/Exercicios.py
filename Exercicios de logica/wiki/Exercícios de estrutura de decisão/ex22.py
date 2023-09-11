"""
Faça um Programa que peça um número inteiro e determine se ele é par ou impar.
"""

while True:  # Enquanto o usuario nao digitar um numero inteiro
    try:
        numero = int(input('Digite um numero inteiro: '))

    except:
        print('\n\nERRO\nDigite um numero inteiro novamente.\n')

    else:  # Se o usuario digitou um numero inteiro
        print(f'\n\n\t\tO numero {numero} é ', end='')

        if numero % 2 == 0:  # Se o usuario digitou um numero par
            print(f'par')
        else:
            print('impar')

        break
