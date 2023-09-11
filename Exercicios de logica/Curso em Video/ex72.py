"""
 Crie um programa que tenha uma dupla totalmente preenchida com
 uma contagem por extenso, de zero até vinte. Seu programa deverá
 ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
"""

# Valores na extensao
numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco',
           'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze',
           'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis',
           'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

print('\n\n\t\t\033[;37mDigite um valor negativo para encerrar.\033[m\n')

while True:  # Enquanto o usuario nao digitar um numero menor que 0
    try:
        numero = int(input('\n\nDigite um numero de 0 a 20 para ver ele por extenso...\n'
                           'Numero: '))

        if numero < 0:  # Se o usuario digitar um valor menor que 0, o programa encerra.
            break

    except:
        print('\n\n\t\t[\033[;31mERRO\033[m]: Por favor, insira o valor numerico novamente.\n\n')

    else:
        if 20 >= numero >= 0:  # Se o valor digitado for entre 0 e 20.
            print('\n' * 2)
            print('--' * 15)
            print(f'\t\t\033[;1mResultado\033[m\n\nNumero: {numero}\n'
                  f'Extensao: {numeros[numero]}')
            print('--' * 15)

        else:
            print('\n\n\t\t[\033[;31mERRO\033[m]: Digite um numero de 0 a 20\n\n')

print('\n\n\t\tPrograma encerrado com sucesso\n\n')
