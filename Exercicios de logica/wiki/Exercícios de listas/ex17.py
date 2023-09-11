"""
Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta será determinado
pela média dos cinco valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas
pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. O programa deve ser encerrado quando
não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:

Atleta: Rodrigo Curvêllo

Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Resultado final:
Atleta: Rodrigo Curvêllo
Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
Média dos saltos: 5.9 m
"""

atletas = []  # Lista onde ficara a lista de cada atleta com seus dados
cont = 1  # Contador para informar ID do atleta

while True:  # Enquanto o usuario informar o nome do atleta
    atleta = []  # Lista onde ficara os dados do atleta da vez
    saltos = []  # Lista onde ficara os saltos do atleta da vez

    print()
    print('--' * 20)
    nome_atleta = str(input(f'Informe o nome do {cont}º atleta\nNome: '))

    if nome_atleta == '':  # Se o usuario decidiu encerrar o programa
        break

    while len(saltos) != 5:  # Enquanto o usuario nao informar os 5 saltos do atleta
        try:
            print()
            for c in range(5):
                saltos.append(float(input(f'Informe o valor do {c + 1}º salto: ')))

        except ValueError:
            print('\n\n\t\t[\033[;31mERRO\033[m]: Por favor, informe os valores dos saltos corretamente.\n\n')
            saltos = []

    atleta.append(nome_atleta)
    atleta.append(saltos)
    atleta.append(sum(saltos) / len(saltos))  # Adicionando a media nos dados do atleta
    atletas.append(atleta)  # Adicionando dados do atleta na lista de atletas
    cont += 1  # Trocando ID para o proximo atleta

if len(atletas) > 0:  # Se o usuario informou os dados de pelo menos 1 atleta
    print('\n\n\t\tResultado')
    for esportista in atletas:
        print()
        print(f'Atleta: {esportista[0]}\n'
              f'Saltos: ', end='')
        print(*esportista[1], sep=' - ')
        print(f'Média dos saltos: {esportista[2]:.1f} m')

else:
    print('\n\n\t\t\033[;37mVocê não informou os dados de nenhum atleta\033[m\n\n')
