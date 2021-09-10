# Exercício Python 010:
#   Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
#   e mostre quantos dólares ela pode comprar.

from functions import pular

while True:
    print('\n')
    print('-==-' * 11)
    print(f'\033[;1m{"_- Conversor de Moedas -_":^45}\033[m')
    print('-==-' * 11)
    print('\n')
    try:
        escolha = int(input("""Digite um dos numeros para escolher 
a qual moeda deseja converter.
    
    \033[;1m1 -> Dólar
    2 -> Euro\033[m
    
    \033[1;31m0\033[m \033[;1m-> Encerrar o programa.\033[m
    
    
Escolha: """))
    except:
        pular(5)
        print('___' * 10)
        print('\033[;1m[\033[1;31mERRO\033[m]\nPor favor, tente novamente.')
        print('___' * 10)
        input('Pressione \033[1;4menter\033[m para continuar.')
        pular(10)
    else:
        if escolha == 1:    # Converter para dólar
            pular(5)
            print('____' * 20)
            carteira = float(input('Informe quantos reais voce possui...\nR\033[1;32m$\033[m '))
            dolar = carteira * 0.19
            print(f'\n\nCom R\033[1;32m$\033[m{carteira} voce tem U\033[1;32m$\033[m{dolar} (Dólares).')
            input('\nPressione \033[1;4menter\033[m para voltar ao menu de escolha.')
            print('____' * 20)
            pular(10)
        elif escolha == 2:  # Converter para euro
            pular(5)
            print('____' * 20)
            carteira = float(input('Informe quantos reais voce possui...\nR\033[1;32m$\033[m '))
            euro = carteira * 0.16
            print(f'\n\nCom R\033[1;32m$\033[m{carteira} voce tem \033[1;32m€\033[m{euro} (Euros).')
            input('\nPressione \033[1;4menter\033[m para voltar ao menu de escolha.')
            print('____' * 20)
            pular(10)
        elif escolha == 0:  # Encerrar o programa
            pular(10)
            print('Programa \033[1;31mencerrado\033[m! Ate logo :D.')
            break
        else:
            pular(5)
            print('___' * 10)
            print('\033[;1m[\033[1;31mERRO\033[m]\nPor favor, tente novamente.')
            print('___' * 10)
            input('Pressione \033[1;4menter\033[m para continuar.')
            pular(10)
