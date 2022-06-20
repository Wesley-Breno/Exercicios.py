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


print(f'\n\n\033[;37m{"Digite [ 0 ] para encerrar":^45}\033[m\n\n')
while True:  # Enquanto usuario nao digitar 0 na variavel 'cnpj'
    cnpj = str(input('Digite o CNPJ: '))

    if len(cnpj) == 1 and cnpj == '0':
        break

    if len(cnpj) == 18 or len(cnpj) == 14:
        cnpj = [n for n in cnpj if n.isdigit()]  # Pegando somente os numeros do CNPJ
        cnpj = ''.join(cnpj)

        cnpj2 = numeros_cnpj(cnpj)  # Fazendo a copia do CNPJ, sem os 2 ultimos digitos
        cnpj2 += digito(cnpj2)  # Fazendo calculo e colocando o penultimo digito
        cnpj2 += digito(cnpj2, 6)  # Fazendo calculo e colocando o ultimo digito

        print(f'\n\n\033[;1m{"Este CNPJ é valido!":^45}\033[m\n\n' if cnpj == cnpj2 else
              f'\n\n\033[;1m{"Este CNPJ é invalido!":^45}\033[m\n\n')

    else:
        print('\n\n\033[1;31mERRO\033[m\nPor favor, digite o CNPJ corretamente.\n\n')

print(f'\n\n\033[;1m{"Programa encerrado com sucesso <3":^45}\033[m\n\n')
