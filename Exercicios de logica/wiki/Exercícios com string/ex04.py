"""
Nome na vertical em escada.
Modifique o programa anterior de forma a mostrar o nome em formato de escada.

F
FU
FUL
FULA
FULAN
FULANO
"""

nome = str(input('Informe o seu nome: '))

quantidade_caracteres_nome = 0  # Variavel que sera responsavel por mostrar uma quantidade especifica de caracteres

while True:  # Enquanto o programa nao mostrar o nome em formato de escada
    for c in range(quantidade_caracteres_nome):  # Mostrando quantidade especifica de caracteres
        print(nome[c], end='')

    print()

    quantidade_caracteres_nome += 1  # Aumentando a quantidade de caracteres que sera mostrado
    if quantidade_caracteres_nome > len(nome):  # Se o programa ja mostrou o nome em formato de escada
        break
