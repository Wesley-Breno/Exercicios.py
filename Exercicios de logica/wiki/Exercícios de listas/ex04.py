"""
Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
"""

vetor = []  # Lista onde ficara todas as letras informadas
consoantes = []  # Lista onde ficara apenas as consoantes que foram informadas

while True:  # Enquanto o usuario nao informar as 10 letras do vetor.
    try:
        for c in range(10):  # Adicionando os 10 caracteres no vetor
            dado = str(input(f'Informe a {c + 1}º letra do vetor: '))

            if dado.isalpha() and dado != '':  # Se o dado que o usuario informou for uma letra
                vetor.append(dado)
            else:
                print('\n\n\t\t[\033[;31mERRO\033[m]: Por favor, informe os valores do vetor corretamente.\n\n')
                vetor = []
                break

    except ValueError:
        print('\n\n\t\t[\033[;31mERRO\033[m]: Por favor, informe os valores do vetor corretamente.\n\n')
        vetor = []

    else:
        if len(vetor) == 10:  # Se o usuario informou os 10 caracteres corretamente
            break

for letra in vetor:  # Verificando as consoantes que estao no vetor
    if letra in 'bcdfgjklmnpqrstvwxz':
        consoantes.append(letra)

print('\n\n\t\tResultado\n'
      f'Total de consoantes: {len(consoantes)}\n'
      f'Consoantes informadas: {consoantes}')
