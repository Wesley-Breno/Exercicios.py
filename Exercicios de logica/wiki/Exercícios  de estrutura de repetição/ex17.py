"""
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
"""

while True:  # Enquanto o usuario nao informar o numero
    try:
        numero = int(input('\nInforme o numero que deseja ver sua fatorial\nNumero: '))
    except:
        print('\n\n\t\t[\033[;31mERRO\033[m]: Por favor, informe um numero inteiro novamente.\n\n')
    else:
        break

fatorial = 1  # Variavel que tera o resultado da fatorial

print(f'\n\n\t\tFatorial de {numero}\n')

print(f'{numero}!=', end='')
for c in range(numero, 0, -1):  # Fazendo calculo da fatorial
    fatorial *= c

    if c == 1:
        print(f'{c}=', end='')
    else:
        print(c, end='.')

print(fatorial)
