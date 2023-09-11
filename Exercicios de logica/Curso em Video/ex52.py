
"""
- Exercício feito pelo SmartPhone - 
Faca um programa que leia um numero inteiro e
diga se ele e ou nao um numero primo.
"""

print('__' * 22)
print(f'\n\n\033[;1m{"Numeros primos":^45}\033[m\n')
print('\033[;37m>Descubra se um valor é primo\n>Se o numero for verde, ele é divisivel\n>Se o numero for vermelho, nao é divisivel\n>Se for divisivel apenas por 1 e ele mesmo, é um numero primo.\n\n\033[m')
print('Pressione \033[;1mEnter\033[m para comecar.')
print('__' * 22)
input()

while True:    # Enquanto o usuario nao digitar zero.
    cont = 0    # Contador para saber se o numero é primo. se o contador for igual a 2, o numero é primo.
    
    print('\n' * 5)
    print(f'\033[;37m{"Digite [ 0 ] para encerrar o programa.":^45}\033[m\n\n')
    print('__' * 16)
    
    try:
        numero = int(input('Digite um numero natural: '))
    except:
        print('\n' * 5)
        print('__' * 16)
        print('[ \033[;31mERROR\033[m ]\n Por favor, verifique o numero informado.')
        print('__' * 16)   
        input('Pressione \033[;1mEnter\033[m para tentar de novo.')
        print('\n' * 5)
    else:
        if numero == 0:    # Se o usuario digitar zero, o programa ira encerrar.
            break

        print('\n' * 5)
        for c in range(1, numero + 1):    # Fazendo uma contagem de 1 ate o numero digitado.
            if c == numero:    # Se chegar no numero digitado, o programa nao ira colocar ', '.
                if numero % c == 0:    # Se o numero for divisivel...
                    print(f'\033[;32m{c}\033[m')
                    cont += 1    # Contador recebe  + 1
                else:
                    print(f'\033[;31m{c}\033[m')
            else:
                if numero % c == 0:
                    print(f'\033[;32m{c}\033[m', end=', ')
                    cont += 1
                else:
                    print(f'\033[;31m{c}\033[m', end=', ')
         
        print('\n' * 5)           
        if cont == 2:    # Se o contador for igual a 2, o numero digitado é primo.
            print(f'O numero {numero} é um \033[;32mnumero primo\033[m.')
            print('__' * 16)
            input('Pressione \033[;1mEnter\033[m para continuar.')
        else:
            print(f'O numero {numero} \033[;31mnao\033[m é um numero primo.')
            print('__' * 16)
            input('Pressione \033[;1mEnter\033[m para continuar.')
        
        print('\n' * 10)

print(f'\n\n\n{"Programa encerrado ♡":^45}\n\n\n')
