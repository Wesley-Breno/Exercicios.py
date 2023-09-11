# Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo.

from functions import titulo, press_enter, erro, pular, encerrar, programa_encerrado  # Funcoes que criei para me ajudar

deseja = 0  # Recebe 0 se o usuario nao quiser encerrar o programa, recebe 1 se o usuario quiser encerrar o programa.

while deseja != 1:  # Enquanto o usuario nao quiser encerrar...
    titulo('▲ Triangulo ▲')
    press_enter()

    try:    # Pegando os valores dos 3 lados.
        lado1 = float(input('\n\nDigite o tamanho do 1° lado: '))
        lado2 = float(input('Digite o tamanho do 2° lado: '))
        lado3 = float(input('Digite o tamanho do 3° lado: '))
    except:
        erro('Por favor\nVerifique os dados informados.')
        pular(5)
    else:
        if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado2 + lado1:  # Se a soma dos 2 lados for maior que o 3° lado.
            print(f'\nOs valores \033[;1m{lado1, lado2, lado3}\033[m \033[1;32mpodem\033[m formar um triangulo.\n')
            press_enter()
        else:
            print(f'\nOs valores \033[;1m{lado1, lado2, lado3}\033[m \033[1;31mnao\033[m podem formar um triangulo.\n')
            press_enter()

        deseja = encerrar()  # Perguntando ao usuario se ele deseja encerrar o programa.
        if deseja == 0:  # Se o usuario nao quiser encerrar, o programa ira pular 5 linhas.
            pular(5)

programa_encerrado()    # Mensagem de despedida para o usuario.
