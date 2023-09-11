"""
Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações:
"Qual o melhor Sistema Operacional para uso em servidores?"

As possíveis respostas são:

1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro

Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da
mesma. O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. Não deverão ser
aceitos valores além dos válidos para o programa (0 a 6). Os valores referentes a cada uma das opções devem ser
armazenados num vetor. Após os dados terem sido completamente informados, o programa deverá calcular a percentual de
cada um dos concorrentes e informar o vencedor da enquete. O formato da saída foi dado pela empresa, e é o seguinte:

Sistema Operacional     Votos   %
-------------------     -----   ---
Windows Server           1500   17%
Unix                     3500   40%
Linux                    3000   34%
Netware                   500    5%
Mac OS                    150    2%
Outro                     150    2%
-------------------     -----
Total                    8800

O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.
"""

from tabulate import tabulate  # Funcao que ira tabular os dados

votos = [['Windows Server', 0], ['Unix', 0], ['Linux', 0], ['Netware', 0], ['Mac OS', 0], ['Outro', 0]]
porcentagens = []  # Lista onde ficara as porcentagens de cada SO para compara-los
recebeu_mais_votos = []
total_de_votos = 0

while True:  # Enquanto o usuario nao digitar 0 para encerrar a votacao
    try:
        print()
        print('--' * 35)
        voto = int(input('''Digite o numero que corresponde a qual sistema OS voce deseja votar:
[ 1 ] - Windows Server
[ 2 ] - Unix
[ 3 ] - Linux
[ 4 ] - Netware
[ 5 ] - Mac OS
[ 6 ] - Outro
[ 0 ] - Encerrar votacao

Voto: '''))

    except ValueError:
        print('\n\n\t\t[\033[;31mERRO\033[m]: Informe o numero que corresponde ao sistema OS que deseja votar.\n')

    else:
        if voto == 0:
            break

        if 0 < voto <= 6:  # Se o voto do usuario estiver entre 0 e 6
            votos[voto - 1][1] += 1  # Adicionando +1 voto ao SO escolhido
            total_de_votos += 1

        else:
            print('\n\n\t\t[\033[;31mERRO\033[m]: Informe o numero que corresponde ao sistema OS que deseja votar.\n')

# Pegando porcentagem de votos de cada SO e adicionando a porcentagem na lista principal e na lista de porcentagens
for index, votos_feitos in enumerate(votos):
    porcentagem = votos_feitos[1] / total_de_votos * 100
    votos[index].append(int(porcentagem))
    porcentagens.append(int(porcentagem))

# Comparando as porcentagens e vendo qual porcentagem é maior e adicionando na lista de mais votados
for index, porcentagem_calculada in enumerate(votos):
    if porcentagem_calculada[2] == max(porcentagens):  # Se for a maior porcentagem
        recebeu_mais_votos.append(porcentagem_calculada[:])  # Adicionando dados do SO

print()
print(tabulate(votos, headers=['Sistema Operacional', 'Votos', '%']))  # Fazendo tabela com os dados dos SO
print('--' * 18)
print(f'Total de votos\t\t\t{total_de_votos}\n')

if len(recebeu_mais_votos) > 1:  # Se tiver mais de 1 SO com a maior porcentagem
    print('Houve empate nas votacoes!!!')

else:
    print(f'O Sistema Operacional mais votado foi o {recebeu_mais_votos[0][0]}, com {recebeu_mais_votos[0][1]} votos, '
          f'correspondendo a {recebeu_mais_votos[0][2]}% dos votos.')
