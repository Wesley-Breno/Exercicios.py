# Estudando List comprehension
# Exemplo 1: Copiar uma lista

lista_mae = [1, 2, 3, 4, 5]
lista_copia = [n for n in lista_mae]

# Exemplo 2: Copie uma lista onde cada numero é multiplicado por 2

lista_filho = [n * 2 for n in lista_mae]

# Exemplo 3: Copie uma lista onde cada numero vai ter seu indice do lado.

lista_filho_ex3 = [(i, n) for i, n in enumerate(lista_mae)]

# Exemplo 4: Copie uma lista de nomes e troque o 'A' por '@'.

lista_nomes = ['Gustavo', 'Raissa', 'Larissa', 'Banana']
lista_sem_a = [n.replace('a', '@').upper() for n in lista_nomes]

# Exemplo 5: Copie uma lista e faça 2 elementos irem um pro lugar do outro

lista_nomes_exemplo5 = [['Gustavo', 'Raissa'], ['Larissa', 'Banana']]
lista_trocada = [(nome2, nome1) for nome1, nome2 in lista_nomes_exemplo5]

# Exemplo 6: Copie uma lista que tem a contagem de 0 a 100, so coloque os numeros divisiveis por 3 e 8.

lista_contagem_100 = [n for n in range(100)]
lista_divisiveis_38 = [n for n in lista_contagem_100 if n % 3 == 0 and n % 8 == 0]

# Exemplo 7: Copie uma lista que tem a contagem de 0 a 100, e so coloque os numeros que sao divisiveis por 3, oq n for 0

lista_divisiveis3 = [n if n % 3 == 0 else 0 for n in lista_contagem_100]

