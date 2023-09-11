"""
Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores.
Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.
"""

votos = []  # Lista onde ficara cada voto
candidato_a = 0  # Total de votos dos candidatos
candidato_b = 0
candidato_c = 0

while True:  # Enquanto o usuario nao informar quantos eleitores irao votar.
    try:
        eleitores = int(input('\nDigite o numero total de eleitores que irão votar\nTot. eleitores: '))
    except:
        print('\n\n\t\t[\033[;31mERRO\033[m]: Informe quantos eleitores irão votar\n\n')
    else:
        break

cont = 1  # Contador para informar qual candidato esta votando

while eleitores != 0:  # Enquanto todos os eleitores nao votarem
    print()
    print('__' * 25)
    print('Digite o numero que corresponde ao candidato')
    try:
        voto = int(input(f'\t\t[ voto do {cont}º eleitor ]\n\n'
                         f'[ 1 ] - Candidato A\n'
                         f'[ 2 ] - Candidato B\n'
                         f'[ 3 ] - Candidato C\n\n'
                         f'Candidato escolhido: '))
    except:
        print('\n\n\t\t[\033[;31mERRO\033[m]: Digite apenas o numero que corresponde ao candidato escolhido.\n\n')

    else:
        if voto == 1 or voto == 2 or voto == 3:  # Se o usuario votou em um dos tres candidatos
            votos.append(voto)
            eleitores -= 1  # Menos usuarios para votar
            cont += 1  # Contando quantos usuarios ja votaram

        else:
            print('\n\n\t\t[\033[;31mERRO\033[m]: Digite apenas o numero que corresponde ao candidato escolhido.\n\n')

for voto in votos:  # Colocando cada voto que corresponde a um candidato em sua variavel
    if voto == 1:
        candidato_a += 1

    elif voto == 2:
        candidato_b += 1

    else:
        candidato_c += 1

print('\n\n\t\tResultado das eleições\n\n'
      f'Candidato A: {candidato_a} votos\n'
      f'Candidato B: {candidato_b} votos\n'
      f'Candidato C: {candidato_c} votos\n')
