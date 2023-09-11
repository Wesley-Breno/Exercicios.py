"""
A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos.
Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários, e
identificar os usuários com maior espaço ocupado. Através de um programa, baixado da Internet, ele conseguiu gerar o
seguinte arquivo, chamado "usuarios.txt":

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

from funcoes import converter_bytes_para_megabytes, percentual_de_uso_do_usuario  # Funcoes criadas
from tabulate import tabulate  # Funcao responsavel por tabular o resultado da analise

nome_usuarios_e_megabytes_usados = []  # Lista onde ficara o index, nome, megabytes usados e a porcentagem de uso.
soma_de_todos_os_megabytes_usados = 0
media_de_todos_os_mageabytes = 0

# Abrindo arquivo e adicionando os dados em uma lista
with open('usuarios.txt', 'r') as file:
    for index, linha in enumerate(file):
        nome_usuarios_e_megabytes_usados.append(  # Colocando o index, nome do usuario e os bytes convertidos na lista.
            [index + 1, linha.split()[0], converter_bytes_para_megabytes(int(linha.split()[1]))]
        )

# Somando todos os megabytes que foram usados
for usuario in nome_usuarios_e_megabytes_usados:
    soma_de_todos_os_megabytes_usados += usuario[2]

# Deixando o total de megabytes com apenas 2 casas decimais, colocando media dos megabytes em uma variavel
soma_de_todos_os_megabytes_usados = float(f'{soma_de_todos_os_megabytes_usados:.2f}')
media_de_todos_os_mageabytes = f'{soma_de_todos_os_megabytes_usados / len(nome_usuarios_e_megabytes_usados):.2f}'

# Pegando porcentagem de uso de cada usuario e adicionando na lista.
for index, usuario in enumerate(nome_usuarios_e_megabytes_usados):
    porcentagem_de_uso = percentual_de_uso_do_usuario(usuario[2], soma_de_todos_os_megabytes_usados)
    nome_usuarios_e_megabytes_usados[index][2] = f'{usuario[2]} MB'  # Colocando 'MB' ao lado dos megabytes usados
    nome_usuarios_e_megabytes_usados[index].append(f'{porcentagem_de_uso}%')

# Abrindo/Reescrevendo arquivo do resultado final da analise
with open('relatorio.txt', 'w+') as file:
    file.write("""ACME Inc. | Uso do espaco em disco pelos usuarios\n""")
    file.write(tabulate(  # Criando tabela com os dados analisados
        nome_usuarios_e_megabytes_usados, headers=['Nr.', 'Usuario', 'Espaco utilizado', '% de uso'], tablefmt='pretty')
    )
    file.write(f'\n\nEspaco total ocupado: {soma_de_todos_os_megabytes_usados} MB\n'
               f'Espaco medio ocupado: {media_de_todos_os_mageabytes} MB')
