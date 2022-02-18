# Crie um programa que faça o computador jogar Jokenpô com você.

from random import choice    # Usando o choice para ele escolher um numero de 1 a 3.
from functions import titulo, press_enter, pular, programa_encerrado, erro    # Funcoes que criei.

objetos = [1, 2, 3]    # Cada numero representa um objeto do jokenpo.
jogador_pontos, cpu_pontos = 0, 0    # A contagem de pontos (o primeiro a chegar a 5 ganha).

titulo('Jokenpo')
press_enter('para jogar.')

while True:
    if cpu_pontos == 5:    # Se a cpu alcançar 5 vitorias
        print(f'\n\n\033[;1m{"Voce":>21} \033[m\033[1;31mperdeu\033[m!')
        print(f'{"A cpu alcançou 5 pontos.":^45}\n')
        jogador_pontos, cpu_pontos = 0, 0    # Zerando a contagem de pontos
        press_enter('para encerrar ou continuar a jogar.')
        pular(5)

    if jogador_pontos == 5:    # Se o usuario alcançar 5 vitorias
        print(f'\n\n\033[;1m{"Voce":>21} \033[m\033[1;32mvenceu\033[m!')
        print(f'{"Voce alcançou 5 pontos.":^45}\n')
        jogador_pontos, cpu_pontos = 0, 0
        press_enter('para encerrar ou continuar a jogar.')
        pular(5)

    escolha_cpu = choice(objetos)    # A escolha que a cpu fez
    print(f'\n\033[;1m{"Escolha":^45}\033[m')
    try:
        escolha_jogador = int(input('''
[ 1 ] ▷ Pedra
[ 2 ] ▷ Papel
[ 3 ] ▷ Tesoura
[ 0 ] \033[1;31m▷\033[m Encerrar


escolha: '''))
    except:
        erro('Algo deu errado\nPor favor, tente novamente.')
        pular(5)
    else:

        pular(2)
        if escolha_jogador == 0:    # Se o usuario decidir encerrar o programa.
            break

        # Empate
        if escolha_jogador == escolha_cpu:
            print(f'\033[33;1m{"Empate":^45}\033[m')

        # Jogador ganhando
        if escolha_jogador == 1 and escolha_cpu == 3:    # jogador = pedra, cpu = tesoura
            print(f'\033[;1m{"Voce":>21} \033[m\033[1;32mvenceu\033[m!')
            print(f'{"A cpu escolheu tesoura.":^45}')
            jogador_pontos += 1

        if escolha_jogador == 2 and escolha_cpu == 1:    # jogador = papel, cpu = pedra
            print(f'\033[;1m{"Voce":>21} \033[m\033[1;32mvenceu\033[m!')
            print(f'{"A cpu escolheu pedra.":^45}')
            jogador_pontos += 1

        if escolha_jogador == 3 and escolha_cpu == 2:    # jogador = tesoura, cpu = papel
            print(f'\033[;1m{"Voce":>21} \033[m\033[1;32mvenceu\033[m!')
            print(f'{"A cpu escolheu papel.":^45}')
            jogador_pontos += 1

        # Cpu ganhando
        if escolha_cpu == 1 and escolha_jogador == 3:  # cpu = pedra, jogador = tesoura
            print(f'\033[;1m{"Voce":>21} \033[m\033[1;31mperdeu\033[m!')
            print(f'{"A cpu escolheu pedra.":^45}')
            cpu_pontos += 1

        if escolha_cpu == 2 and escolha_jogador == 1:  # cpu = papel, jogador = pedra
            print(f'\033[;1m{"Voce":>21} \033[m\033[1;31mperdeu\033[m!')
            print(f'{"A cpu escolheu papel.":^45}')
            cpu_pontos += 1

        if escolha_cpu == 3 and escolha_jogador == 2:  # cpu = tesoura, jogador = papel
            print(f'\033[;1m{"Voce":>21} \033[m\033[1;31mperdeu\033[m!')
            print(f'{"A cpu escolheu tesoura.":^45}')
            cpu_pontos += 1

        if escolha_jogador != 1 and escolha_jogador != 2 and escolha_jogador != 3 and escolha_jogador != 0:    # Se o usuario nao digitar nenhuma das opções do menu de escolha.
            erro('Digite uma das opções do menu.')
            pular(5)
        else:
            print(f'{f"| Jogador - {jogador_pontos} | --- | CPU - {cpu_pontos} |":^45}\n\n')
            press_enter('para jogar novamente.')
            pular(5)


programa_encerrado()
