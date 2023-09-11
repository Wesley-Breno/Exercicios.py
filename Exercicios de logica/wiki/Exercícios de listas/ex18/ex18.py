"""
Uma grande emissora de televisão quer fazer uma enquete entre os seus telespectadores para saber qual o melhor jogador
após cada jogo. Para isto, faz-se necessário o desenvolvimento de um programa, que será utilizado pelas telefonistas,
para a computação dos votos. Sua equipe foi contratada para desenvolver este programa, utilizando a linguagem de
programação C++. Para computar cada voto, a telefonista digitará um número, entre 1 e 23, correspondente ao número da
camisa do jogador. Um número de jogador igual zero, indica que a votação foi encerrada. Se um número inválido for
digitado, o programa deve ignorá-lo, mostrando uma breve mensagem de aviso, e voltando a pedir outro número. Após o
final da votação, o programa deverá exibir:

→ O total de votos computados;
→ Os númeos e respectivos votos de todos os jogadores que receberam votos;
→ O percentual de votos de cada um destes jogadores;

→ O número do jogador escolhido como o melhor jogador da partida, juntamente com o número de votos e o percentual de
votos dados a ele.

→ Observe que os votos inválidos e o zero final não devem ser computados como votos. O resultado aparece ordenado pelo
número do jogador. O programa deve fazer uso de arrays. O programa deverá executar o cálculo do percentual de cada
jogador através de uma função. Esta função receberá dois parâmetros: o número de votos de um jogador e o total de votos.
A função calculará o percentual e retornará o valor calculado. Abaixo segue uma tela de exemplo. O disposição das
informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada execução do
programa. Ao final, o programa deve ainda gravar os dados referentes ao resultado da votação em um arquivo texto no
disco, obedecendo a mesma disposição apresentada na tela.

Enquete: Quem foi o melhor jogador?

Número do jogador (0=fim): 9
Número do jogador (0=fim): 10
Número do jogador (0=fim): 9
Número do jogador (0=fim): 10
Número do jogador (0=fim): 11
Número do jogador (0=fim): 10
Número do jogador (0=fim): 50
Informe um valor entre 1 e 23 ou 0 para sair!
Número do jogador (0=fim): 9
Número do jogador (0=fim): 9
Número do jogador (0=fim): 0

Resultado da votação:

Foram computados 8 votos.

Jogador Votos           %
9               4               50,0%
10              3               37,5%
11              1               12,5%
O melhor jogador foi o número 9, com 4 votos, correspondendo a 50% do total de votos.
"""

jogadores = []
total_votos_feitos = 0


def retorna_porcentagem_de_votos(votos_atleta, total_votos):
    """
    Funcao que ira calcular os votos recebidos do atleta e o total de votos e retornar a porcentagem de votos que o
    atleta tem.
    :param votos_atleta: Votos que o atleta recebeu
    :param total_votos: Total de votos que foram feitos
    :return: Retorno da porcentagem de votos que o atleta tem
    """
    return votos_atleta / total_votos * 100


print('\n\nEnquente: Quem foi o melhor jogador?\n')

while True:  # Enquanto o usuario nao digitar 0 para encerrar a votacao.
    try:
        jogador = int(input('Número do jogador (0=fim): '))

    except ValueError:
        print('Informe um valor entre 1 e 23 ou 0 para sair!')

    else:
        if jogador == 0:
            break

        if jogador > 23 or jogador < 0:  # Se o usuario informou um valor invalido
            print('Informe um valor entre 1 e 23 ou 0 para sair!')
        else:
            if len(jogadores) > 0:  # Se o usuario ja informou os votos de algum jogador
                tem = False  # Variavel para saber se o jogador ja existe na lista
                for atleta in jogadores:
                    for chave, dados in atleta.items():
                        if dados[0] == jogador:
                            dados[1] += 1  # Somando +1 nos votos do jogador
                            tem = True  # Informando que o usuario existe na lista
                if tem is False:
                    jogadores.append({'jogador': [jogador, 1]})
            else:
                jogadores.append({'jogador': [jogador, 1]})

            total_votos_feitos += 1

for atleta in jogadores:
    for chave, dados in atleta.items():
        porcentagem = retorna_porcentagem_de_votos(dados[1], total_votos_feitos)
        dados.append(porcentagem)

jogadores = sorted(jogadores, key=lambda x: x['jogador'][0])  # Ordenando lista pelo numero da camisa do jogador

print(f"""
Resultado da votacao:

Foram computados {total_votos_feitos} votos.

Jogador\t\tVotos\t\t%""")

porcentagens = []  # Lista que ira conter todas as porcentagens dos jogadores para saber qual tem a maior porcentagem
atleta_com_maior_voto = []
maior_porcentagem_de_votos = 0

for atleta in jogadores:
    for chave, dado in atleta.items():
        porcentagens.append(dado[2])
        print(f'{dado[0]}\t\t\t{dado[1]}\t\t\t{dado[2]:.1f}%')

maior_porcentagem_de_votos = max(porcentagens)

for atleta in jogadores:
    for chave, dado in atleta.items():
        if dado[2] == maior_porcentagem_de_votos:
            atleta_com_maior_voto.append([dado[0], dado[1], dado[2]])

if len(atleta_com_maior_voto) > 1:  # Se tiver mais de 1 atleta com a maior porcentagem de votos
    print('Não houve um atleta com a maior porcentagem de votos')
else:
    print(f'O melhor jogador foi o número {atleta_com_maior_voto[0][0]}, com {atleta_com_maior_voto[0][1]} votos, '
          f'correspondendo a {atleta_com_maior_voto[0][2]:.1f}% do total de votos.')

with open('dados.txt', 'w+') as file:  # Criando um arquivo de texto com o resultado da votacao
    file.writelines(f'Foram computados {total_votos_feitos} votos.\n')
    file.writelines('Jogador\t\t\tVotos\t\t\t%\n')

    for atleta in jogadores:
        for chave, dado in atleta.items():
            file.writelines(f'{dado[0]}\t\t\t\t{dado[1]}\t\t\t\t{dado[2]:.1f}%\n')

    if len(atleta_com_maior_voto) > 1:
        file.writelines('Não houve um atleta com a maior porcentagem de votos')
    else:
        file.writelines(f'O melhor jogador foi o número {atleta_com_maior_voto[0][0]} com {atleta_com_maior_voto[0][1]}'
                        f' votos, correspondendo a {atleta_com_maior_voto[0][2]:.1f}% do total de votos.')
