"""
Faça um Programa que pergunte em que turno você estuda.
Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
"""

try:
    turno = str(input('\nInforme o seu turno...\n\n'
                      'M para Matutino\n'
                      'V para Vespertino\n'
                      'N para Noturno\n\n'
                      'Meu turno: '))[0].upper()

except:
    print('\n\n\t\t\033[;31mValor invalido!\033[m')

else:
    print('\n\n\t\t', end='')
    if turno == 'M':
        print('Bom dia!')

    elif turno == 'V':
        print('Boa tarde!')

    elif turno == 'N':
        print('Boa noite!')

    else:
        print('\033[;31mValor invalido!\033[m')
