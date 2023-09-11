"""
Nome na vertical.
Faça um programa que solicite o nome do usuário e imprima-o na vertical.

F
U
L
A
N
O
"""

nome_usuario = str(input('Informe o seu nome: '))  # Recebendo nome do usuario

print('\n\t\tNome na vertical\n')
for letra in nome_usuario:  # Mosntrando cada letra do nome por linha
    print(letra)
