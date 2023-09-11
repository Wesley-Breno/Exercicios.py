"""
Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a
idade e a altura na ordem inversa a ordem lida.
"""

pessoas = []  # Lista onde ficara a idade e a altura de cada pessoa
pessoa = []  # Lista onde ficara a idade e a altura

while True:  # Enquanto o usuario nao informar corretamente a idade e a altura de cada pessoa
    try:
        for c in range(5):
            print()
            print('--' * 15)
            pessoa.append(int(input(f'Informe a idade da {c + 1}º pessoa\nIdade: ')))
            pessoa.append(float(input(f'Informe a altura da {c + 1}º pessoa\nAltura: ')))

            pessoas.append(pessoa)
            pessoa = []

    except ValueError:  # Se o usuario informou um valor invalido
        print('\n\n\t\t[\033[;31mERRO\033[m]: Por favor informe corretamente os dados das pessoas.\n\n')
        pessoa = []
        pessoas = []

    else:  # Se o usuario informou corretamente os dados das 5 pessoas
        break

print('\n\t\tRESULTADO\n')

for c in range(len(pessoas) - 1, -1, -1):  # Imprimindo os dados de cada pessoa em ordem inversa
    print('--' * 15)
    print(f'\t\t[ {c + 1}º Pessoa ]\n'
          f'Idade: {pessoas[c][0]}\n'
          f'Altura: {pessoas[c][1]}')
