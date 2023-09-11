"""
Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999,
que é a condição de parada. No final, mostre quantos números
foram digitados e qual foi a soma entre eles (desconsiderando o flag).
"""

lista_numeros = []  # Lista onde ficara cada numero digitado pelo usuario.
print('\033[;37m\n\t\tDigite numeros para fazer a soma entre eles\n\t\tDigite [ 999 ] para parar e mostrar a soma.'
      '\n\033[m')

while True:  # enquanto o usuario quiser adicionar numeros
    try:
        numero = int(input('> '))

    except:
        print('\n\t\t\033[;31mERRO\033[m, por favor, digite um numero inteiro.\n')

    else:
        if numero == 999:  # Se o usuario nao quiser mais adicionar numeros
            break

        lista_numeros.append(numero)  # Adicionando o numero digitado

print(f'\n\t\tVoce digitou o total de \033[;1m{len(lista_numeros)}\033[m valores'  # Mostrando a quantidade de valores
      f'\n\t\tA soma entre eles equivale a: \033[;1m{sum(lista_numeros)}\033[m\n')  # Mostrando a soma entre eles
