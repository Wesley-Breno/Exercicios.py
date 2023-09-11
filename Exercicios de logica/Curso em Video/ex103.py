"""
Faça um programa que tenha uma função chamada ficha(),
que receba dois parâmetros opcionais: o nome de um jogador
e quantos gols ele marcou. O programa deverá ser capaz de
mostrar a ficha do jogador, mesmo que algum dado não tenha
sido informado corretamente.
"""


def ficha(nome_jogador='(desconhecido)', gols='0'):
    """
    Funcao que recebe dois valores opcionais como parametro e
    mostra a ficha do jogador, independente se foi colocado ou
    nao valores nos parametros.
    :param nome_jogador: Parametro onde ficara o nome do jogador
    :param gols: Parametro onde ficara os gols feitos pelo jogador
    :return: None
    """
    if nome_jogador == '':  # Se o usuario so pressionou enter
        nome_jogador = '(desconhecido)'

    if gols == '':  # Se o usuario so pressionou enter
        gols = '0'

    print(f'\n\n\t\tO jogador {nome_jogador.title()} fez {gols} gols no campeonato.\n\n')


print('__' * 17)
nome = str(input('Digite o nome do jogador: '))
gols_feitos = str(input('Digite a quantidade de gols: '))

ficha(nome_jogador=nome, gols=gols_feitos)  # Adicionando os valores informados nos parametros.
