"""
Nome ao contrário em maiúsculas.
Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o nome do usuário de trás para frente
utilizando somente letras maiúsculas. Dica: lembre−se que ao informar o nome o usuário pode digitar letras maiúsculas ou
minúsculas.
"""

nome_usuario = str(input('Digite o seu nome: ')).upper()  # Recebendo nome do usuario

print(f'Nome invertido: ', end='')

# Mostrando cada caractere do nome invertido pelo indice
for c in range(len(nome_usuario) - 1, -1, -1):
    print(nome_usuario[c], end='')
