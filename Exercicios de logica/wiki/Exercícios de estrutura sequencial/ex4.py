"""
Faça um Programa que peça as 4 notas bimestrais e mostre a média.
"""

notas = []  # Variavel onde ficarao as notas

while True:  # Enquanto o usuario nao digitar todas as 4 notas
    for c in range(4):
        try:  # Tentando pegar nota
            notas.append(float(input(f'Digite a {c + 1}º nota do aluno: ')))
        except:  # Mostrando um erro na tela e esvaziando lista com notas
            print('\033[;31mDIGITE UM VALOR NUMERICO\033[m')
            notas = []
            break

    if len(notas) == 4:  # Se o usuario digitou todas as 4 notas.
        break

print(f'A media do aluno é {sum(notas) / len(notas)}')
