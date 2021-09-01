# Aqui fica algumas funcoes que irei usar em alguns exercicios. :)

def pular(n=1):
    """
    Funcao que sera usada para pular linhas sem o uso exagerado
    de prints ou estruturas de repeticao.
    :param n: Serve para colocar a quantidade de linhas que serao puladas.
    :return: None
    """
    for c in range(0, n):
        print()
