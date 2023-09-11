"""
Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a
entrada e permita repetir a operação.
"""

deseja_encerrar = 0  # Variavel que ira conter o valor que ira dizer se o usuario quer encerrar o programa ou nao

while deseja_encerrar != '2':  # Enquanto o usuario nao desejou encerrar o programa
    while True:  # Enquanto o usuario nao informar a quantidade de habitantes e a taxa de crescimento anual
        print('--' * 22)
        try:
            populacao_pais_a = float(input('Informe a quantidade de habitantes do país A\n'
                                           'Quantidade de habitantes: '))
            taxa_crescimento_pais_a = float(input('\nInforme a taxa de crescimento do pais A\n'
                                                  'Taxa de crescimento: '))
        except:
            print('\n\n\t\t[\033[;31mERRO\033[m]: Informe os dados do país A corretamente.\n\n')

        else:
            break

    while True:
        print('--' * 22)
        try:
            populacao_pais_b = float(input('Informe a quantidade de habitantes do país B\n'
                                           'Quantidade de habitantes: '))
            taxa_crescimento_pais_b = float(input('\nInforme a taxa de crescimento do pais B\n'
                                                  'Taxa de crescimento: '))
        except:
            print('\n\n\t\t[\033[;31mERRO\033[m]: Informe os dados do país B corretamente.\n\n')

        else:
            break

    total_de_anos = 0  # Variavel que ira conter a quantidade de anos para ultrapassar o outro país

    if populacao_pais_a < populacao_pais_b:  # Se o país A for menor que o país B
        while populacao_pais_a < populacao_pais_b:  # Enquanto o pais A for menor que o pais B
            populacao_pais_a = populacao_pais_a + (populacao_pais_a * taxa_crescimento_pais_a / 100)  # Adicionando taxa de crescimento anual da população do pais A
            populacao_pais_b = populacao_pais_b + (populacao_pais_b * taxa_crescimento_pais_b / 100)  # Adicionando taxa de crescimento anual da população do pais B
            total_de_anos += 1  # Fazendo a contagem de anos

        print(f'\n\n[ O país A precisara de {total_de_anos} anos para ultrapassar o país B em numero de habitantes ]\n\n')

    elif populacao_pais_b < populacao_pais_a:  # Se o país B for menor que o país A
        while populacao_pais_b < populacao_pais_a:
            populacao_pais_a = populacao_pais_a + (populacao_pais_a * taxa_crescimento_pais_a / 100)
            populacao_pais_b = populacao_pais_b + (populacao_pais_b * taxa_crescimento_pais_b / 100)
            total_de_anos += 1

        print(f'\n\n[ O país B precisara de {total_de_anos} anos para ultrapassar o país A em numero de habitantes ]\n\n')

    else:  # Se o numero de habitantes dos dois países forem iguais.
        print('\n\n\t\t[ O numero de habitantes dos dois países sao iguais ]\n\n')

    while True:  # Enquanto o usuario nao informar se quer continuar ou encerrar o programa.
        print('--' * 17)
        deseja_encerrar = str(input('Deseja fazer outro calculo?\n'
                                    '[ 1 ] - Sim\n'
                                    '[ 2 ] - Nao\n\n'
                                    'Informe o numero: '))

        if deseja_encerrar == '1':
            break

        elif deseja_encerrar == '2':
            break

        else:
            print('\n\n\t\t[\033[;31mERRO\033[m]: Informe um dos numeros que correspondem a uma escolha.\n\n')

print('\n\n\t\tPrograma encerrado com sucesso.')
