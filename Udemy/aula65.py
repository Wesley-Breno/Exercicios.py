lista_numeros = [[1, 2, 3], [4, 5, 6, 6], [7, 8, 9], [9, 9, 9]]    # Lista que foi usada para o teste do algoritmo


def tem_duplicado(*args):
    """
    Função feita para verificar se tem algum
    numero que apareça mais de uma vez (duplicado).

    :param args: parametro onde sera colocado a lista/tupla/set com seus numeros ou a sequencia de numeros.
    :return: Retorna 0 se tiver numeros duplicados, retorna -1 se nao tiver numeros duplicados.
    """
    if len(args) > 1 and type(args) == tuple:   # Se o usuario tiver digitado numero por numero
        lista = []  # Recriando a lista
        numeros_duplicados = []     # Lista onde vai ficar os numeros duplicados
        for n in args:
            if n not in lista:  # Verificando se o numero nao esta na lista
                lista.append(n)
            else:
                if n not in numeros_duplicados:     # Se o numero for duplicado, adiciona ele na lista de duplicados
                    numeros_duplicados.append(n)
        if len(numeros_duplicados) > 0:     # Se tiver numeros duplicados
            # Retornando o 0 para dizer que tem numero multiplicado, retorna a lista, retorna os numeros duplicados
            return 0, args, numeros_duplicados
        else:
            return -1, lista    # Retorna -1 se nao tiver numero duplicado, retorna a lista com os numeros analisados

    else:   # Se o usuario tiver colocado uma lista como parametro
        numeros_duplicados = []
        lista = []
        # Verificando lista por lista para ver se tem numeros duplicados
        for l1 in args:
            for l2 in l1:
                for n in l2:
                    if n not in lista:
                        lista.append(n)
                    else:
                        if n not in numeros_duplicados:
                            numeros_duplicados.append(n)
        if len(numeros_duplicados) > 0:
            return 0, args, numeros_duplicados
        else:
            return -1, lista


res = tem_duplicado(lista_numeros)
if len(res[1]) == 1:    # Se foi usado uma lista com numeros para fazer o analise
    if res[0] == 0:     # Se tiver numero duplicado
        print('\nTotal de numeros colocados.')
        for l1 in res[1]:   # Escrevendo cada lista e seus numeros
            for l2 in l1:
                print(l2)
        print(f'Numeros que foram duplicados: {res[2]}')
    else:
        print('\nTotal de numeros colocados.')
        print(res[1])
        print('Nenhum numero duplicado foi encontrado!')
else:
    if res[0] == 0:
        print('\nTotal de numeros colocados.')
        print(res[1])
        print(f'Numeros que foram duplicados: {res[2]}')
    else:
        print('\nTotal de numeros colocados.')
        print(res[1])
        print('Nenhum numero duplicado foi encontrado!')

