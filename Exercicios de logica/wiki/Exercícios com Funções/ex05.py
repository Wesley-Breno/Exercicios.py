"""
Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a
quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função
“altera” o valor de custo para incluir o imposto sobre vendas.
"""


def soma_imposto(taxa_imposto: float, custo: float):
    """
    Funcao que recebe um valor porcentual como parametro e um valor total de custo.
    A funcao ira fazer a soma do custo com o percentual que foi informado e
    retornar o valor total da soma com o custo + valor percentual.
    :param taxa_imposto: Valor percentual que sera usado para fazer a soma com o custo.
    :param custo: Valor que sera somado com o parametro "taxa_imposto", que sera o percentual que sera somado.
    :return: Retorna o valor total da soma com o percentual.
    """

    custo_total = custo + (custo * taxa_imposto / 100)  # Fazendo soma do valor percentual com o custo.
    return custo_total


if __name__ == "__main__":
    resultado_soma_imposto = soma_imposto(10, 100)
    print(f'\n\t\tCusto com imposto: R$ {resultado_soma_imposto:.2f}')
