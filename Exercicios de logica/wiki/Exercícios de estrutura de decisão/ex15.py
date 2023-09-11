"""
Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo.
Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;
"""

lados = []
while True:  # Enquanto o usuario nao informar os lados corretamente.
    try:
        for c in range(3):
            lados.append(int(input(f'Informe o {c + 1}º lado: ')))

    except:
        print('\n\n\t\t\033[;31mDIGITE OS LADOS CORRETAMENTE.\033[m\n')
        lados = []

    else:
        break

if lados[0] < lados[1] + lados[2] and lados[1] < lados[0] + lados[2] and lados[2] < lados[1] + lados[0]:

    print('\n\n\t\tOs valores informados formam um triangulo ', end='')
    if lados[0] == lados[1] == lados[2]:
        print('equilátero\n')

    elif lados[0] == lados[1] or lados[0] == lados[2] or lados[1] == lados[2]:
        print('isosceles\n')

    else:
        print('escaleno\n')

else:
    print('\n\n\t\tOs valores informados \033[;31mnão\033[m formam um triangulo.\n')
