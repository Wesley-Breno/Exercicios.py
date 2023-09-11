"""
Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos existentes entre 1
e um número inteiro informado pelo usuário.
"""

cont = 0  # Contador que sera usado para saber quantas vezes o numero da vez foi divisivel
numeros_primos = []

while True:  # Enquanto o usuario nao informar um numero inteiro
    try:
        numero_informado = int(input('\nInforme um numero para ver os numeros primos existentes ate o numero informado\n'
                           'Numero inteiro: '))
    except:
        print('\n\n\t\t[\033[;31mERRO\033[m]: Por favor, informe um numero inteiro corretamente.\n\n')
    else:
        break


for numero in range(1, numero_informado + 1):  # Para cada numero ate o numero informado
    if cont == 2:  # Se o numero da vez anterior for primo
        numeros_primos.append(numero - 1)

    cont = 0

    for num in range(1, numero + 1):  # Fazendo divisoes de cada numero ate o numero da vez
        if numero % num == 0:
            cont += 1

print(f'\n\n\t\tNumeros primos existentes de 1 a {numero_informado}\n'
      f'\t\t\t\t\t\t↯\n'
      f'{numeros_primos}')
