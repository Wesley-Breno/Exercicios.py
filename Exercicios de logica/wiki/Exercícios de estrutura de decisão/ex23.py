"""
Faça um Programa que peça um número e informe se o número é inteiro ou decimal.
"""

while True:
    try:
        numero = float(input('Digite um numero: '))

    except:
        print('\n\nERRO\nDigite um valor novamente.')

    else:
        numero_str = str(numero).split('.')  # Separando o numero inteiro do decimal.

        print(f'\n\n\t\tO valor {numero} é um valor ', end='')

        if int(numero_str[1]) > 0:  # Se o numero decimal for maior que zero
            print('decimal')
        else:
            print('inteiro')

        break
