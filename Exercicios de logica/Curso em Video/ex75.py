"""
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os
em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
"""

quantas_vezes_apareceu_9 = 0
posicao_do_num3 = None
numeros_pares_digitados = None

print('\n' * 2)
print('__' * 12)
valores = tuple(str(input(f'Informe o {c + 1}° valor: ')) for c, n in enumerate(range(4)))

cont = 0
for numero in valores:  # Contando se foram digitados os 4 numeros inteiros pedidos.
    if numero.isdigit():  # Se 'numero' for um numero.
        cont += 1

if cont == 4:  # Se todos os valores digitados sao numeros.

    for indice, numero in enumerate(valores):
        if numero == '9':
            quantas_vezes_apareceu_9 += 1

        if numero == '3':
            posicao_do_num3 = indice

        if int(numero) % 2 == 0:
            numeros_pares_digitados = list()
            numeros_pares_digitados.append(numero)

    print('--' * 26)
    print(f"""\n\n\t\t\033[;37mResultado\033[m\n
* Quantas vezes apareceu o numero 9: {quantas_vezes_apareceu_9}x
* Posicao do numero 3: \033[;31m{f'{posicao_do_num3 + 1}º' if posicao_do_num3 is not None else
    'Numero 3 nao foi digitado'}\033[m 
* Numeros pares que foram digitados: \033[;31m{numeros_pares_digitados if numeros_pares_digitados is not None else 
    'Nenhum valor par foi digitado.'}\033[m""")
    print('--' * 26)

else:
    print('\n\n\t\t[\033[;31mERRO\033[m]: Digite 4 numeros inteiros.\n\n')
