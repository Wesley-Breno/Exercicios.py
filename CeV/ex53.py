# Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsidere os espaços.

print('\nDigite [ 0 ] para encerrar.\n') # Se o usuario digitar 0 o programa sera encerrado.
while True:    # Enquanto o usuario nao digitar zero.
    frase = str(input('digite a frase: ').strip())
    
    if frase == '0':    # Se o usuario digitou 0
        break
    
    frase_junta = []    # Lista onde vai ficar a frase junta, sem os espacos
    for i in frase:
        if i != ' ':
           frase_junta.append(i)

    frase_contraria = frase_junta[::-1]    # Usando a formatacao para colocar a frase ao contrario

    if frase_junta == frase_contraria:
        print('\nessa frase eh \033[;32mpalindromo\033[m')
        input('digite Enter para continuar.')
    else:
        print('\nessa frase \033[;31mnao\033[m eh palindromo')
        input('digite Enter para continuar.')
    print('\n\n')

print('\n\nprograma encerrado ♡ byebye')
    
