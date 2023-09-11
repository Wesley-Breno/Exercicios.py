"""
Em uma competição de salto em distância cada atleta tem direito a cinco saltos. No final da série de saltos de cada
atleta, o melhor e o pior resultados são eliminados. O seu resultado fica sendo a média dos três valores restantes.
Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois
informe a média dos saltos conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a
média). Faça uso de uma lista para armazenar os saltos. Os saltos são informados na ordem da execução, portanto não são
ordenados. O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser
conforme o exemplo abaixo:

Atleta: Rodrigo Curvêllo

Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Melhor salto:  6.5 m
Pior salto: 5.3 m
Média dos demais saltos: 5.9 m

Resultado final:
Rodrigo Curvêllo: 5.9 m
"""

atletas = {}  # Dicionario que ira ficar todos os atletas e seus dados
cont = 1  # Contador que sera usado como o id de cada usuario

print('\n\n\t\t\033[;37m[Não informe o nome do atleta para encerrar o programa]\033[m\n\n')

while True:  # Enquanto o usuario quiser ficar adicionando atletas
    print()
    print('--' * 14)
    nome_atleta = str(input(f'Digite o nome do {cont}º atleta\nNome: ')).title()

    if nome_atleta == '':  # Se o usuario decidiu parar de adicionar atletas
        break

    saltos_formatados = []  # Lista que ira conter todos os saltos, menos o maior salto e o menor salto.

    while True:  # Enquanto o usuario nao informar os 5 saltos do atleta informado
        try:
            for c in range(5):
                saltos_formatados.append(float(input(f'Informe a distancia do {c + 1}º salto: ')))
        except ValueError:
            print('\n\n\t\t[\033[;31mERRO\033[m]: Por favor, informe um valor numerico para a distancia.\n\n')
            saltos_formatados = []
        else:
            maior_salto = max(saltos_formatados)
            menor_salto = min(saltos_formatados)
            todos_os_saltos = saltos_formatados[:]  # Lista que ira conter todos os saltos

            for index, salto in enumerate(saltos_formatados):  # Retirando o maior e o menor salto da lista
                if salto == maior_salto:
                    saltos_formatados.pop(index)

                if salto == menor_salto:
                    saltos_formatados.pop(index)

            media_saltos = sum(saltos_formatados) / len(saltos_formatados)

            atletas[cont] = {'Nome atleta': nome_atleta,
                             'Saltos': todos_os_saltos,
                             'Maior salto': maior_salto,
                             'Menor salto': menor_salto,
                             'Media saltos': media_saltos}
            break

    cont += 1  # Aumentando valor do contador para ser o ID de outro atleta

atletas_e_medias = dict()  # Dicionario que so ira conter o nome dos atletas e a media de saltos deles

if len(atletas) > 0:  # Se o usuario adicionou pelo menos 1 atleta
    print('\n\t\t[ Resultado ]')
    for id_atleta, dados_atleta in atletas.items():
        print()
        print('--' * 13)
        print(f'ID do atleta: {id_atleta}')
        for chave, valor in dados_atleta.items():
            print(f'{chave}: {valor}')

        atletas_e_medias[dados_atleta['Nome atleta']] = dados_atleta['Media saltos']

    print('\n\t\t[ Resultado final ]\n')
    for nome, media in atletas_e_medias.items():
        print(f'{nome}: {media}m')
