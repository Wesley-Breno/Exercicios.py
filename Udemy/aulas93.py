"""
Faça uma lista de tarefas com as seguintes opções;
    * Adicionar tarefa
    * Listar tarefas
    * Desfazer ultima tarefa
    * Refazer ultima tarefa desfeita
"""

from time import sleep

lista_tarefas = []
tarefas_desfeitas = []

while True:
    print(f'\n\n\033[;1m{"Menu":^45}\033[m\n')
    try:
        acao = int(input('''
Digite a acao que deseja fazer: 

[ 1 ] - Adicionar tarefa
[ 2 ] - Lista tarefas
[ 3 ] - Desfazer ultima tarefa
[ 4 ] - Refazer tarefa desfeita

[ 0 ] - Encerrar programa

Digite: '''))

    except:
        print('\n\n\n\033[1;31mERROR\033[m\nPor favor, tente novamente.\n\n\n')
        sleep(2)

    else:
        print('__' * 25)
        if acao == 1:
            lista_tarefas.append(str(input('Digite a tarefa: ')).title().strip())
            print(f'\n\n\033[;1m{"Tarefa adicionada com sucesso":^45}\033[m\n\n')
            sleep(2)

        elif acao == 2:
            if len(lista_tarefas) > 0:
                print(f'\n\n\033[;1m{"Todas as tarefas":^45}\033[m\n')
                print(*lista_tarefas, sep='\n')
                input('\n\nPressione enter para continuar.')
            else:
                print(f'\n\n\033[;1m{"Nao existe nenhuma tarefa ainda":^45}\033[m\n\n')
                sleep(2)

        elif acao == 3:
            if len(lista_tarefas) > 0:
                tarefas_desfeitas.append(lista_tarefas[-1])
                lista_tarefas.pop()
                print(f'\n\n\033[;1m{"Ultima tarefa desfeita":^45}\033[m\n\n')
                sleep(2)
            else:
                print(f'\n\n\033[;1m{"Nao existe nenhuma tarefa ainda":^45}\033[m\n\n')
                sleep(2)

        elif acao == 4:
            if len(tarefas_desfeitas) > 0:
                lista_tarefas.append(tarefas_desfeitas[-1])
                tarefas_desfeitas.pop()
                print(f'\n\n\033[;1m{"Ultima tarefa refeita":^45}\033[m\n\n')
                sleep(2)
            else:
                print(f'\n\n\033[;1m{"Nao existe nenhuma tarefa desfeita ainda":^45}\033[m\n\n')
                sleep(2)

        elif acao == 0:
            break

        else:
            print('\n\n\n\033[1;31mERROR\033[m\nPor favor, tente novamente.\n\n\n')
            sleep(2)

print(f'\n\n\033[;1m{"Programa encerrado com sucesso :)":^45}\033[m\n\n')
