"""
Crie um programa onde o usuário possa digitar cinco valores numéricos
e cadastre-os em uma lista, já na posição correta de inserção
(sem usar o sort()). No final, mostre a lista ordenada na tela.
"""

lista = []  # Lista onde ficara os valores em ordem

for c in range(5):  # Fazendo um for para pegar os 5 valores
    numero = int(input('Digite o valor: '))

    if c == 0 or numero > lista[-1]:  # Se for o primeiro valor ou o numero for maior que o ultimo digito
        lista.append(numero)
        print('O valor foi adicionado no final da fila.')

    else:
        posicao = 0  # variavel para navegar pelas posicoes da lista usando o while
        while posicao <= len(lista):  # Enquanto ele nao passar todas posicoes da lista
            if numero < lista[posicao]:  # Se numero for menor que o valor que esta na posicao
                lista.insert(posicao, numero)  # Coloca o numero no lugar do valor que esta na posicao certa
                print(f'Valor adicionado na {posicao}º posicao')
                break

            posicao += 1

print(lista)
