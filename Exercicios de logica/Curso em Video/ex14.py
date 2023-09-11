# Exercicio 14
# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

from functions import *

titulo('Conversor de temperatura')

deseja = 0
while deseja != 1:
    try:
        graus_celsius = float(input('\n\nInforme o grau \033[;1m°C\033[m -> '))
    except:
        erro()
    else:
        if type(graus_celsius) == float:
            fahrenheit = (graus_celsius * 9 / 5) + 32
            kelvin = graus_celsius + 273.15
            print()
            print('__' * 18)
            print(f'Grau Celsius: \033[;1m{graus_celsius}\033[m\nConvertido para Fahrenheit: \033[;1m{fahrenheit}\033[m\nConvertido para Kelvin: \033[;1m{kelvin}\033[m')
            print('__' * 18)
            press_enter()
            while True:
                try:
                    deseja = str(input('Deseja continuar a converter? [S/N] -> ')).upper()[0]
                except:
                    erro()
                else:
                    if deseja == 'S':
                        deseja = 0
                        break
                    elif deseja == 'N':
                        deseja = 1
                        break
                    else:
                        erro()
        else:
            erro()

print(f'\n\n\033[;1m{"Programa encerrado com sucesso":^45}')
print(f'{"Ate logo :)":^45}\033[m')
