"""
Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10.
O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
Tabuada de 5:
5 X 1 = 5
5 X 2 = 10
...
5 X 10 = 50
"""

while True:  # Enquanto o usuario nao informar corretamente o numero
    try:
        numero = int(input('\nInforme o numero que deseja ver a sua tabuada\nNumero: '))
    except:
        print('\n\n\t\t[\033[;31mERRO\033[m]: Por favor, informe o numero corretamente.\n\n')
    else:
        if 0 < numero < 11:  # Se o numero informado estiver entre 1 e 10
            break
        else:
            print('\n\n\t\t[\033[;31mERRO\033[m]: Por favor, informe um numero entre 1 e 10.\n\n')

print(f'\n\n\t\tTabuada do numero {numero}\n')
for c in range(1, 11):
    print(f'{numero} x {c} = {numero * c}')
