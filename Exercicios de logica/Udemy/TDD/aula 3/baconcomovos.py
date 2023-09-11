"""
1 - Receber um numero inteiro
2 - Saber se o numero é multiplo de 3 e 5: Bacon com ovos
3 - Saber se o numero é multiplo somente de 3: Bacon
4 - Saber se o numero é multiplo somente de 5: Ovos
5 - Saber se o numero não é multiplo de 3 e 5: Passa fome
"""


def bacon_com_ovos(numero):
    """
    Funcao que retorna uma string dependendo do valor
    numerico que foi informado como parametro...

    - Se o numero for multiplo de 3 e 5: 'Bacon com ovos'
    - Se o numero for somente multiplo de 3: 'Bacon'
    - Se o numero for somente multiplo de 5: 'Ovos'
    - Se o numero nao for multiplo de 3 e nem de 5: 'Passar fome'

    :param numero: Valor que sera recebido para fazer o calculo.
    :return: Retorna a string dependendo se é multiplo ou nao de 3 e 5
    """
    assert isinstance(numero, int), 'numero deve ser int.'  # Se o numero nao for tipo int, levantara uma excessao assert.

    if numero % 3 == 0 and numero % 5 == 0:  # Se o numero for multiplo de 3 e 5.
        return 'Bacon com ovos'

    if numero % 3 == 0:  # Se o numero for multiplo de 3.
        return 'Bacon'

    if numero % 5 == 0:  # Se o numero for multiplo de 5.
        return 'Ovos'

    return 'Passar fome'  # Se o numero nao for multiplo de 3 e nem de 5.
