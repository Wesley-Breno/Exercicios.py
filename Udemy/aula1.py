from functions import *

while True:
    print(f'\n\033[31;1m{"Bem vindo ao menu":^45}\033[m')

    try:
        escolha = int(input('''\nDigite o numero que corresponde\na escolha que deseja fazer.


1 \033[1;31m➣\033[m Exercicio 1.

2 \033[1;31m➣\033[m Exercicio 2.

3 \033[1;31m➣\033[m Exercicio 3.

4 \033[1;31m➣\033[m Informações.

0 \033[1;31m➣\033[m Encerrar.


Escolha: '''))
    except:
        print('\n\033[1;31mERRO\033[m\nVerifique o valor inserido.\nPor favor, tente novamente.')
        pular()
        linha('__', 18)
        press_enter('para voltar ao menu.')
        linha('\n', 5)
    else:
        if escolha == 1:
            print(f'\n\n{"Exercicio 1":^45}\n')
            press_enter()

            print(f'\n\n\033[;37m{"Digite [ 0 ] para encerrar.":^45}\033[m\n\n')

            while True:  # Enquanto o usuario nao digitar '0'.
                pular(2)

                try:
                    linha('__', 14)
                    numero = int(input('Digite um numero inteiro: '))
                    linha('__', 14)

                except:
                    pular(5)
                    erro('Por favor\nDigite um valor valido.')
                    pular(5)

                else:
                    if numero == 0:  # Se o usuario digitou '0', o programa encerra.
                        press_enter('para voltar ao menu.')
                        pular(4)
                        break

                    if numero % 2 == 0:
                        print(f'O numero {numero} é \033[;32mpar\033[m')
                    else:
                        print(f'O numero {numero} é \033[;31mimpar\033[m')

                    linha('__', 14)

        elif escolha == 2:
            while True:
                numerico, string = 0, 0  # Contador para saber quantos numeros e strings tem.

                titulo('Que horas são?')
                press_enter('para informar a hora.')

                hora_original = str(input('Digite que horas são: ')).strip().split()[0]

                if len(hora_original) == 2 or len(
                        hora_original) == 5:  # Usuario informou apenas a hora, ou a hora e os minutos.

                    for n in hora_original:  # Verificando os numeros e strings que tem.
                        if n in '1234567890':
                            numerico += 1
                        if n in ':':
                            string += 1

                    if numerico == 4 and string == 1 or numerico == 2 and string == 0:  # Usuario informou a hora e os minutos, ou so a hora.
                        hora = int(hora_original[
                                   :2])  # Convertendo a hora em inteiro para pode fazer as estruturas condicionais.
                        pular(2)

                        if 00 <= hora <= 11:
                            print(
                                f'{"Bom dia meu rei!":^45}\n{"Ja é uma boa hora pra um cafezin?":^45}\n{hora_original:>22}Hrs\n')
                            press_enter('para encerrar.')
                            break

                        elif 12 <= hora <= 17:
                            print(
                                f'{"Boa tarde chefia!":^45}\n{"Ja olho pra janela hoje?":^45}\n{hora_original:>22}Hrs\n')
                            press_enter('para encerrar.')
                            break

                        elif 18 <= hora <= 23:
                            print(
                                f'{"Boa noiteeeee!":^45}\n{"Fecha essa janela ai, porque aqui eu to com muito frio!":^45}\n{hora_original:>22}Hrs\n')
                            press_enter('para encerrar.')
                            break

                        else:
                            erro('Por favor\nInforme a hora correta.\nExemplo: 00:00, 12:34')

                else:
                    erro('Por favor\nInforme a hora correta.\nExemplo: 00:00, 12:34')
            pular(4)

        elif escolha == 3:
            print(f'\n\n{"Exercicio 3":^45}')
            """
            Faça um programa que peça o primeiro nome do usuario.
            Se o nome tiver 4 letras ou menos escreva "Seu nome é curto";
            se tiver entre 5 e 6 letras, escreva "Seu nome é normal";
            maior que 6 escreva "Seu nome é muito grande".
            """

            from functions import titulo, press_enter, linha, erro, programa_encerrado  # Funções que criei.

            titulo('Name')
            press_enter()

            while True:
                try:
                    nome = str(input('Digite o nome: ')).strip().title().split()[
                        0]  # Retirando os espaços, colocando em maiusculo e pegando somente o primeiro nome.

                except:
                    erro('Por favor\nDigite um nome so com letras.')

                else:
                    if nome.isalpha():  # Se so houver letras no nome.
                        print(f'\n\n\033[;1m{nome}\033[m')
                        linha(vezes=12)

                        if len(nome) <= 4:
                            print('Seu nome é curto.')

                        elif 5 <= len(nome) <= 6:
                            print('Seu nome é normal.')

                        else:
                            print('Seu nome é muito grande.')

                        linha(vezes=12)
                        press_enter('para encerrar.')
                        break

                    else:
                        erro('Por favor\nDigite um nome so com letras.')

            programa_encerrado()

        elif escolha == 4:

            linha('\n', 5)
            print(f'\033[1;37m{"Informações":^65}\033[m')
            print('''
    Neste software feito por mim, deixei 3 exercicios que foram
    feitos no curso do \033[;1m@otaviomirandabr\033[m na plataforma Udemy.
    (Os exercicios so foram feitos apenas para o meu aprendizado na linguagem.)

    Exercicio 1
        Faça um programa que peça ao usuario para digitar um numero inteiro,
        informe se este numero é par ou impar. Caso o usuario não digite um
        numero inteiro, informe que não é um numero inteiro.

    Exercicio 2
        Faça um programa que pergunte a hora ao usuario e, baseando-se no ho-
        rario descrito, exiba a saudação apropriada. EX.
        Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.

    Exercicio 3
        Faça um programa que peça o primeiro nome do usuario. Se o nome tiver
        4 letras ou menos, escreva "Seu nome é  curto"; se tiver entre 5 e 6
        letras, escreva "Seu nome é normal"; maior que 6 escreva "Seu nome é
        muito grande".''')
            pular()
            linha('__', 18)
            press_enter('para voltar ao menu.')
            linha('\n', 5)

        elif escolha == 0:
            linha('\n', 5)
            break

        else:
            erro('Verifique o valor inserido.\nPor favor, tente novamente.')
            pular()
            linha('__', 18)
            press_enter('para voltar ao menu.')
            linha('\n', 5)

programa_encerrado()
