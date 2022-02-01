# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais

from functions import titulo, press_enter, erro, pular, programa_encerrado  # Funcoes que criei.

titulo('Comparador')
press_enter('para iniciar.')
print(f'\n\n\033[1;37m{"Digite [ 0 ] para encerrar.":^45}\033[m\n')

while True:  # Enquanto o usuario nao digitar 0.
    try:
        numero1 = int(input('Digite o 1° numero: '))
        if numero1 == 0:  # Se o usuario digitar 0 em um dos numeros, o programa encerra.
            break
        numero2 = int(input('Digite o 2° numero: '))
        if numero2 == 0:
            break
    except:
        erro('Por favor\nVerifique os valores informados.')
    else:
        if numero1 > numero2:
            pular(4)
            print('--' * 20)
            print(f'\t\tNumero {numero1} é o maior valor.')
            print('--' * 20)
            press_enter('para comparar de novo.')
        elif numero2 > numero1:
            pular(4)
            print('--' * 20)
            print(f'\t\tNumero {numero2} é o maior valor.')
            print('--' * 20)
            press_enter('para comparar de novo.')
        else:
            pular(4)
            print('--' * 20)
            print(f'\t\tO numero {numero1} e {numero2} sao iguais.')
            print('--' * 20)
            press_enter('para comparar de novo.')
    pular(5)

programa_encerrado()
