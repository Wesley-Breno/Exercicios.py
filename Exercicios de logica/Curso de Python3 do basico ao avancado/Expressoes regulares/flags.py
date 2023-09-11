"""
re.A -> ASCII
re.I -> IGNORECASE
re.M -> Multiline
re.S -> Dotall
"""

import re

texto = """
131.768.468-53
055.123.060-50
955.123.060-90
"""

texto2 = 'O joão gosta de folia \n E adora ser amado'

# Validando o formato dos CPFs do 'texto'.
print(re.findall(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', texto, flags=re.M))  # Considera cada linha do 'texto' como uma string.

print()

# Usando o 're.S' para encotrar a frase que comeca com 'o' e termina com 'o', mesmo com quebra de linha.
print(re.findall(r'^o.*o$', texto2, flags=re.I | re.S))
