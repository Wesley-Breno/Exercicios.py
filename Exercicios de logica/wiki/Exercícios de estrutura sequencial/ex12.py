"""
Tendo como dados de entrada a altura de uma pessoa,
construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
"""

while True:  # Enquanto o usuario nao digitar um valor que seja valido.
    try:
        altura = float(input('\n\nDigite a sua altura em metros: '))

    except:
        print('\n\n\t\t\033[;31mDIGITE OS VALORES CORRETAMENTE.\033[m')

    else:  # Se o usuario digitou o valor corretamente.
        break

peso_ideal = (72.7 * altura) - 58

print(f'\n\n\t\tO seu peso ideal medindo {altura:.2f} é de {peso_ideal:.1f}Kgs.\n\n')
