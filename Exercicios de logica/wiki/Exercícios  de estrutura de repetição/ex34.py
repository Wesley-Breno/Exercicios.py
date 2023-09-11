"""
Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. Um número primo é aquele
que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número inteiro e determine se ele é ou não
um número primo.
"""

cont = 0  # Contador que ira contar quantas vezes o numero foi divisivel

while True:  # Enquanto o usuario nao informar um valor inteiro valido
    try:
        numero = int(input('\nInforme um numero inteiro: '))
    except:
        print('\n\n\t\t[\033[;31mERRO\033[m]: Informe um valor inteiro conrretamente.\n\n')
    else:
        break

for c in range(1, numero + 1):  # Indo do 1 ate o numero informado e contando quantas vezes ele foi divisivel
    if numero % c == 0:
        cont += 1

if cont == 2:  # Se o numero foi divisivel apenas 2 vezes
    print(f'\nO valor {numero} é um numero primo')
else:
    print(f'\nO valor {numero} não é um numero primo')
