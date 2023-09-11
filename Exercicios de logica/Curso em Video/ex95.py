"""
Aprimore o desafio 93 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
"""

jogadores = []
cont = 1  # Contador para saber quantos jogadores foram adicionados
while True:  # Enquanto os dados do jogador nao forem inseridos
    jogador = dict()  # Dicionario onde ficara as informacoes do jogador
    jogador['gols'] = []  # Adicionando uma chave gols que ira conter uma lista com os gols feitos

    if cont > 1:  # Se tiver mais de 1 jogador adicionado
        print('\n\n\t\t\033[;37mDigite [ 0 ] para ver a tabela de jogadores\033[m\n\n')

    jogador['nome'] = str(input(f'Nome do {cont}º jogador: '))

    if jogador['nome'] == '0':
        break

    try:
        quantidade_partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou:  '))

        if quantidade_partidas == 0:
            break

    except:
        print('\n\n\t\t[\033[;31mERRO\033[m]: Verifique o valor inserido\n\n')

    else:
        while True:  # Enquanto os gols de cada partida nao forem informados
            for c in range(quantidade_partidas):
                try:
                    jogador['gols'].append(int(input(f'Quantos gols na {c + 1}º partida: ')))

                except:  # Se o usuario informou um valor invalido
                    print('\n\n\t\t[\033[;31mERRO\033[m]: Verifique o valor inserido\n\n')
                    jogador['gols'].clear()
                    break

            if len(jogador['gols']) == quantidade_partidas:  # Se foi informado os gols de cada partida
                break

        jogador['total_gols'] = sum(jogador['gols'])  # Pegando a soma de cada gol feito
        jogador['id'] = cont  # Adicionando ID ao jogador
        jogadores.append(jogador)  # Adicionando jogador na lista de jogadores
        cont += 1

if len(jogadores) >= 1:  # Se tiver pelo menos 1 jogador adicionado
    print('\n\nID - Nome \t\t Gols \t\t T. gols')
    print('--' * 20)
    for jogador in jogadores:
        print(f'{jogador["id"]} - {jogador["nome"]}\t\t{jogador["gols"]}\t\t{jogador["total_gols"]}')

    print('--' * 20)
    while True:  # Enquanto o usuario nao digitar 0
        try:
            print('\n\n\t\t\033[;37mDigite [ 0 ] para encerrar programa\033[m\n\n')

            deseja = int(input('Deseja mostrar os dados de qual jogador? (Informe com base no ID)\n'
                               'ID do jogador: '))
            if deseja == 0:
                print('\n\n\t\tPrograma encerrado com sucesso :)\n\n')
                break

        except:
            print('\n\n\t\t[\033[;31mERRO\033[m]: Verifique o valor inserido\n\n')

        else:
            cont = 0  # Contador para saber quantas vezes procurou e nao achou o jogador com o ID informado
            for jogador in jogadores:  # Para cada jogador na lista
                if jogador['id'] == deseja:  # Se o ID informado estiver na lista de jogadores
                    print(f'''\n\n\t\tInformações

|> Nome do jogador: {jogador["nome"]}
|> Total de partidas jogadas: {len(jogador["gols"])}''')
                    for c in range(len(jogador['gols'])):
                        print(f'\t|> Total de gols {c + 1}º partida: {jogador["gols"][c]}')
                    print(f'|> Total de gols: {jogador["total_gols"]}\n\n')
                    break

                else:
                    cont += 1

            if cont == len(jogadores):  # Se o contador for igual a quantidade de jogadores
                print('\n\n\t\t[\033[;31mERRO\033[m]: ID nao encontrado, verifique o valor inserido\n\n')

else:
    print('\n\n\t\t\033[;37mVoce nao digitou jogadores suficientes para mostrar a tabela.\033[m\n\n')
