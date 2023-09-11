"""
Faça um programa que mostre os n termos da Série a seguir:
  S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.
Imprima no final a soma da série.
"""

while True:  # Enquanto o usuario nao informar a quantidade de termos corretamente.
    print('')
    print('---' * 12)
    try:
        total_termos = int(input('Informe a quantidade de termos\nTermos: '))
    except ValueError:
        print('\n\n\t\t[\033[;31mERRO\033[m]: Por favor, informe um valor numerico corretamente.\n\n')
    else:
        break

denominador = 1
soma = 0

print('\nS = ', end='')
for numerador in range(1, total_termos + 1):  # Criando cada termo e fazendo o seu calculo
    if numerador == total_termos:  # Se for o ultimo termo
        print(f'{numerador}/{denominador}')
    else:
        print(f'{numerador}/{denominador} + ', end='')
    soma += numerador / denominador  # Somando cada termo
    denominador += 2

print(f'Soma total dos {total_termos} termos: {soma}')
