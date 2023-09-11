"""
Faça um Programa que leia um número e exiba o dia correspondente da semana.
(1-Domingo, 2- Segunda, etc.),
se digitar outro valor deve aparecer valor inválido.
"""

dias_da_semana = ['Domingo', 'Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sabado']

while True:  # Enquanto o usuario nao digitar um numero que corresponda a um dia da semana.
    try:
        numero_digitado = int(input('\nDigite um numero que seja correspondente ao dia da semana.\n'
                                    'Numero: '))
    except:
        print('\n\n\t\t\033[;31mDIGITE UM NUMERO QUE SEJA CORRESPONDENTE AO DIA DA SEMANA.\033[m\n')

    else:
        if 1 <= numero_digitado <= 7:
            print(f'\n\n\t\tVoce digitou um numero que corresponde a {dias_da_semana[numero_digitado - 1]}')
            break

        else:
            print('\n\n\t\t\033[;31mDIGITE UM NUMERO QUE SEJA CORRESPONDENTE AO DIA DA SEMANA.\033[m\n')
