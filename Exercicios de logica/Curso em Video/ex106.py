"""
Faça um mini-sistema que utilize o Interactive Help do Python.
O usuário vai digitar o comando e o manual vai aparecer.
Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use cores.
"""

from time import sleep  # Importando a funcao sleep para fazer o programa demorar seu proximo passo.

while True:  # Enquanto o usuario nao digitar 'FIM'.
    print('\n\n\t\tDigite a função ou modulo que deseja ver a informações\n'
          '\t\t\t\t\033[;37mDigite "FIM" para encerrar o programa.\033[m\n')

    input_usuario = str(input('Função ou modulo: '))

    if input_usuario == 'FIM':  # Se o usuario digitou 'FIM'.
        break

    print(f'Tentando acessar as informacoes de "{input_usuario}"', end='')
    for c in range(3):  # Escrevendo 3 '.' a cada 1 segundo ao lado do print a cima.
        print('.', end='')
        sleep(1)

    print('\n\033[;37m')
    help(input_usuario)
    print('\n\033[m')

print('\n\n\t\tPrograma encerrado'
      '\n\t\t\tAte logo :)')
