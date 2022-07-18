"""
Crie um programa onde o usuário possa digitar cinco valores numéricos
e cadastre-os em uma lista, já na posição correta de inserção
(sem usar o sort()). No final, mostre a lista ordenada na tela.
"""

lista = []

for c in range(5):
    print('__' * 10)
    numero = int(input('Digite o valor: '))

    if c == 0 or numero > lista[-1]:
        lista.append(numero)
        print('Valor adicionado ao final da lista.')

    else:
        posicao = 0

        while posicao < len(lista):
            if numero <= lista[posicao]:
                lista.insert(posicao, numero)
                print(f'Valor adicionado na posicao {posicao}')
                break

            posicao += 1


print(f'Numeros informados em ordem: {lista}')
