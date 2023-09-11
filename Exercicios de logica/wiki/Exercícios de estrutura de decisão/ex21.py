"""
Faça um Programa para um caixa eletrônico.
O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas.
As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais.
O programa não deve se preocupar com a quantidade de notas existentes na máquina.

Exemplo 1:
Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;

Exemplo 2:
Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de
5 e quatro notas de 1.
"""

notas = [100, 50, 10, 5, 1]

while True:
    try:
        valor = int(input('Digite o valor a ser sacado: '))
    except:
        print('\n\n\033[;31mERRO\033[m\n'
              'Informe o valor que queira sacar corretamente.\n\n')
    else:
        break

if 10 <= valor <= 600:
    total_notas = {100: 0, 50: 0, 10: 0, 5: 0, 1: 0}  # Dicionario com as notas e o total que foram usadas.
    cont = 0  # Contador para trocar de nota com base no indice das notas.
    valor_clonado = 0  # Fazendo a soma das notas usadas, para ser igual ao valor informado.

    while True:
        valor_clonado += notas[cont]

        if valor_clonado > valor:  # Se passou do valor informado
            valor_clonado -= notas[cont]  # Subtraindo valor que foi somado
            cont += 1  # Trocando de nota

        else:
            total_notas[notas[cont]] += 1  # Adicionando +1 na contagem da nota que foi usada

        if valor_clonado == valor:
            break

        if cont == 5:  # Se o programa ja verificou todas as notas
            cont = 0  # Fazendo o programa verificar as notas do inicio

    print('\n\t\t[ Notas que foram sacadas ]\n')
    for nota_usada, quantidade in total_notas.items():
        if quantidade > 0:  # Se a nota foi usada.
            print(f'Notas de {nota_usada}: {quantidade}x')

else:
    print('\n\n\033[;31mERRO\033[m\n'
          'O limite de saque é de 10 a 600 reais.')
