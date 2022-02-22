# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
# indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from functions import titulo, press_enter    # Funcoes que criei.
from time import sleep    # Funcao usada para fazer o programa "dormir".

titulo('Contagem regressiva')
press_enter('para começar a contagem.')

print()
for c in range(10, 0, -1):    # Vai contar do 10 ate o 0.
    print(c)
    sleep(1)    # Fazendo o programa "dormir" por 1 segundo.

print(f'\n\033[;1m{"⁂⁂ Feliz ano novo!!! ⁂⁂":^45}\033[m')    # Mensagem para o usuario, desejando feliz ano novo.
