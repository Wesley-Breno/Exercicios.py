"""
Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.
Exemplo:
  12376489
  => 98467321
"""

while True:  # Enquanto o usuario nao informar o valor numerico corretamente
    try:
        print()
        print('--' * 25)
        numero = int(input('Informe um valor numerico para ver ele invertido\nValor: '))

    except ValueError:
        print('\n\n\t\t[\033[;31mERRO\033[m]: Por favor, informe o valor numerico corretamente.\n\n')

    else:
        break

numeros_caracteres = []  # Lista que ira conter os caracteres separados
numeros_invertidos = ''

for num in str(numero):  # Separando caracteres
    numeros_caracteres.append(num)

total = len(numeros_caracteres)  # Total de caracteres no valor informado

while total != 0:  # Enquanto o programa nao analisar todos os caracteres
    numeros_invertidos += numeros_caracteres[-1]  # Adicionando o ultimo caractere
    numeros_caracteres.pop()  # Removendo ultimo caractere da lista de caracteres
    total -= 1

print('\n\n\t\t[ Resultado ]\n\n'
      f'Numero informado: {numero}\n'
      f'Numero invertido: {numeros_invertidos}')
