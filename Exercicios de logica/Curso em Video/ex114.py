"""
Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
"""

from urllib.request import urlopen

try:
    urlopen('http://pudim.com.br/')

except:
    print('\n\n\t\tO site nao esta \033[;31macessivel\033[m :(\n\n')

else:
    print('\n\n\t\tO site esta \033[;32macessivel\033[m :D\n\n')
