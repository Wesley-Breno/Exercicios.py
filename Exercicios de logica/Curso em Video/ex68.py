"""
Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
"""

from random import randint  # Importando o modulo random com a funçao randint para pegar numeros aleatorios
from time import sleep  # Importando o modulo time com a funçao sleep para fazer o programa demorar seu processo.

total_vitorias = 0  # contagem de acertos do usuario

while True:
    valor_cpu = randint(1, 9)  # Pegando um numero aleatorio de 1 a 9

    try:
        valor_jogador = int(input('Digite um valor > '))
        par_ou_impar = str(input('Par ou Impar? [P/I] > ').lower())[0]
    except:
        print('\n\n\t\t[\033[;31mERRO\033[m]: Por favor, informe os valores novamente.\n\n')
        sleep(2.5)
    else:

        resultado = (valor_jogador + valor_cpu) % 2 == 0  # Retorna valor bool se os valores dividos por 2 for resto 0

        if resultado and par_ou_impar == 'p':  # Se deu par e o usuario escolheu par
            print(f"""\n\t\tVoce \033[;32macertou\033[m
        {valor_jogador} + {valor_cpu} = Par\n""")
            total_vitorias += 1

        elif not resultado and par_ou_impar == 'i':  # Se deu impar e o usuario escolheu impar
            print(f"""\n\t\tVoce \033[;32macertou\033[m
        {valor_jogador} + {valor_cpu} = Impar\n""")
            total_vitorias += 1

        else:  # Se o usuario perdeu
            if resultado:
                print(f"""\n\t\tVoce \033[;31merrou\033[m
        {valor_jogador} + {valor_cpu} = Par""")
                break
            else:
                print(f"""\n\t\tVoce \033[;31merrou\033[m
        {valor_jogador} + {valor_cpu} = Impar""")
                break

print(f'\n\tTotal de vitorias ate perder: {total_vitorias}\n\n')
