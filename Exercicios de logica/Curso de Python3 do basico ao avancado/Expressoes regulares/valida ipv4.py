"""
IPv4 é composto por quatro números, cada um entre 0 e 255, separados por pontos.
Exemplo: xxx.xxx.xxx.xxx
"""

import re

ipv4 = str(input('Digite um IPV4: '))

ipv4_valido = re.findall(r'^(?:(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]|[0-9])\.?){4}\b$', ipv4)

if len(ipv4_valido) >= 1:
    print('\n\n\t\tFormato IPV4 \033[;32mvalido\033[m\n\n'
          f'IPV4: {ipv4}')

else:
    print('\n\n\t\tFormato IPV4 \033[;31minvalido\033[m\n\n'
          '* IPV4 é composto por quatro numeros\n'
          '* Cada numero entre 0 e 255\n'
          '* Separados por pontos\n'
          'Exemplo: xxx.xxx.xxx.xxx')
