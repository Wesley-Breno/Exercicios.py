"""
Faça um programa que calcule o mostre a média aritmética de N notas.
"""

numeros = []  # Valores que o usuario ira informar
contador = 1  # Contador para saber quantos numeros estao sendo informados

print('\n\n\t\t\033[;37mDigite [ 0 ] para parar de adicionar valores\033[m\n\n')

while True:  # Enquanto o usuario nao digitar 0
    try:
        valor = int(input(f'\nDigite valores para mostrar sua media aritmetica\n{contador}º valor: '))

    except:
        print('\n\n\t\t[\033[;31mERRO\033[m]: Por favor, insira um valor novamente.\n\n')

    else:
        if valor == 0:  # Parando de adicionar valores
            break

        numeros.append(valor)
        contador += 1

print('\n\n\t\tResultado\n\n'
      f'Valores informados: {numeros}\n'
      f'Media aritmetica: {sum(numeros)} / {len(numeros)} = \033[;4m{sum(numeros) / len(numeros)}\033[m')
