"""
Faça um Programa que peça dois números e imprima o maior deles.
"""

valores = []  # Lista que ira receber os dois valores.

while True:  # Enquanto o usuario nao digitar os dois valores corretamente.
    try:
        for c in range(2):
            valores.append(float(input(f'Digite o {c + 1}º valor: ')))

    except:
        print('\n\t\t\033[;31mDIGITE UM VALOR VALIDO\033[m\n')
        valores = []

    else:
        break

print(f'\n\n\t\tO maior valor entre {int(valores[0])} e {int(valores[1])} é {int(max(valores))}\n')
