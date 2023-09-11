"""
Valida e corrige número de telefone. Faça um programa que leia um número de telefone, e corrija o número no caso deste
conter somente 7 dígitos, acrescentando o '3' na frente. O usuário pode informar o número com ou sem o traço separador.

Valida e corrige número de telefone
Telefone: 461-0133
Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.
Telefone corrigido sem formatação: 34610133
Telefone corrigido com formatação: 3461-0133
"""

# Enquanto o usuario nao informar um numero com pelo menos 7 digitos
while True:
    numero_informado = str(input('Informe o numero de telefone: '))

    # Se o valor informado pelo usuario for apenas de caracteres numericos
    if numero_informado.replace('-', '').isdigit():

        # Se o numero informado pelo usuario estiver com os 8 digitos e com o '3' na frente
        if len(numero_informado.replace('-', '')) == 8 and numero_informado.replace('-', '')[0] == '3':
            print(f'Telefone corrigido com formatação: {numero_informado[0:4]}-{numero_informado[4:]}')
            break

        # Se o numero informado pelo usuario estiver com apenas os 7 caracteres numericos.
        elif len(numero_informado.replace('-', '')) == 7:
            print('Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.')
            print(f'Telefone corrigido com formatação: 3{numero_informado[0:3]}-{numero_informado[3:]}')
            break

        # Se o numero estiver invalido
        else:
            print('\n\n\t\t[ERRO]: Por favor, informe o numero de telefone corretamente.\n\n')
    else:
        print('\n\n\t\t[ERRO]: Por favor, informe o numero de telefone corretamente.\n\n')
