lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]


def verificar_duplicado(lista):
    numeros = set()
    duplicado = -1  # Retornara -1 se nao houver nenhum numero duplicado.

    for numero in lista:
        if numero in numeros:  # Se achar um numero que ja foi adicionado ao conjunto 'numeros'
            duplicado = numero
            break

        numeros.add(numero)  # Se este numero nao foi adicionado ainda.

    return duplicado


for lista in lista_de_listas_de_inteiros:
    print('__' * 18)
    print(f'{lista}\n'
          f'Primeiro numero duplicado -> {verificar_duplicado(lista)}')
    print('__' * 18)
    print()
