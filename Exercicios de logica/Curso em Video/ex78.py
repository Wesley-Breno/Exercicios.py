"""
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas
respectivas posições na lista.
"""

valores = []

while True:  # Enquanto o usuario nao digitar 5 valores inteiros
    print('__' * 15)
    for c in range(5):
        valor = str(input(f'Informe o {c + 1}º valor: '))

        if valor.isdigit():  # Se o valor digitado for um numero
            valores.append(valor)

        else:  # Se o valor digitado nao for um numero, limpa a lista e reinicia o for.
            print('\n\n\t\t[\033[;31mERRO\033[m]: Por favor, insira os valores numericos novamente.\n\n')
            valores.clear()
            break

    if len(valores) == 5:  # Se o usuario digitou os 5 valores corretamente
        break

for indice, numero in enumerate(valores):  # Pegando cada numero e seu indice
    if indice == 0:  # Se for o primeiro numero da lista
        maior = (indice + 1), numero
        menor = (indice + 1), numero
    else:
        if int(numero) > int(maior[1]):  # Se o numero da vez for maior que o maior valor ja visto
            maior = (indice + 1), numero

        if int(numero) < int(menor[1]):  # Se o numero da vez for menor que o menor valor ja visto
            menor = (indice + 1), numero

print('\n')
print('--' * 15)
print(f"""Maior valor: {maior[1]}
Posicao: {maior[0]}
--------------------------
Menor valor: {menor[1]}
Posicao: {menor[0]}""")
print('--' * 15)
