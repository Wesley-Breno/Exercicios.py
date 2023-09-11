"""
Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões. O vendedor
recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um vendedor que teve vendas
brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470. Escreva um programa
(usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de valores:

$200 - $299
$300 - $399
$400 - $499
$500 - $599
$600 - $699
$700 - $799
$800 - $899
$900 - $999
$1000 em diante

Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados.
"""

cont = 1  # Contador para mostrar em qual funcionario esta informando os dados
vendas = [0] * 9  # Lista onde ficara a quantidade de funcionarios que recebem um intervalo especifico de valor
valores = ['$200 - $299', '$300 - $399', '$400 - $499',
           '$500 - $599', '$600 - $699', '$700 - $799',
           '$800 - $899', '$900 - $999', '$1000 em diante']

print('\n\n\t\t\033[;37mDigite um valor menor que zero para encerrar\033[m\n\n')

while True:  # Enquanto o usuario nao digitar um valor menor que 0
    try:
        venda_bruta = float(input(f'Informe o valor da venda bruta do {cont}º vendedor\nVenda bruta: R$ '))
        if venda_bruta < 0:
            break

    except ValueError:
        print(f'\n\n\t\t[\033[;31mERRO\033[m]: Informe o valor da venda bruta do {cont}º vendedor corretamente.\n\n')

    else:
        cont += 1

        salario = ((venda_bruta * 9 / 100) + 200)  # Salario total com os 9% da venda bruta
        posicao = int(((salario // 100) - 2))  # Pegando a divisao inteira do salario para usar como posicao da lista

        if posicao >= 0:
            if posicao > 8:  # Se o salario for maior que 1000
                posicao = 8  # Colocando a posicao no ultimo dado da lista
            vendas[posicao] += 1  # Somando a quantidade de funcionarios que se enquadra em quantia X

print('\n\nQuantidade de funcionarios que receberam o equivalente a...')
for index, valor in enumerate(valores):
    print(f'{valor} = {vendas[index]} funcionario(s)')
