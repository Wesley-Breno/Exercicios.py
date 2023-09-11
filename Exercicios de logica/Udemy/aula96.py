from random import randint


def numeros_cnpj(cnpj):
    """
    Funcao que so vai pegar os numeros do CNPJ, tirando os 2 ultimos digitos.
    :param cnpj: CNPJ
    :return: Retorna somente os numeros do CNPJ e sem os 2 ultimos digitos.
    """
    cnpj_copia = [n for p, n in enumerate(cnpj) if n.isdigit() and p < 15] if len(cnpj) == 18 else \
        [n for p, n in enumerate(cnpj) if n.isdigit() and p < 12]  # Pegando tudo, menos 2 ultimos digitos

    return ''.join(cnpj_copia)  # Retornando somente os numeros do CNPJ, sem os 2 ultimos caracteres.


def digito(cnpj, start=5):
    """
    Funcao que vai fazer o calculo e colocar o penultimo e ultimo digito do CNPJ.
    :param cnpj: CNPJ
    :param start: De onde ira comecar a contagem para fazer o calculo, 5 para o penultimo digito, 6 para ultimo.
    :return: Retorna o digito
    """
    resultado = 0

    for n in cnpj:  # Indo por cada numero do CNPJ e fazendo o calculo
        start = 9 if start == 1 else start
        resultado += int(n) * start
        start -= 1

    ult_num = 11 - (resultado % 11)  # Pegando o digito
    ult_num = 0 if ult_num > 9 else ult_num

    return str(ult_num)  # Retornando digito


def gera_cnpj():
    """
    Funcao que gera um CNPJ e retorna o mesmo.
    :return: CNPJ valido
    """
    while True:  # Enquanto a funcao nao fazer um CNPJ valido
        cnpj = ''
        for posicao in range(10):  # Adicionando numeros aleatorios e colocando os '.', '/' e '-' de um CNPJ
            if posicao == 2 or posicao == 5:
                cnpj += '.'
            if posicao == 7:
                cnpj += str(randint(0, 9))
                cnpj += '/0001-'
            else:
                cnpj += str(randint(0, 9))

        cnpj_numeros = [n for n in cnpj if n.isdigit()]  # Pegando somente os numeros do CNPJ
        cnpj_numeros = ''.join(cnpj_numeros)  # Concatenando os numeros do CNPJ

        cnpj2 = numeros_cnpj(cnpj)
        cnpj2 += digito(cnpj2)
        cnpj2 += digito(cnpj2, 6)

        if cnpj_numeros == cnpj2:  # Comparando os numeros do CNPJ original com oque foi feito o calculo
            break

    return cnpj


for c in range(5):
    cnpj = gera_cnpj()
    print(cnpj)
