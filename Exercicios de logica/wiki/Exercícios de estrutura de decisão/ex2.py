"""
Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
"""

while True:  # Enquanto o usuario nao digitar um valor inteiro.
    try:
        valor = int(input('Digite um valor: '))

    except:
        print('\n\t\t\033[;31mDigite um valor inteiro\033[m\n')

    else:
        break

print('\n\n\t\t', end='')
if valor == 0:  # Se for igual a zero.
    print(f'O valor {valor} é um valor \033[;37mneutro\033[m.')

elif valor > 0:  # Se for positivo
    print(f'O valor {valor} é \033[;32mpositivo\033[m.')

else:  # Se for negativo
    print(f'O valor {valor} é \033[;31mnegativo\033[m.')
