def soma(x, y):
    """
    Funcao que soma os parametros x, y e retorna o resultado.

    # Teste 1
    # Chamando a funcao soma e colocando seus parametros, depois espera que o resultado retornado seja igual a 2.
    >>> soma(1, 1)
    2

    # Teste 2
    # Chamando a funcao soma e colocando seus parametros, depois espera que o resultado retornado seja igual a 10.
    >>> soma(-10, 20)
    10

    # Teste 3
    # Chamando a funcao soma e colocando seus parametros, depois espera que o resultado retornado seja igual a um AssertionError.
    >>> soma('10', 20)
    Traceback (most recent call last):
    ...
    AssertionError: Parametro [ x ]: Digite numeros inteiros ou flutuantes.
    """
    assert isinstance(x, (int, float)), 'Parametro [ x ]: Digite numeros inteiros ou flutuantes.'  # So ira prosseguir se a instancia da variavel for igual a int ou float.
    assert isinstance(y, (int, float)), 'Parametro [ y ]: Digite numeros inteiros ou flutuantes.'
    return x + y


def subtrai(a, b):
    """
    Funcao que subtrai os parametros a, b e retorna o resultado.

    # Teste 1
    # Chamando a funcao subtrai e colocando seus parametros, depois espera que o resultado seja igual a 5.
    >>> subtrai(10, 5)
    5
    """
    return a - b


if __name__ == '__main__':
    import doctest
    doctest.testmod()  # Iniciando doctests
