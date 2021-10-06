# Crie um programa que leia um número Real qualquer pelo
# teclado e mostre na tela a sua porção Inteira.

from functions import *

encerrar = 0
while encerrar == 0:
    titulo('Conversor de numero real')
    try:
        numero_real = float(input('\nDigite o numero real: '))
    except:
        erro('Por favor\nDigite um numero real valido.')
    else:
        numero = int(numero_real)
        pular(2)
        print('__' * 14)
        print(f'Numero real: \033[;1m{numero_real}\033[m\nConvertido para inteiro: \033[;1m{numero}\033[m')
        print('__' * 14)
        press_enter()
        while True:
            try:
                deseja = str(input('\nDeseja encerrar o programa? [S/N] -> ')).upper()[0]
            except:
                erro()
            else:
                if deseja == 'S':
                    encerrar += 1
                    break
                elif deseja == 'N':
                    break
                else:
                    erro()

pular(5)
print(f'\033[;1m{"Programa encerrado":^45}')
print(f'{"Ate logo :D":^45}\033[m')
pular(5)
