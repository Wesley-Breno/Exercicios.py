"""
Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário.
O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos.
Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.
"""

while True:  # Enquanto o usuario nao informar um numero valido
    try:
        numero = int(input('\nInforme um valor para ver os numeros primos que tem ate o valor informado\n'
                           'Valor informado: '))
    except:
        print('\n\n\t\t[\033[;31mERRO\033[m]: Por favor, informe um valor valido\n\n')
    else:
        break

primos = []  # Lista que ira conter os numeros primos
numero_de_divisoes = 0  # Total de divisoes que o programa fez ate encontrar todos os valores primos

for c in range(1, numero + 1):  # Contagem ate o numero informado
    cont = 0
    for n in range(1, c + 1):  # Dividindo ate o numero da vez
        if c % n == 0:
            numero_de_divisoes += 1
            cont += 1

    if cont == 2:  # Se o numero for primo
        primos.append(c)

print(f'\n\n\t\tNumeros primos entre 1 e {numero}\n\n'
      f'Numeros primos: {primos}\n'
      f'Total de divisoes feitas: {numero_de_divisoes}')
