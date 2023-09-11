"""
Faça um programa para imprimir:
    1
    1   2
    1   2   3
    .....
    1   2   3   ...  n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.
"""


def imprimi_arvore_de_n_valores(n):
    quantidade_numeros_na_linha = 1  # Contador que ira informar a quantidade de numeros de cada linha
    contador = 1  # Contador que ira fazer a contagem dos numeros de cada linha

    while True:  # Enquanto a funcao nao imprimir toda a arvore
        for c in range(quantidade_numeros_na_linha):  # Imprimindo a contagem dos numeros de cada linha
            print(contador, end=' ')
            contador += 1
        print()

        if n == quantidade_numeros_na_linha:  # Se a funcao ja imprimiu a arvore completa
            break
        else:
            quantidade_numeros_na_linha += 1
            contador = 1


if __name__ == "__main__":
    imprimi_arvore_de_n_valores(9)  # Imprimindo a arvore do valor 10
