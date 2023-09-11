#  Faça um programa que calcule a soma entre todos os números que são múltiplos de três
#  e que se encontram no intervalo de 1 até 500.

from functions import titulo, press_enter    # Funcoes que criei.

soma = 0    # Variavel onde ira ficar a soma.
cont = 0    # Variavel onde ira ficar quantos numeros foram somados.

titulo('Multiplos de 3')
press_enter('para mostrar os multiplos.')

print()
for c in range(1, 501, 2):    # Fazendo contagem de 1 a 500, pulando de 2 em 2.
    if c % 3 == 0:    # Se o numero for divisivel por 3.
        cont += 1
        soma += c    # Fazendo a soma de cada numero.

print(f'\nA soma de todos os {cont} numeros multiplos de 3\nTotal da soma: {soma}')
