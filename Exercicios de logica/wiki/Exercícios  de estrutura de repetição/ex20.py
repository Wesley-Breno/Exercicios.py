"""
Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial
a números inteiros positivos e menores que 16.
"""

print('\n\t\t\033[;37mDigite [ 0 ] para encerrar o programa\033[m\n\n')

while True:  # Enquanto o usuario nao digitar 0 para encerrar o programa
    try:
        print('__' * 25)
        numero = int(input('Informe um valor entre 1 e 16 para ver sua fatorial\nValor:  '))

    except:
        print('\n\n\t\t[\033[;31mERRO\033[m]: Por favor, insira um valor entre 1 e 16.\n\n')

    else:
        if numero == 0:  # Se o usuario quis encerrar o programa
            break

        if numero > 0 and numero < 17:  # Se o usuario informou um valor entre 1 e 16
            print(f'\n\n\t\tFatorial de {numero}\n')

            fatorial = 1

            for c in range(numero, 0, -1):  # Fazendo calculo da fatorial do numero informado
                fatorial *= c

                if c == 1:
                    print(c, end=' = ')

                else:
                    print(c, end=' x ')

            print(fatorial)
            input('\nPressione ENTER para continuar.')

        else:
            print('\n\n\t\t[\033[;31mERRO\033[m]: Por favor, insira um valor entre 1 e 16.\n\n')
