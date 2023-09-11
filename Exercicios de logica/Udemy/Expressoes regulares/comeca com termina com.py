"""
Meta caracteres:
^ -> Comeca com
$ -> Termina com
[^a-z] -> Negacao
"""

import re

cpf = '147.852.963-12'
print(re.findall(r'^(([0-9]{3}\.){2}[0-9]{3}-[0-9]{2})$', cpf))  # A string tem comecar e terminar da forma especificada
print(re.findall(r'[^a-zA-Z]+', cpf))  # A string pode ter qualquer caractere, menos letras de A a Z.
