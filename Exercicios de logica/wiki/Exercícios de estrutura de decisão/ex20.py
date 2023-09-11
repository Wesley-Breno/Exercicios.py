"""
Faça um Programa para leitura de três notas parciais de um aluno.
O programa deve calcular a média alcançada por aluno e presentar:

A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
A mensagem "Aprovado com Distinção", se a média for igual a 10.
"""

notas = []  # Lista onde ficara as notas do aluno

while True:  # Enquanto o usuario nao digitar as notas corretamente
    for c in range(3):
        try:
            notas.append(float(input(f'Digite a {c + 1}º nota: ')))
        except:
            print('\n\n\t\tInforme as notas corretamente\n')
            notas.clear()

    if len(notas) == 3:  # Se o usuario informou as notas
        media = sum(notas) / len(notas)  # Media do aluno

        print('\nSituação: ', end='')

        if media < 7:  # Reprovado
            print('\033[;31mReprovado\033[m')

        elif media == 10:  # Aprovado com distinção
            print('\033[;32mAprovado com distinção\033[m')

        elif media >= 7:  # Apenas aprovado
            print('\033[;32mAprovado\033[m')

        break
