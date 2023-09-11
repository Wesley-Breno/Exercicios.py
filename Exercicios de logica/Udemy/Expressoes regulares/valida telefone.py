import re

while True:  # Enquanto o usuario nao digitar o formato de um numero de telefone corretamente
    telefone = str(input('Digite o numero de telefone: '))

    formato_completo = re.findall(r'^\+\d{,3} \d{2} \d{4}-\d{4}$|^\+\d{,3} \d{2} \d{8}$', telefone)  # DDI + DD + numero
    numero_e_dd = re.findall(r'^\d{2} \d{4}-\d{4}$|^\d{2} \d{8}$', telefone)  # DD + numero
    numero = re.findall(r'^\d{4}-\d{4}$|^\d{8}$', telefone)  # Apenas numero

    if len(formato_completo) == 1:  # Se o usuario digitou o formato completo de um numero de telefone
        print('\n\n\t\tVoce digitou o formato completo de um numero de telefone')

        dd_e_numero = numero_e_dd = re.findall(r'\d{2} \d{4}-\d{4}|\d{2} \d{8}', telefone)
        apenas_numero = re.findall(r'\d{4}-\d{4}|\d{8}', telefone)

        print(f'\nFormato completo DDI + DD + numero: {formato_completo}\n'
              f'Formato DD + numero: {dd_e_numero}\n'
              f'Formato numero: {apenas_numero}')

        break

    elif len(numero_e_dd) == 1:  # Se o usuario digitou apenas o DD e o numero de telefone
        print('\n\n\t\tVoce digitou apenas o DD e o numero do telefone')

        apenas_numero = re.findall(r'\d{4}-\d{4}|\d{8}', telefone)

        print(f'\nFormato DD + numero: {numero_e_dd}\n'
              f'Formato numero: {apenas_numero}')

        break

    elif len(numero) == 1:  # Se o usuario digitou apenas o numero de telefone
        print('\n\n\t\tVoce digitou apenas o numero do telefone')

        print(f'\nFormato numero: {numero}')

        break

    else:
        print('\n\n\t\t\033[;37mPor favor, digite o numero do telefone corretamente.\033[m\n')
