# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

from functions import titulo, press_enter, erro, pular, programa_encerrado    # Funcoes que criei.

titulo('10 termos de uma PA')
press_enter('para comecar.')
pular(5)
print(f'\033[;37m{"Digite [ 0 ] nas duas opcoes para encerrar.":^55}\033[m\n\n')

while True:    # Enquanto o usuario nao digitar zero na variavel 'termo' e na 'razao'.
    print('__' * 15)
    try:
        termo = int(input('Primeiro termo: '))
        razao = int(input('Razão: '))
    except:
        erro('Por favor\nDigite um valor valido.')
    else:
        if termo == 0 and razao == 0:    # Se o usuario digitou zero nas duas variaveis, o programa encerra.
            break
        pular(5)
        print(f'{f"❧ 10 termos de {termo} ☙":^45}\n')
        cont = 0    # Contador para saber se chegou nos 10 termos.
        print('\t', end='')    # Dando um espaço para os termos ficarem mais no meio da tela.
        while True:
            if cont < 9:    # Se o contador for menor que nove, coloque uma seta para o proximo termo.
                print(f'{termo}', end=' ➫ ')
            else:
                print(f'{termo}\n\n')
            termo += razao

            cont += 1
            if cont == 10:    # Se o contador chegar nos 10 termos, ele para de mostrar.
                break

        press_enter('para fazer de novo.')
        pular(5)

programa_encerrado()    # Mensagem de despedida para o usuario.
