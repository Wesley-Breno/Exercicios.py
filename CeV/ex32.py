# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from functions import titulo, press_enter, erro, programa_encerrado, pular

titulo('Ano bissexto')
press_enter('para fazer o calculo.')

while True:    # Enquanto o usuario nao digitar 0
    try:
        print(f'\n\n\033[1;37m{"-- Digite 0 para encerrar --":^45}\033[m\n\n')
        ano = int(input('Digite o ano: '))
    except:
        erro('Por favor\n\nVerifique o dado que foi\ninformado e tente novamente.')
        pular(10)
    else:
        if ano == 0:    # Se o usuario digitar 0, o programa é encerrado
            break
        if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 and ano % 100 == 0:    # Para saber se o ano é bissexto
            print(f'\n\n\033[;4m{f"{ano} é um ano bissexto.":^45}\033[m\n\n')
            press_enter('para fazer outro calculo.')
            pular(10)
        else:
            print(f'\n\n\033[;4m{f"{ano} não é bissexto.":^45}\033[m\n\n')
            press_enter('para fazer outro calculo.')
            pular(10)

programa_encerrado()    # Mensagem para quando o programa for encerrado
