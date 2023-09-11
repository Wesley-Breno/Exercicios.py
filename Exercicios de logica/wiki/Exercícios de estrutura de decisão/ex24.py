"""
Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:

par ou ímpar;
positivo ou negativo;
inteiro ou decimal.
"""

numeros = []
while True:  # Enquanto o usuario nao digitar os valores corretamente
    try:
        for c in range(2):
            numeros.append(float(input(f'Informe o {c + 1}º valor: ')))

    except:
        print('\n\nERRO\nInforme os valores corretamente.\n')
        numeros = []

    else:
        break

while True:  # Enquanto o usuario nao escolher uma das operacoes
    try:
        print('----' * 15)
        operacao_escolhida = int(input("""Digite a operacao escolhida conforme o numero ao lado.

[ 1 ] - Par ou impar
[ 2 ] - Positivo ou negativo
[ 3 ] - Inteiro ou decimal
[ 4 ] - Encerrar programa

Operacao escolhida: """))

    except:
        print('\n\nERRO\nDigite uma das operacoes que foram mostradas.\n')
        input('Pressione ENTER para continuar.')

    else:
        if operacao_escolhida == 4:  # Se o usuario decidiu encerrar o programa
            break

        if operacao_escolhida != 1 and operacao_escolhida != 2 and operacao_escolhida != 3:  # Se a operacao escolhida nao foi nenhuma das que foram mostradas
            print('\n\nERRO\nDigite uma das operacoes que foram mostradas.\n')

        else:
            for num in numeros:
                print(f'\n\n\t\tNumero {num}\n')

                print(f'O numero {num} é um numero ', end='')

                if operacao_escolhida == 1:
                    if num == 0:
                        print('neutro')

                    elif num % 2 == 0:
                        print('par')

                    else:
                        print('impar')

                elif operacao_escolhida == 2:
                    if num == 0:
                        print('neutro')

                    elif int(num) > 0:
                        print('positivo')

                    else:
                        print('negativo')

                elif operacao_escolhida == 3:
                    num_str = str(num).split('.')  # Separando o numero inteiro do decimal.

                    if num == 0:
                        print('neutro')

                    elif int(num_str[1]) > 0:  # Se o numero decimal for maior que zero
                        print('decimal')

                    else:
                        print('inteiro')

                print('--' * 18)

        input('Pressione ENTER para continuar.')
