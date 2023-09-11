
# Dados que serao adicionados no arquivo
cont = 0  # Contador para saber qual coluna esta digitando.
colunas = []  # Os caracteres da primeira linha
linha = []  # Lista que ira ficar tudo oque o usuario digitar em uma linha
dados = []  # Todos os dados digitados de forma agrupada

print('\n\n\t\t\033[;37mDigite [ 0 ] pra parar de adicionar colunas\n\t\te adicionar os dados...\033[m\n\n')

while True:  # Enquanto o usuario nao quiser mais adicionar colunas no arquivo .csv
    cont += 1
    coluna = str(input(f'Informe o nome da {cont}º coluna: '))  # Recebendo o nome da coluna

    if coluna == '0':  # Se o usuario decidiu encerrar
        break

    colunas.append(coluna)

if len(colunas) > 0:  # Se o usuario digitou algum dado

    print('\n\n\t\t\033[;37mDigite [ 0 ] pra parar de adicionar dados e criar o arquivo.\033[m\n\n')

    cont = 0  # Contador para saber em qual coluna esta escrevendo
    while True:  # Enquanto o usuario estiver adicionando dados nas colunas
        print('\n')
        print('__' * 20)
        dado = str(input(f'Informe o dado da coluna {colunas[cont]}: '))  # Adicionando dados em cada coluna

        if dado == '0':  # Se o usuario decidiu parar de adicionar dados e criar o arquivo
            break

        cont += 1

        linha.append(dado)

        if cont == len(colunas):  # Se todas colunas foram preenchidas, limpa a lista para adicionar dados na proxima linha
            dados.append(linha)  # Adicionando os dados de cada linha
            linha = []
            cont = 0

    if len(dados) > 0:

        with open('dados.csv', 'w+') as file:  # Criando/sobrescrevendo arquivo .csv
            for index, item in enumerate(colunas):  # Para cada coluna ( palavras da primeira linha do arquivo )

                if index != len(colunas) - 1:  # Se nao estiver no final da lista
                    file.write(f'{item}, ')

                else:
                    file.write(item)

            file.write('\n')  # Pulando linha

            for item in dados:  # Para cada linha escrita
                for index, nome in enumerate(item):  # Para cada dado na linha

                    if index != len(item) - 1:  # Se nao estiver no final da lista
                        file.write(f'{nome}, ')

                    else:
                        file.write(nome)

                file.write('\n')  # Pulando para proxima linha

    else:
        print('\n\n\t\t[\033[;31mERRO\033[m]: Nenhum dado informado.\n\n')

else:
    print('\n\n\t\t[\033[;31mERRO\033[m]: Nenhum dado informado.\n\n')
