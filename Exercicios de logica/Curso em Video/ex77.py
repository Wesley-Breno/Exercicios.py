"""
Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
"""

palavras = ('arroz', 'feijao', 'batata', 'galinha guisada')

for palavra in palavras:  # Para cada palavra na tupla
    print(f'\nVogais da palavra [ {palavra} ]: ', end='')
    for letra in palavra:  # Para cada letra
        if letra in 'aeiou':  # Se letra estiver em A, E, I, O, ou U.
            print(letra, end=' ')
