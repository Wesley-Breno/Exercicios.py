"""
Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado.
Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imputa(),
mas com uma validação de dados para aceitar apenas valores que seja monetários.
"""


def leiadinheiro(mensagem):
    """
    Funcao que escreve uma mensagem e recebe um input do usuario onde so
    é possivel receber valores numericos, e tambem é possivel receber valor Float com ','.

    :param mensagem: Mensagem que aparecera na tela para o usuario
    :return: Retorna o valor digitado em tipo Float
    """
    while True:  # Enquanto o usuario nao digitar o valor corretamente
        print(mensagem, end='')  # Mostrando a mensagem na tela e recebendo o input
        valor = str(input())  # Recebendo o input

        valor = valor.replace('.', ',')  # Trocando as ',' por '.'

        cont = 0  # Contador para saber se todos os caracteres sao numericos ou ','
        for caractere in valor:
            if caractere == ',':
                cont += 1

            if caractere.isdigit():
                cont += 1

        if valor == '' or cont != len(valor):  # Se o usuario digitou nada ou caracteres foram informados invalidamente
            print('\n\t\t[\033[;31mERRO\033[m]: Informe um valor numerico.\n')

        if cont == len(valor):  # Se os caracteres estiverem corretos
            valor = valor.replace(',', '.')

            try:  # Tentando retornar o valor em tipo Float
                return float(valor)

            except:  # Fazendo repetir o While se nao conseguir
                ...
