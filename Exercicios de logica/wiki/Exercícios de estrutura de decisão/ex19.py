"""
Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do
mesmo. Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:

326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades
"""

numero = int(input('Digite um numero aleatorio que seja menor que 1000\nNumero: '))

if 1000 > numero > 0:  # Se o numero estiver entre 1 e 999.

    numeros_separados = str(numero)  # Transformando em string para contar os caracteres.

    print(f'\n{numero} = ', end='')

    if len(numeros_separados) == 3:  # Se tiver centena
        print(f'{numeros_separados[0]} centena', end='')

        if int(numeros_separados[0]) > 1:  # Se tiver mais de uma centena.
            print(f's, ', end='')
        else:
            print(f', ', end='')

        print(f'{numeros_separados[1]} dezena', end='')

        if int(numeros_separados[1]) > 1:  # Se tiver mais de uma dezena.
            print('s e ', end='')
        else:
            print(' e ', end='')

        print(f'{numeros_separados[2]} unidade', end='')  # Se tiver mais de uma unidade.

        if int(numeros_separados[2]) > 1:
            print('s')
        else:
            ...

    elif len(numeros_separados) == 2:  # Se tiver dezena
        print(f'{numeros_separados[0]} dezena', end='')

        if int(numeros_separados[0]) > 1:
            print('s e ', end='')
        else:
            print(' e ', end='')

        print(f'{numeros_separados[1]} unidade', end='')

        if int(numeros_separados[1]) > 1:
            print('s')
        else:
            ...

    else:  # Se tiver apenas unidade
        print(f'{numeros_separados[0]} unidade', end='')

        if int(numeros_separados[0]) > 1:
            print('s')
        else:
            ...

else:
    print('\n\n\t\tPor favor, digite um numero aleatorio que seja menor que 1000.\n')
