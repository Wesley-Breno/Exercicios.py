from time import sleep  # Importando a funcao sleep para fazer o programa demorar algum tempo para continuar
from collections import deque  # Importando a funcao deque para fazer uma lista FIFO

print('\n\n\t\t\033[;1mQuitanda do Werli\033[m\n\n')

fila = deque()
cont = 0  # Contador para dizer qual cliente comprou no pedido

while True:
    cont += 1
    print('--' * 12)
    escolha = str(input("""
        Menu

[ 1 ] - Agua
[ 2 ] - Coxinha
[ 3 ] - Pastel
[ 4 ] - Coquinha gelada
[ 0 ] - Sair do menu


Escolha: """))

    if escolha.isdigit():  # Se o valor digitado for um numero
        if escolha == '1':
            print(f'\nCliente {cont} pediu Agua')
            fila.append(['Agua'])

        elif escolha == '2':
            print(f'\nCliente {cont} pediu Coxinha')
            fila.append(['Coxinha'])

        elif escolha == '3':
            print(f'\nCliente {cont} pediu Pastel')
            fila.append(['Pastel'])

        elif escolha == '4':
            print(f'\nCliente {cont} pediu Coquinha gelada')
            fila.append(['Coquinha gelada'])

        elif escolha == '0':
            break

        else:
            print('\n\n\t[\033[;31mERRO\033[m]: Por favor, escolha um produto do cardapio com base em seu numero\n\n')
            cont = 0

        sleep(1)

    else:
        print('\n\n\t[\033[;31mERRO\033[m]: Por favor, escolha um produto do cardapio com base em seu numero\n\n')
        cont = 0

    sleep(1)

cont = 0  # Contador para mostrar qual cliente finalizou a compra
while True:
    if len(fila) != 0:
        print(f'\nCliente {cont + 1} finalizou a compra de {fila.popleft()}')
        cont += 1
    else:
        break

print('\n\n\t\tNao ha mais pedidos :)\n\n')
