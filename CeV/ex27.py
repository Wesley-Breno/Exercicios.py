# Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.

from functions import titulo, press_enter, pular, encerrar, erro, programa_encerrado

deseja = 0
while deseja != 1:
    titulo('Primeiro e ultimo')
    press_enter('para começar.')

    pular(25)
    try:
        nome = str(input('\n\nDigite o seu nome completo...\nNome: ').title())
    except:
        erro('Por favor\nTente novamente.')
    else:
        nome_lista = nome.split()   # Fazendo cada nome virar uma lista apos cada espaço
        nome_junto = ''.join(nome_lista)    # Juntando o nome sem os espaços

        if nome_junto.isalpha():    # Se todas os caracteres que estiverem no nome foram letras
            if len(nome_lista) == 1:    # Se o usuario digitou apenas um nome
                pular(25)
                erro('Por favor, digite o nome\ncompleto.')
                pular(25)
            else:
                primeiro_nome = nome_lista[0]   # Pegando o primeiro nome
                ultimo_nome = nome_lista[-1]    # Pegando o ultimo nome

                pular(25)
                print('╼╼' * 20)
                print(f'Primeiro nome > \033[1;37m{primeiro_nome}\033[m\nUltimo nome > \033[1;37m{ultimo_nome}\033[m\n\nNome completo\n\033[1;37m{nome}\033[m')
                print('╼╼' * 20)
                press_enter()
                pular(25)
                deseja = encerrar()  # Função para perguntar ao usuario se ele quer encerrar.
                if deseja == 0:  # Se o usuario não querer encerrar o programa, pulara 25 linhas
                    pular(25)
        else:
            pular(25)
            erro('Por favor, digite um nome\nque so contenha letras.')
            pular(25)

programa_encerrado()    # Função para escrever uma mensagem de adeus quando o programa for encerrado
