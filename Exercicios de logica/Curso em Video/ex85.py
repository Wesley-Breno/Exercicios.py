"""
Crie um programa onde o usuário possa digitar sete valores numéricos
e cadastre-os em uma lista única que mantenha separados os valores
pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
"""

lista = [[], []]  # Colocando duas listas vazias dentro da lista, cada lista vai ter valores pares/impares

for c in range(7):
    print('__' * 12)
    numero = int(input(f'Digite o {c + 1}º valor: '))

    if numero % 2 == 0:  # Se o numero for par, adiciona na primeira lista da lista
        lista[0].append(numero)

    else:  # Adiciona na segunda
        lista[1].append(numero)

print('\n\n\t\tResultado\n'
      f'Pares: {sorted(lista[0])}\n'  # Mostrando os valores que sao pares
      f'Impares: {sorted(lista[1])}\n\n')  # Mostrando os valores que sao impares
