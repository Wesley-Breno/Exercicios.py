"""
Faça um programa que leia um número qualquer e mostre o seu fatorial.
Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
"""
numero = None
while type(numero) != int:  # Enquanto o usuario nao digitar um numero inteiro
    print('__' * 20)
    try:
        numero = int(input('Informe um numero para ver sua fatorial\nNumero: '))
    except:
        print('\n\n\033[;31mERRO\033[m\nPor favor, tente novamente.\n\n')

print(f'\n\t\tFatorial de {numero}\n')

fatorial = 1  # Variavel da fatorial onde ficara armazenado o resultado
print(f'{numero}! = ', end='')
for contagem in range(numero, 0, -1):  # Contagem do numero colocado ate 1.

    if contagem == 1:
        print(f'{contagem}', end=' = ')

    else:
        print(f'{contagem} x ', end='')

    fatorial *= contagem  # Fazendo a multiplicacao de cada numero para pegar o resultado

print(fatorial)
