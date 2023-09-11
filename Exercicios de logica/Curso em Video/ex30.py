# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

from functions import titulo, erro, press_enter, encerrar, programa_encerrado, pular

deseja = 0

while deseja != 1:    # Enquanto o usuario decidir continuar usando o programa.
    titulo('Impar ou Par')
    print(f'{"Digite um numero e direi":^45}')
    print(f'{"se ele é impar ou par.":^45}\n\n')

    try:
        numero = int(input('Numero: '))    # Numero que sera feito o calculo.
    except:
        erro('Por favor\nVerifique o numero inserido.')    # Tratamento de erro, caso o usuario nao digite um numero.
        pular(5)
    else:
        if numero % 2 == 0:    # Se o numero for par.
            print(f'\n\n{f"Numero {numero} é par.":^45}\n\n')
            press_enter()
            deseja = encerrar()    # Pergunta ao usuario se ele deseja encerrar o programa, retorna 1 se sim.
            if deseja == 0:
                pular(5)
        else:    # Se o numero for impar.
            print(f'\n\n{f"Numero {numero} é impar.":^45}\n\n')
            press_enter()
            deseja = encerrar()
            if deseja == 0:
                pular(5)

programa_encerrado()
