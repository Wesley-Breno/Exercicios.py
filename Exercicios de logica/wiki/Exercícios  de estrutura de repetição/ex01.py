"""
Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo
até que o usuário informe um valor válido.
"""

while True:  # Enquanto o usuario nao informar uma nota entre 0 e 10
    try:
        nota = int(input('\nInforme uma nota entre 0 e 10\nNota: '))
    except:
        print('\n\n\t\t[\033[;31mERRO\033[m]: Por favor insira uma nota entre 0 e 10.')
    else:
        if 0 <= nota <= 10:  # Se a nota informada estiver entre 0 e 10
            print(f'\n\n\t\tVoce informou a nota [{nota}]')
            break
        else:
            print('\n\n\t\t[\033[;31mERRO\033[m]: Por favor insira uma nota entre 0 e 10.')
