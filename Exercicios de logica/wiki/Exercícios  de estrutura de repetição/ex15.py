"""
A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
Faça um programa capaz de gerar a série até o n−ésimo termo.
"""

while True:  # Enquanto o usuario nao informar o n-ésimo
    try:
        nesimo = int(input('\nInforme o n-ésimo termo da sequencia fibonacci\nn-ésimo termo: '))
    except:
        print('\n\n\t\t[\033[;31mERRO\033[m]: Por favor, informe o n-ésimo termo da sequencia.\n\n')
    else:
        break

# Variaveis que serao usadas para fazer a sequencia fibonacci
n1 = 1
n2 = n1
n3 = n2

print('\n\n\t\tSequencia de Fibonacci\n')

if nesimo == 1:  # Se o usuario so quer ver 1 termo
    print(1)

else:
    for c in range(nesimo - 1):
        if c == 0:  # Se estiver no primeiro termo
            print('1, ', end='')

        if c == nesimo - 2:  # Se estiver no ultimo termo
            print(n3)
            n3 = n1 + n2
            n1 = n2
            n2 = n3

        else:
            print(n3, end=', ')
            n3 = n1 + n2
            n1 = n2
            n2 = n3
