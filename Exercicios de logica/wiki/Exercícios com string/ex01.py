"""
Tamanho de strings.
Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. Informe também se as duas
strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

Compara duas strings
String 1: Brasil Hexa 2006
String 2: Brasil! Hexa 2006!
Tamanho de "Brasil Hexa 2006": 16 caracteres
Tamanho de "Brasil! Hexa 2006!": 18 caracteres
As duas strings são de tamanhos diferentes.
As duas strings possuem conteúdo diferente.
"""

print('Compara duas strings')

# Recebendo 2 strings informadas pelo usuario
string_1 = str(input('String 1: '))
string_2 = str(input('String 2: '))

# Mostrando o total de caracteres de cada string
print(f'Tamanho de "{string_1}": {len(string_1)} caracteres')
print(f'Tamanho de "{string_2}": {len(string_2)} caracteres')

# Se as duas strings tiverem a mesma quantidade de caractere
if len(string_1) == len(string_2):
    print('As duas strings sao de tamanho igual')
else:
    print('As duas strings são de tamanhos diferentes.')

# Se as duas strings tiverem o mesmo conteudo
if string_1 == string_2:
    print('As duas strings possuem conteudo igual')
else:
    print('As duas strings possuem conteúdo diferente.')
