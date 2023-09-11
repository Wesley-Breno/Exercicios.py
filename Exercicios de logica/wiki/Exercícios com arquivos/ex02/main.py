"""
A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos. Para
tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários, e identificar
os usuários com maior espaço ocupado. Através de um programa, baixado da Internet, ele conseguiu gerar o seguinte
arquivo, chamado "usuarios.txt":

    alexandre       456123789
    anderson        1245698456
    antonio         123456456
    carlos          91257581
    cesar           987458
    rosemary        789456125

Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo, você deve criar um programa que gere um
relatório, chamado "relatório.txt", no seguinte formato:

ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso

1    alexandre       434,99 MB             16,85%
2    anderson       1187,99 MB             46,02%
3    antonio         117,73 MB              4,56%
4    carlos           87,03 MB              3,37%
5    cesar             0,94 MB              0,04%
6    rosemary        752,88 MB             29,16%

Espaço total ocupado: 2581,57 MB
Espaço médio ocupado: 430,26 MB

O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso sejam necessários, de forma a
agilizar a execução do programa. A conversão da espaço ocupado em disco, de bytes para megabytes deverá ser feita
através de uma função separada, que será chamada pelo programa principal. O cálculo do percentual de uso também deverá
ser feito através de uma função, que será chamada pelo programa principal.
"""

from utils import converte_bytes_pra_megabytes, pega_porcentagem_de_uso_do_usuario
from tabulate import tabulate  # Funcao usada para escrever no arquivo em forma de tabela

# Abrindo arquivo com o nome e bytes dos usuarios e separando esses dados para analise
with open('usuarios.txt', 'r', encoding='utf-8') as file:
    dados = file.readlines()

    usuarios = []  # Lista onde ira conter os nomes dos usuarios
    megabytes_usuarios = []  # Lista onde ira conter os bytes dos usuarios convertidos para megabytes

    # Pegando nomes de usuarios e convertendo os bytes para megabytes e colocando cada dado em sua lista
    for dado in dados:
        usuarios.append(dado.split(' ')[0])
        megabytes_usuarios.append(
            converte_bytes_pra_megabytes(
                int(dado.split(' ')[-1].replace('\n', '')))  # Pegando bytes usados do usuario e enviando para converter
        )

# Fazendo analise de porcentagem de uso de cada usuario e colocando em uma lista
porcentagem_de_uso_usuarios = []
for megabyte in megabytes_usuarios:
    porcentagem_de_uso_usuarios.append(pega_porcentagem_de_uso_do_usuario(megabytes_usuarios, megabyte))

# Adicionando os dados de cada usuario em uma unica lista para poder fazer uma tabela com a funcao
dados = []
for index in range(0, len(usuarios) - 1):
    dados.append([index + 1, usuarios[index],
                  f'{megabytes_usuarios[index]:.2f} MB',
                  f'{porcentagem_de_uso_usuarios[index]:.2f}%'])


# Escrevendo relatorio no formato de tabela
with open('relatorio.txt', 'w+', encoding='utf-8') as file:
    file.write("""ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------\n""")
    file.write(tabulate(dados, headers=['Nr.', 'Usuário', 'Espaço utilizado', '% do uso\n'], colalign='left', tablefmt='plain'))
    file.write(f'\n\nEspaco total ocupado: {sum(megabytes_usuarios):.2f}MB\n'
               f'Espaco medio ocupado: {sum(megabytes_usuarios) / len(megabytes_usuarios):.2f}MB')
    