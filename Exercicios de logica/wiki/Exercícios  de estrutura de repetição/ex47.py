"""
Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e a pior nota são eliminadas.
A sua nota fica sendo a média dos votos restantes. Você deve fazer um programa que receba o nome do ginasta e as notas
dos sete jurados alcançadas pelo atleta em sua apresentação e depois informe a sua média, conforme a descrição acima
informada (retirar o melhor e o pior salto e depois calcular a média com as notas restantes). As notas não são
informados ordenadas. Um exemplo de saída do programa deve ser conforme o exemplo abaixo:

Atleta: Aparecido Parente
Nota: 9.9
Nota: 7.5
Nota: 9.5
Nota: 8.5
Nota: 9.0
Nota: 8.5
Nota: 9.7

Resultado final:
Atleta: Aparecido Parente
Melhor nota: 9.9
Pior nota: 7.5
Média: 9,04
"""

atletas = dict()
cont_atleta = 0  # Contador que ira servir como id do atleta

print('\n\n\t\t\033[;37m[Não informe o nome do atleta para encerrar o programa]\033[m\n\n')

while True:  # Enquanto o usuario quiser adicionar atletas
    cont_jurados = 1  # Contador que ira servir para informar o voto de qual jurado sera recebido
    cont_atleta += 1  # Trocando o id para adicionar outro atleta

    print()
    print('--' * 15)
    nome_atleta = str(input(f'Informe o nome do {cont_atleta}º atleta: ')).title()

    if nome_atleta == '':  # Se o usuario nao quer mais adicionar atletas
        break

    votos = []
    while cont_jurados != 8:  # Enquanto o usuario nao informar os 7 votos dos jurados que o atleta recebeu
        try:
            votos.append(float(input(f'Informe o voto do {cont_jurados}º jurado para o atleta "{nome_atleta}": ')))

        except ValueError:
            votos = []
            print(f'\n\n\t\t[\033[;31mERRO\033[m]: Por favor, informe o voto do {cont_jurados}º jurado corretamente.\n\n')

        else:
            cont_jurados += 1

    maior_voto = max(votos)
    menor_voto = min(votos)
    votos_formatado = []  # Lista com os votos, mas eliminando o maior e menor voto

    for voto in votos:
        if voto == maior_voto:
            ...
        elif voto == menor_voto:
            ...
        else:
            votos_formatado.append(voto)

    media = sum(votos_formatado) / len(votos_formatado)

    atletas[cont_atleta] = {'Nome do atleta': nome_atleta, 'Maior voto recebido': maior_voto, 'Menor voto recebido': menor_voto, 'Media': media}

if len(atletas) > 0:  # Se o usuario informou pelo menos 1 atleta
    print('\n\n\t\t[ Resultado final ]\n')
    for id_atleta, dados_atleta in atletas.items():
        for chave, valor in dados_atleta.items():
            print(f'{chave}: {valor}')
        print()

else:
    print('\n\n\t\tVoce nao informou nenhum atleta\n\n')
