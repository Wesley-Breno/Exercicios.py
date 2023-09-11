"""
No exemplo acima eu estou usando grupos e retrovisores para diminuir a repeticao de expressoes regulares. com isso eu
faco a validacao do formato de um cpf, tirando os caracteres que vem antes do cpf e os que vem depois, deixando assim
somente o cpf.
"""

import re

cpf = 'asdasdasd147.852.963-12 asdasdasd'  # CPF com alguns caracteres antes e depois dele.

cpf = re.findall(r'(([0-9]{3}\.){2}[0-9]{3}-([0-9]{2}))', cpf)  # Retornando uma lista com uma tupla com o formato
# original do cpf, os dois conjuntos de caracteres que se repetem 2x, a ultima sequencia de 3 numeros e os 2 ultimos
# numeros.

print(cpf)
print(cpf[0][0])  # Mostrando na tela o formato original do cpf.
