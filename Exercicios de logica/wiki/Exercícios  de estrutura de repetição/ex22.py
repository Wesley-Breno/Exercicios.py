"""
Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é
divisível.
"""

while True:  # Enquanto o usuario nao informar um numero valido
    try:
        numero = int(input('\nInforme um valor para saber se é um numero primo ou nao\nValor informado: '))
    except:
        print('\n\n\t\t[\033[;31mERRO\033[m]: Por favor, informe um valor valido\n\n')
    else:
        break

cont = 0  # Contador para saber se o numero foi divisel apenas 2 vezes
numeros_divisiveis = []  # Numeros que sao divisiveis caso o numero nao seja primo

for c in range(1, numero + 1):  # Dividindo por todos os numeros ate o valor informado
    if numero % c == 0:
        cont += 1
        numeros_divisiveis.append(c)

if cont == 2:  # Se o numero foi divisivel por 1 e por ele mesmo
    print(f'\n\n\t\tO numero {numero} é um valor \033[;32mprimo\033[m\n')
else:
    print(f'\n\n\t\tO numero {numero} \033[;31mnão\033[m é um valor primo\n'
          f'Numeros que são divisiveis por {numero}: {numeros_divisiveis}')
