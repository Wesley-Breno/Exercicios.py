# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from functions import titulo, press_enter, erro, pular, programa_encerrado
from random import randint

cont = 0    # Contador para executar um algoritmo apenas uma vez.
while True:
    titulo('Adivinhe')
    if cont == 0:
        press_enter()
        cont += 1
    try:    # Menu de escolha
        escolha = int(input('''\nDigite o numero da escolha que deseja fazer...

[ 1 ] ➤ Jogar
[ 2 ] ➤ Informações
[ 3 ] ➤ Sair

Escolha: '''))
    except:
        erro('Por favor, tente novamente.')
    else:
        if escolha == 1:    # Se o usuario escolher jogar.
            pular(10)
            while True:
                numero = randint(0, 5)  # Pegando um numero de 0 a 5

                try:
                    pular(5)
                    print('__' * 15)
                    adivinhe = int(input('Qual numero eu pensei?\n> '))
                except:
                    erro('Por favor, tente novamente.')
                else:
                    if adivinhe == -1:  # O usuario escolheu parar de jogar
                        pular(10)
                        break
                    elif adivinhe >= 6:  # Se o usuario digitar um numero que seja maior que 5
                        erro('Digite um numero entre 0 e 5\nDigite -1 se quiser parar.')
                    elif adivinhe == numero:    # Se o usuario acertar o numero que a CPU escolheu
                        pular(5)
                        print(f'\033[;1m{"Parabéns":^45}\033[m')
                        print(f'\033[1;32m{"Você acertou":^45}\033[m\n\n')
                        press_enter()
                    else:   # Se o usuario errar o numero que a CPU escolheu 
                        pular(5)
                        print(f'\033[;1m{"Oh não":^45}\033[m')
                        print(f'\033[1;31m{"Você errou":^45}\033[m')
                        print(f'\n{f"Eu pensei no numero {numero}":^45}\n\n')
                        press_enter()
        elif escolha == 2:  # Se o usuario escolher ler as informações
            pular(5)
            print(f'\033[1;37m{"Informações":^90}\033[m')
            print('''\033[;37m
Exercício que foi colocado no vídeo do professor Gustavo Guanabara, no canal Curso em Vídeo.

\033[1;37mExercício 28\033[m\033[;37m
    Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e 
    peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
    O programa deverá escrever na tela se o usuário venceu ou perdeu.

\033[1;37mComo jogar?\033[m\033[;37m
    Após iniciar o programa e pressionar enter, você ira para o menu de escolha, onde vai
    escolher entre jogar, ler as informações ou encerrar o programa.
    
    Caso tenha escolhido jogar, basta apenas adivinhar o numero em que a CPU 'pensou'.
    Se você quiser parar de jogar apenas digite '-1' quando o programa pedir para você
    adivinhar o numero.\033[m''')
            print()
            press_enter('para voltar ao menu.')
            pular(10)
        elif escolha == 3:  # Se o usuario escolher encerrar o programa.
            pular(5)
            break
        else:   # Se o usuario não digitar nenhuma das opções
            erro('Por favor, verifique o numero\nque foi digitado.')
            pular(10)

programa_encerrado()
