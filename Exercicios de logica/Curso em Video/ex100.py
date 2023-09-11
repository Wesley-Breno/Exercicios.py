"""
Faça um programa que tenha uma lista chamada números e duas funções
chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números
e vai colocá-los dentro da lista e a segunda função vai mostrar a soma
entre todos os valores pares sorteados pela função anterior.
"""

from random import randint  # Importando a funcao randint para gerar numeros inteiros aleatorios
from time import sleep  # Importando a funcao sleep para fazer o programa demorar para executar o proximo passo

numeros = []


def sorteia(lista):
    """
    Funcao que recebe uma lista como parametro e adiciona 5 valores inteiros na lista.
    :param lista: Parametro onde ficara a lista.
    :return: None
    """
    print('Numeros que foram adicionados na lista: ', end='')

    for c in range(5):
        numero_aleatorio = randint(1, 9)  # Numero que sera adicionado na lista
        print(numero_aleatorio, end=' ')
        sleep(0.5)

        lista.append(numero_aleatorio)  # Adicionando numero na lista


def somapar(lista):
    """
    Funcao que recebe uma lista de numeros inteiros como parametro e mostra a soma entre os valores pares.
    :param lista: Parametro que recebe a lista de numeros inteiros
    :return: None
    """
    soma = 0  # Variavel que recebera a soma dos valores pares

    for numero in lista:
        if numero % 2 == 0:  # Se o resto da divisao por 2 do numero for igual a 0.
            soma += numero

    if soma == 0:  # Se nao tiver nenhum numero par na lista.
        print(f'\nSoma dos valores pares da lista: \033[;37m[Nenhum valor par foi adicionado]\033[m')

    else:
        print(f'\nSoma dos valores pares da lista: {soma}')


print('-=-' * 17)
sorteia(numeros)
somapar(numeros)
print('-=-' * 17)
