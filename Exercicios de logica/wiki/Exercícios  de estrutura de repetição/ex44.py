"""
Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados
são:

1 , 2, 3, 4  - Votos para os respectivos candidatos
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco

Faça um programa que calcule e mostre:
O total de votos para cada candidato;
O total de votos nulos;
O total de votos em branco;
A percentagem de votos nulos sobre o total de votos;
A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.
"""

# Dicionario com o codigo do candidato e sua quantidade de votos
candidatos = {1: 0,
              2: 0,
              3: 0,
              4: 0,
              5: 0,
              6: 0}

print('\n\n\t\t\033[;37m[ Digite um valor negativo para encerrar votação ]\033[m')

while True:  # Enquanto o usuario nao informar um numero negativo
    try:
        print('--' * 23)
        voto = int(input("""\tInforme o codigo em quem deseja votar
[ 1 ] - Jose
[ 2 ] - Augusto
[ 3 ] - Cesar
[ 4 ] - Mario
[ 5 ] - Voto nulo
[ 6 ] - Voto em branco

| Voto: """))
        print('--' * 23)

    except ValueError:  # Se o usuario nao digitou um numero
        input('\n\n\t[\033[;31mERRO\033[m]: Informe o codigo que representa em quem voce quer votar.\n'
              '\t\t\t\tPressione ENTER para continuar\n')

    else:
        if voto < 0:  # Se o usuario decidiu encerrar a votação
            break

        try:
            candidatos[voto] += 1

        except KeyError:  # Se o usuario informou um numero que nao corresponde a um candidato
            input('\n\n\t\t[\033[;31mERRO\033[m]: Candidato não encontrado\n'
                  '\t\t Pressione ENTER para continuar\n')

total_votos = candidatos[1] + candidatos[2] + candidatos[3] + candidatos[4] + candidatos[5] + candidatos[6]

print(f"""
\t\tResultado da eleição

Nome do candidato | Codigo | Total de votos
Jose                  1           {candidatos[1]}
Augusto               2           {candidatos[2]}
Cesar                 3           {candidatos[3]}
Mario                 4           {candidatos[4]}
Votos nulos           5           {candidatos[5]}
V. em branco          6           {candidatos[6]}

Porcentagem de votos nulos: {(candidatos[5]/total_votos) * 100:.1f}%
Porcentagem de votos em branco: {(candidatos[6]/total_votos) * 100:.1f}%
""")
