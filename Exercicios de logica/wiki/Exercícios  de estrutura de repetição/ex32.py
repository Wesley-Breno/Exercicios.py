"""
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120.
A saída deve ser conforme o exemplo abaixo:
Fatorial de: 5
5! =  5 . 4 . 3 . 2 . 1 = 120
"""

while True:  # Enquanto o usuario nao informar o valor para fazer o calculo da fatorial
    try:
        numero = int(input('Informe o um valor inteiro para ver sua fatorial\nValor inteiro: '))
    except:
        print('\n\n\t\t[\033[;31mERRO\033[m]: Por favor, informe um valor valido.\n\n')
    else:
        break

fatorial = 1  # Variavel que ira conter o resultado

print(f'\n\n\t\tFatorial de {numero}\n')

# Mostrando o calculo na tela
print(f'{numero}! = ', end='')
for c in range(numero, 0, -1):
    if c == 1:
        print(c, end='')
    else:
        print(c, end=' . ')

    fatorial *= c

print(f' = {fatorial}')  # Resultado
