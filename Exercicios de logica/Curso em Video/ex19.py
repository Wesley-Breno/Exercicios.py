# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela
# o nome do escolhido.

from functions import *     # Importando todas as funções que serão usadas.
from random import randint  # Importando a função randint para chamar um numero aleatorio.

deseja = 0                  # Variavel para saber se o usuario deseja encerrar o programa.
while deseja != 1:
    alunos = []
    numero_no_nome = 0      # Variavel para saber se tem algum numero em um dos nomes.
    erro_adionando_nome = 0  # Variavel para saber se digitou algum nome.
    titulo('Sorteio de alunos')
    pular()
    try:
        for c in range(4):  # Adicionando os quatro alunos.
            alunos.append(str(input(f'Nome do {c + 1}° aluno: ').strip()))
            if alunos[c] == '':     # Caso o usuario nao digite nenhum nome.
                erro('Digite o nome do aluno.')
                erro_adionando_nome = 1
                break
    except:
        erro()
    else:
        for a in alunos:    # Saber se no nome tem algum numero ou caractere especial.
            for b in a:
                if b.isnumeric() or b in '!@#$%"&*()_-+=§{}][/\|?.,¬':
                    numero_no_nome = 1  # Recebe 1 para mostrar que tem numero.
                    nome_errado = a     # Variavel que vai ficar o nome errado.
        if numero_no_nome == 1:
            erro(f'Não é permitido numeros ou\ncaracteres especiais\n[ {nome_errado.capitalize()} ]')
        else:
            if erro_adionando_nome == 0:    # Se foi colocado os 4 nomes corretamente.
                aluno_sorteado = randint(0, len(alunos))    # Sorteando de 0 ate o numero de alunos, o numero sorteado sera a posicao do aluno na lista.
                pular()
                print('__' * 15)
                print(f'O aluno sorteado foi\n> \033[1;32m{alunos[aluno_sorteado].capitalize()}\033[m')
                print('__' * 15)
                press_enter('continuar')
                deseja = encerrar('sorteio')
