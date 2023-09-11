"""
Tendo como dado de entrada a altura (h) de uma pessoa,
construa um algoritmo que calcule seu peso ideal,
utilizando as seguintes fórmulas:

Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
"""


while True:  # Enquanto o usuario nao informar todos os dados.
    try:
        altura_usuario = float(input('-> Digite sua altura em metros: '))
        sexo_usuario = str(input('-> Informe o seu sexo (F para feminino, M para masculino)\nSexo: ')).upper()[0]

    except:
        print('\n\n\t\t\033[;31mDIGITE OS VALORES CORRETAMENTE.\033[m')

    else:
        if sexo_usuario != 'F' and sexo_usuario != 'M':  # Se o sexo informado pelo usuario nao for igual a 'F' ou 'M'.
            print('\n\n\t\t\033[;31mDigite o sexo com F para feminino ou M para masculino.\033[m\n')

        else:  # Se o usuario informou o sexo com 'F' ou 'M'.
            peso_ideal = 0
            if sexo_usuario == 'F':
                peso_ideal = (62.1 * altura_usuario) - 44.7

            if sexo_usuario == 'M':
                peso_ideal = (72.7 * altura_usuario) - 58

            print(f'\n\n\t\tSeu peso ideal é de {peso_ideal:.1f}Kgs\n')
            break
