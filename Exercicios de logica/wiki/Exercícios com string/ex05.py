"""
Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida.

FULANO
FULAN
FULA
FUL
FU
F
"""

nome = str(input('Informe o seu nome: '))

quantidade_caracteres_nome = len(nome)  # Variavel responsavel por mostrar uma quantidade especifica de caracteres

while quantidade_caracteres_nome != 0:  # Enquanto o programa nao mostrar o nome em formato de escada invertida
    for c in range(quantidade_caracteres_nome):  # Mostrando quantidade especifica de caracteres
        print(nome[c], end='')

    print()

    quantidade_caracteres_nome -= 1  # Diminuindo a quantidade de caracteres que sera mostrado
