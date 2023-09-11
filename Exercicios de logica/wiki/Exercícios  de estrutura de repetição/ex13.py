"""
Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número.
Não utilize a função de potência da linguagem.
"""

while True:  # Enquanto o usuario nao informar os valores corretamente
    try:
        base = int(input('\nInforme o valor da base\nValor base: '))
        expoente = int(input('\nInforme o valor do expoente\nValor do expoente: '))
    except:
        print('\n\n\t\t[\033[;31mERRO\033[m]: Por favor, insira os valores corretamente.\n\n')
    else:
        break

resultado = 1
for c in range(expoente):  # Fazendo a potencia
    resultado *= base

print(f'\n\n\t\t{base}^({expoente}) = {resultado}\n\n')  # resultado
