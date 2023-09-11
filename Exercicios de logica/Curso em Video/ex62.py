"""
Melhore o DESAFIO 061
perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos.
"""

from time import sleep  # Importando a funcao para fazer o programa demorar para executar seu proximo 'passo'.

print('\n\t\tDigite [ 0 ] na quantidade de termos\n\t\t\tpara encerrar o programa.\n')
while True:  # Enquanto o usuario nao digitar 0 na variavel 'quantidade_de_termos'.

    print('__' * 15)
    try:
        quantidade_de_termos = int(input('Quantidade de termos > '))

        if quantidade_de_termos == 0:  # Encerrando programa.
            break

        primeiro_termo = int(input('Primeiro termo > '))
        razao = int(input('Razao > '))

    except:
        print('\n\t\t\033[1;31mERRO\033[m\n\t\tPor favor, informe os valores corretamente.\n')
        sleep(2)

    else:
        print(f'\n\t\t{quantidade_de_termos} termos da PA\n')
        while quantidade_de_termos != 0:  # Enquanto o programa nao mostrar a quantidade de termos que o usuario pediu.

            if quantidade_de_termos > 1:  # Se nao for o ultimo termo, mostre o termo e um ' > '.
                print(primeiro_termo, end=' > ')
            else:
                print(primeiro_termo)

            primeiro_termo += razao
            quantidade_de_termos -= 1

print('\n\n\t\tPrograma encerrado com sucesso :)\n\n')
