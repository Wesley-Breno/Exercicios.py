"""
Faça um programa para imprimir:
    1
    2   2
    3   3   3
    .....
    n   n   n   n   n   n  ... n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.
"""


def imprimi_arvore_de_n_valores(n):
    cont = 1  # Contador para imprimir o numero da vez

    while True:  # Enquanto a funcao nao imprimir toda a arvore
        for c in range(cont):  # Imprimindo o numero da vez, um do lado do outro
            print(cont, end=' ')
        print()

        if n == cont:  # Se a funcao ja imprimiu a arvore completa
            break
        else:
            cont += 1


if __name__ == "__main__":
    imprimi_arvore_de_n_valores(9)  # Imprimindo a arvore do valor 10
