"""
A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,...
Faça um programa que gere a série até que o valor seja maior que 500.
"""

# Variaveis que serao usadas para fazer a sequencia fibonacci
n1 = 1
n2 = n1
n3 = n2

print('\n\n\t\tSequencia de Fibonacci\n')

print(n3, n3, end=' ')
while n3 < 500:  # Enquanto o valor nao for maior ou igual a 500
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end=' ')

