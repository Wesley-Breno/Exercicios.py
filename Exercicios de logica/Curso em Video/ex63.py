"""
Escreva um programa que leia um número N inteiro qualquer
e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.

Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8
"""
while True:  # Enquanto o usuario nao digitar um numero para mostrar a sequencia.
    try:
        termos = int(input('Quantos elementos deseja ver?  '))

    except:
        print('\n\t\tERRO, Por favor, digite um numero valido.\n')

    else:
        t1 = 0  # Primeiro elemento da sequencia
        t2 = 1  # Segundo elemento da sequencia
        print(f'\n\t\t{termos} elementos de uma sequencia Fibonacci\n\n', t1, t2, end=' ')
        for c in range(0, termos - 2):
            t3 = t1 + t2  # Somando o valor do primeiro e segundo elemento para ter o resultado
            print(t3, end=' ')
            t1 = t2  # Primeiro elemento vai pegar o valor do segundo elemento
            t2 = t3  # Segundo elemento vai pegar o valor do terceiro elemento

        break

