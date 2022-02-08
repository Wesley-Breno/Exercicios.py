"""
Faça uma lista de tarefas com as seguintes opções:
    adicionar tarefa
    listar tarefas
    opção de desfazer (a cada vez que chamarmos, desfaz a última ação)
    opção de refazer (a cada vez que chamarmos, refaz a última ação)
    ['Tarefa 1', 'Tarefa 2']
    ['Tarefa 1'] <- Desfazer
    ['Tarefa 1', 'Tarefa 2'] <- Refazer
    input <- Nova tarefa
"""

from time import sleep    # Funcao usada para fazer o programa 'dormir'.
from functions import titulo, pular, press_enter, erro, programa_encerrado    # Funcoes que criei.

lista_tarefas = []    # Lista onde ficara todas as tarefas.
lista_tarefas_desfeitas = []    # Lista onde ficara todas as tarefas que foram excluidas.

titulo('Listas de tarefas')
press_enter('para ir ao menu.')

while True:
    pular(10)

    print(f'\033[1;31m{"Menu":^45}\033[m\n')
    try:    # Pedindo ao usuario para fazer uma escolha do que ele deseja fazer.
        escolha = int(input('''
| 1 | \033[1;31m➜\033[m Mostrar tarefas.
| 2 | \033[1;31m➜\033[m Adicionar nova tarefa.
| 3 | \033[1;31m➜\033[m Excluir ultima tarefa.
| 4 | \033[1;31m➜\033[m Refazer tarefa excluida.
| 5 | \033[1;31m➜\033[m Salvar tarefas.

| 6 | \033[1;31m➜\033[m Informacoes.
| 0 | \033[1;31m➜\033[m Encerrar programa.


Escolha: '''))
    except:    # Caso o usuario informe um dado invalido.
        erro('Digite o numero da escolha\nque voce deseja fazer.')
        pular(5)
    else:
        if escolha == 1:    # Mostrar tarefas.
            pular(5)
            print(f'\033[1;31m{"Tarefas":^45}\033[m\n\n')

            if len(lista_tarefas) == 0:    # Caso o usuario nao adicionou nenhuma tarefa.
                print(f'\033[;1m{"Voce ainda nao adicionou uma tarefa.":^45}\033[m\n\n')
            else:
                cont = 0    # Contador para colocar ao lado da tarefa, vai mostrar se é a primeira tarefa, segunda e etc.
                for i in lista_tarefas:
                    cont += 1
                    print(f'{cont} \033[1;31m➤\033[m {i}')
                print()
            press_enter('para voltar ao menu.')

        elif escolha == 2:    # Adicionar tarefas.
            pular(5)
            print(f'\033[1;31m{"Adicionar tarefa":^45}\033[m\n\n')

            lista_tarefas.append(str(input('Nova tarefa ➤ ').strip().capitalize()))    # Adicionando nova tarefa.
            print('Tarefa adicionada com \033[1;32msucesso\033[m.')
            sleep(1)

        elif escolha == 3:    # Excluir ultima tarefa.
            if len(lista_tarefas) == 0:    # Se nao tiver nenhuma tarefa na lista.
                print(f'\n\n\033[;1m{"Voce ainda nao adicionou uma tarefa.":^45}\033[m\n')
                press_enter('para voltar ao menu.')
            else:
                lista_tarefas_desfeitas.append(lista_tarefas[-1])    # Adicionando para a lista de tarefas desfeitas.
                lista_tarefas.pop()    # Apagando a ultima tarefa.
                print('Tarefa excluida com \033[1;32msucesso\033[m.')
                sleep(1)

        elif escolha == 4:    # Refazer tarefa excluida.
            if len(lista_tarefas_desfeitas) == 0:    # Se nao houver nenhuma tarefa na lista de tarefas excluidas.
                print(f'\n\n\033[;1m{"Voce nao excluiu nenhuma tarefa ainda.":^45}\033[m\n')
                press_enter('para voltar ao menu.')
            else:
                lista_tarefas.append(lista_tarefas_desfeitas[-1])    # Adicionando a tarefa excluida de volta a lista de tarefas comum.
                lista_tarefas_desfeitas.pop()    # Apagando a tarefa que estava 'apagada'.
                print('Tarefa adicionada com \033[1;32msucesso\033[m.')
                sleep(1)

        elif escolha == 5:    # Informacoes do programa e exercicio proposto.
            pular(5)
            print(f'\033[1;31m{"Informacoes":^45}\033[m')
            print('''
Exercicio proposto na aula 93 do curso do Luiz Otavio, na plataforma Udemy.

Exercicio;
    
    Faça uma lista de tarefas com as seguintes opções:
    adicionar tarefa
    listar tarefas
    opção de desfazer (a cada vez que chamarmos, desfaz a última ação)
    opção de refazer (a cada vez que chamarmos, refaz a última ação)
    ['Tarefa 1', 'Tarefa 2']
    ['Tarefa 1'] <- Desfazer
    ['Tarefa 1', 'Tarefa 2'] <- Refazer
    input <- Nova tarefa

Exercicio feito por Wesley Breno.
00:42 - 08/02/2022

''')
            press_enter('para voltar ao menu.')

        elif escolha == 0:    # Encerrar programa.
            break

        else:    # Se o usuario digitar uma escolha diferente das que foram mostradas.
            erro('Digite o numero da escolha\nque voce deseja fazer.')
            pular(5)

programa_encerrado()    # Mensagem de despedida para o usuario.
