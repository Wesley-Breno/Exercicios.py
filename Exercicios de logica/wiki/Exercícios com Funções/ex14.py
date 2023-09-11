"""
Quadrado mágico. Um quadrado mágico é aquele dividido em linhas e colunas, com um número em cada posição e no qual a
soma das linhas, colunas e diagonais é a mesma. Por exemplo, veja um quadrado mágico de lado 3, com números de 1 a 9:
8  3  4
1  5  9
6  7  2
Elabore uma função que identifica e mostra na tela todos os quadrados mágicos com as características acima. Dica:
produza todas as combinações possíveis e verifique a soma quando completar cada quadrado. Usar um vetor de 1 a 9 parece
ser mais simples que usar uma matriz 3x3.
"""

from itertools import permutations  # Funcao que sera responsavel por gerar as possibilidades de combinacoes


def quadrados_magicos(lista: list) -> None:
    """
    Funcao que recebe um lista com 9 valores numericos inteiros
    e retorna os quadrados magicos possiveis que podem se fazer
    com os valores da lista.
    :param lista: Lista que ira conter 9 valores numericos inteiros
    :return: None
    """
    verificador_de_inteiros = 0
    quadrados_magicos_gerados = 0

    for dado in lista:  # Contando quantos numeros inteiros tem na lista
        if type(dado) == int:
            verificador_de_inteiros += 1

    # Se a lista conter 9 dados e todos eles se tratarem de um numero inteiro
    if len(lista) == 9 and verificador_de_inteiros == len(lista):
        for combinacao in permutations(lista):  # Para cada combinacao de numeros possiveis
            soma_final = sum(combinacao[:3])  # Soma que deve ser igual a soma das linhas/colunas/diagonais
            cont = 0

            colunas_e_diagonais = combinacao[0:7:3], combinacao[1:8:3], combinacao[2:9:3], combinacao[0:9:4], combinacao[2:8:2]
            for conjunto in colunas_e_diagonais:  # Verificando se cada coluna/diagonal é igual a soma final
                if sum(conjunto) == soma_final:
                    cont += 1

            # Se as linhas forem igual a soma final e as colunas e diagonais tambem forem
            if sum(combinacao[3:6]) == soma_final and sum(combinacao[6:10]) == soma_final:
                if cont == len(colunas_e_diagonais):
                    print(combinacao[:3])
                    print(f'{combinacao[3:6]} = {soma_final}')
                    print(combinacao[6:10])
                    print()
                    quadrados_magicos_gerados += 1

    if quadrados_magicos_gerados == 0:  # Se a funcao nao encontrou nenhum quadrado magico possivel
        print('\n\n\t\tNao conseguimos encontrar um quadrado magico :(\n\n')


if __name__ == '__main__':
    a = [8, 3, 4, 1, 5, 9, 6, 7, 2]
    quadrados_magicos(a)
