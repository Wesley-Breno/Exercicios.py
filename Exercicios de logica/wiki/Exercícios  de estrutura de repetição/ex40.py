"""
Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os
seguintes dados:

Código da cidade;
Número de veículos de passeio (em 1999);
Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
Qual a média de veículos nas cinco cidades juntas;
Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.
"""

cont = 1  # Contador para saber quantas cidades ja foram informadas.
cidades = []

while True:  # Enquanto o usuario nao informar os dados das 5 cidades corretamente.
    if cont == 6:  # Se o usuario ja informou as 5 cidades
        break

    cidade = dict()

    print()
    try:
        cidade['cidade'] = int(input(f'Informe o codigo da {cont}º cidade: '))
        cidade['v_passeios'] = int(input('Informe a quantidade de veiculos de passeioe em 1999: '))
        cidade['acidentes'] = int(input('Informe o numero de acidentes de transito com vitimas: '))

    except:
        print('\n\n\t\t[\033[;31mERRO\033[m]: Verifique os dados preenchidos e tente novamente.\n\n')

    else:
        cont += 1
        cidades.append(cidade)


acidentes = []  # Contera todos os valores de acidentes para ver qual cidade tem mais acidadentes e menor acidentes
veiculos = []  # Contera a quantidade de veiculos, para poder saber a media de veiculos das 5 cidades juntas
acidentes_menor_que_2000_veiculos = []  # Contera a quantidade de acidentes onde a cidade tem menos de 2000 veiculos

for city in cidades:
    acidentes.append(city['acidentes'])
    veiculos.append(city['v_passeios'])

    if city['v_passeios'] < 2000:
        acidentes_menor_que_2000_veiculos.append(city['acidentes'])

# Media de acidentes de cidades que tem menos de 2000 veiculos
media_acidentes = sum(acidentes_menor_que_2000_veiculos) / len(acidentes_menor_que_2000_veiculos)
media_veiculos = sum(veiculos) / len(cidades)  # Media de veiculos das 5 cidades juntas

for city in cidades:
    if city['acidentes'] == max(acidentes):
        maior_indice = city['cidade'], city['acidentes']  # Cidade com maior indice de acidentes

    if city['acidentes'] == min(acidentes):
        menor_indice = city['cidade'], city['acidentes']  # Cidade com menor indice de acidentes

print(f'''\n\n\t\tResultado

> Cidade com maior indice de acidentes
    C. da cidade: {maior_indice[0]}
    T. acidentes: {maior_indice[1]}
    
> Cidade com menor indice de acidentes
    C. da cidade: {menor_indice[0]}
    T. acidentes: {menor_indice[1]}

> Media de veiculos das 5 cidades juntas
    Media: {media_veiculos:.1f}

> Media de acidentes de transito com cidades 
com menos de 2000 veiculos de passeio
    Media: {media_acidentes:.1f}''')
