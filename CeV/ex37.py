# Escreva um programa em Python que leia um número inteiro qualquer
# e peça para o usuário escolher qual será a base de conversão:
# 1 para binário
# 2 para octal
# 3 para hexadecimal.

from functions import titulo, erro, pular, press_enter, programa_encerrado, encerrar  # Funcoes que eu criei.

deseja = 0  # Recebe 0 se o usuario nao quer encerrar o programa, recebe 1 se ele quer.

while deseja != 1:  # Enquanto o usuario nao quiser encerrar o programa.
    titulo('Conversor')
    press_enter('para comecar.')

    try:  # Tentando pegar o valor do numero que sera convertido e no que ele sera convertido.
        numero = int(input('\nDigite o numero que deseja converter...\nNumero: '))
        pular(4)
        escolha = int(input('''
1 \033[1;31m➤\033[m Converter para binario.
2 \033[1;31m➤\033[m Converter para octal.
3 \033[1;31m➤\033[m Converter para hexadecimal.


Escolha: '''))
    except:  # Mensagem de erro, caso o usuario digite um valor invalido.
        erro('Por favor\nVerifique o valor informado.')
        pular(5)
    else:  # Se nao ocorrer erro.
        if escolha == 1:  # Se o usuario escolheu converter para binario.
            numero_em_binario = bin(numero)  # Usando a funcao bin() para converter o numero para binario.
            pular(5)

            print(f'\033[;1m{f"{numero} convertido para binario.":^45}\033[m\n\n')
            print(f'Numero informado  ➤ {numero}\nNumero convertido ➤ {numero_em_binario[2:]}\n')
            press_enter()

            deseja = encerrar()  # Perguntando ao usuario se ele deseja encerrar o programa.
            if deseja == 0:  # Se o usuario nao querer encerrar, o programa ira pular 10 linhas.
                pular(10)

        elif escolha == 2:  # Se o usuario escolheu converter para octal.
            numero_em_octal = oct(numero)  # Usando a funcao oct() para converter o numero para octal.
            pular(5)

            print(f'\033[;1m{f"{numero} convertido para octal.":^45}\033[m\n\n')
            print(f'Numero informado  ➤ {numero}\nNumero convertido ➤ {numero_em_octal[2:]}\n')
            press_enter()

            deseja = encerrar()
            if deseja == 0:
                pular(10)

        elif escolha == 3:  # Se o usuario escolheu converter para hexadecimal.
            numero_em_hexadecimal = hex(numero)  # Usando a funcao hex() para converter o numero para hexadecimal.
            pular(5)

            print(f'\033[;1m{f"{numero} convertido para hexadecimal.":^45}\033[m\n\n')
            print(f'Numero informado  ➤ {numero}\nNumero convertido ➤ {numero_em_hexadecimal[2:]}\n')
            press_enter()

            deseja = encerrar()
            if deseja == 0:
                pular(10)

        else:  # Se o usuario nao digitar nenhuma das opcoes mostradas no menu de escolha.
            erro('Por favor\nVerifique o valor informado.')
            pular(5)

programa_encerrado()  # Mensagem de despedida mostrada ao usuario quando for encerrar o programa.
