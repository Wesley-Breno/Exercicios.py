"""
Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
"""

notas = []

while True:  # Enquanto o usuario nao informar as 4 notas corretamente
    try:
        for c in range(4):
            notas.append(float(input(f'Informe a {c + 1}º nota\nNota: ')))

    except ValueError:
        print('\n\n\t\t[\033[;31mERRO\033[m]: Por favor, informe as notas corretamente.\n\n')
        notas = []

    else:
        break

print('\n\t\tResultado\n\n'
      f'Notas: {notas}\n'
      f'Media: {sum(notas) / len(notas)}')
