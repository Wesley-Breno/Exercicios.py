"""
Crie um programa que gerencie o aproveitamento de um jogador de futebol
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo
o total de gols feitos durante o campeonato.
"""

jogador = dict()  # Dicionario onde ficara as informacoes do jogador
jogador['gols'] = []  # Adicionando uma chave gols que ira conter uma lista com os gols feitos

while True:  # Enquanto os dados do jogador nao forem inseridos
    jogador['nome'] = str(input('Nome do jogador: '))

    try:
        quantidade_partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou:  '))

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

        print(f'''\n\n\t\tInformações
        
|> Nome do jogador: {jogador["nome"]}
|> Total de partidas jogadas: {quantidade_partidas}''')
        for c in range(len(jogador['gols'])):
            print(f'|> Total de gols {c + 1}º partida: {jogador["gols"][c]}')
        print(f'|> Total de gols: {jogador["total_gols"]}\n\n')
        break
