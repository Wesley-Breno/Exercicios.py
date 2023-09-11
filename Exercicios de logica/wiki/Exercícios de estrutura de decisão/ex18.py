"""
Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
"""

import re

data = str(input('Informe uma data com o formato dd/mm/aaaa\nData: '))

data_separada = re.findall(r'^(\d{1,2})/(\d{1,2})/(\d{4})$', data)  # Expressao regular para pegar o formato da data.

dia, mes, ano = data_separada[0]  # Colocando dia, mes e ano informados em variaveis diferentes.

meses_com_30dias = (4, 6, 9, 11)
meses_com_31dias = (1, 3, 5, 7, 8, 10, 12)

if len(data_separada) >= 1:  # Se o formato da data estiver certo, conforme o anunciado do exercício.

    # Se for fevereiro
    if int(dia) <= 28 and int(mes) == 2 and int(ano) % 4 != 0 or int(dia) <= 29 and int(mes) == 2 and int(ano) % 4 == 0:
        print('\n\n\t\tFormato de data \033[;32mvalido\033[m')

    elif int(dia) <= 30 and int(mes) in meses_com_30dias:  # Se for um dos meses com 30 dias
        print('\n\n\t\tFormato de data \033[;32mvalido\033[m')

    elif int(dia) <= 31 and int(mes) in meses_com_31dias:  # Se for um dos meses com 31 dias
        print('\n\n\t\tFormato de data \033[;32mvalido\033[m')

    else:
        print('\n\n\t\tFormato de data \033[;31minvalido\033[m')

else:
    print('\n\n\t\tFormato de data \033[;31minvalido\033[m')
