"""
Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: FUSCA, GOL, VECTRA etc).
Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses carros faz com um litro
de combustível. Calcule e mostre:

O modelo do carro mais econômico;
Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000 quilômetros e
quanto isto custará, considerando um que a gasolina custe R$ 2,25 o litro. Abaixo segue uma tela de exemplo. O
disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada
execução do programa.

Comparativo de Consumo de Combustível

Veículo 1
Nome: fusca
Km por litro: 7
Veículo 2
Nome: gol
Km por litro: 10
Veículo 3
Nome: uno
Km por litro: 12.5
Veículo 4
Nome: Vectra
Km por litro: 9
Veículo 5
Nome: Peugeout
Km por litro: 14.5

Relatório Final
 1 - fusca           -    7.0 -  142.9 litros - R$ 321.43
 2 - gol             -   10.0 -  100.0 litros - R$ 225.00
 3 - uno             -   12.5 -   80.0 litros - R$ 180.00
 4 - vectra          -    9.0 -  111.1 litros - R$ 250.00
 5 - peugeout        -   14.5 -   69.0 litros - R$ 155.17
O menor consumo é do peugeout.
"""

from tabulate import tabulate  # Função que sera responsavel por fazer uma tabela com os dados

carros = []
kms_por_litro = []
contador_carros = 0
nome_carro_mais_economico = ''

# Enquanto o usuario nao informar os dados dos 5 carros
while contador_carros != 5:
    try:  # Tentando pegar o nome do carro e os kms que ele faz por litro
        nome_carro = str(input(f'Veículo {contador_carros + 1}\n'
                               f'Nome: ')).title()
        km_carro = float(input('Kms por litro: '))
        print()

    except ValueError:  # Se o usuario nao informou corretamente os dados
        print('\n\n\t\t[ERRO]: Por favor, informe corretamente os dados do carro.\n\n')

    else:  # Se o usuario informou corretamente os dados do carro
        carros.append([nome_carro, km_carro, f'{1000 / km_carro:.1f} litros', f'R$ {(1000 / km_carro) * 2.25:.2f}'])
        contador_carros += 1

# Mostrando tabela com o nome do carro, kms por litro, gasolina gasta em 1000km, total gasto em 1000km rodados
print('\n\t\t\tRelatorio final\n')
print(tabulate(carros, headers=['Carro', 'Km p/ litro', 'Gasolina gasta em 1000Km', 'Total gasto'], tablefmt='pretty'))

# Pegando cada kms por litro de cada carro e mostrando na tela o carro mais economico
for carro in carros:
    kms_por_litro.append(carro[1])

carro_mais_economico = max(kms_por_litro)

for carro in carros:
    if carro[1] == carro_mais_economico:
        nome_carro_mais_economico = carro[0]

print(f'O carro com o menor consumo é o {nome_carro_mais_economico}')
