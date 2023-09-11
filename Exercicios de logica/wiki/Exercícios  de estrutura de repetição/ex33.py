"""
O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado
de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.
"""

temperaturas = []  # Lista que ira conter todas as temperaturas informadas pelo usuario
cont = 1  # Contador para saber quantas temperaturas ja foram informadas

print('\n\n\t\tDigite [ 0 ] para parar de adicionar temperaturas\n')

while True:  # Enquanto o usuario nao digitar 0
    try:
        temperatura = float(input(f'\nInforme a {cont}º temperatura em graus celsius\n'
                                  f'Temperatura: '))

    except:
        print('\n\n\t\t[\033[;31mERRO\033[m]: Informe a temperatura corretamente\n\n')

    else:
        if temperatura == 0:
            break

        temperaturas.append(temperatura)
        cont += 1

print('\n\n\t\tRESULTADO\n\n'
      f'Maior temperatura informada: {max(temperaturas)}\n'
      f'Menor temperatura informada: {min(temperaturas)}\n'
      f'Media das temperaturas: {sum(temperaturas) / len(temperaturas):.1f}')
