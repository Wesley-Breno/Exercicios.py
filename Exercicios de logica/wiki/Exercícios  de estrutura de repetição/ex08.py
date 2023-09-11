"""
Faça um programa que leia 5 números e informe a soma e a média dos números.
"""

cont = 1  # Contador para saber qual valor esta sendo informado
valores = []  # Lista que ira ter os valores informados

while cont != 6:  # Enquanto o usuario nao informar os 5 valores
    try:
        valores.append(int(input(f'Informe o {cont}° valor: ')))

    except:  # Se o usuario nao informou o valor corretamente
        print('\n\n\t\t[\033[;31mERRO\033[m]: Insira os 5 valores corretamente\n\n')
        cont = 1
        valores = []

    else:
        cont += 1

print('\n\n\t\tResultado\n\n'
      f'Soma dos valores informados: {sum(valores)}\n'
      f'Media dos valores: {sum(valores) / len(valores)}')
