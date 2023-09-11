"""
Exercício para fazer um algoritmo que gere um CPF.
"""

from random import randint  # Função usada para gerar numeros inteiros aleatorios.
from functions import linha, pular, press_enter, encerrar, programa_encerrado  # Funções que criei.

deseja_encerrar = 0
pular(5)

while True:  # Enquanto o usuario nao quiser encerrar o programa.
    press_enter('para gerar um CPF.')
    cpf, cpf_copia = [], []
    cpf_valido = False
    cont = 0  # Contador que sera usado para saber onde colocar as pontuações.

    while not cpf_valido:

        soma, calculo = 0, 0  # Serão usados para pegar o penultimo e ultimo numero do CPF.

        for c in range(11):
            cpf.append(randint(0, 9))

        for p, n in enumerate(range(10, 1, -1)):  # Pegando a multiplicacao de cada numero na sequencia que foi mostrada na aula e fazendo a soma.
            soma += cpf[p] * n

        calculo = 11 - (soma % 11)
        calculo = 0 if calculo > 9 else calculo
        cpf_copia.append(cpf[:9])
        cpf_copia.append(calculo)

        calculo, soma = 0, 0  # Zerando as variaveis para pegar o calculo do ultimo numero do CPF.

        for p, n in enumerate(range(11, 1, -1)):
            soma += cpf[p] * n

        calculo = 11 - (soma % 11)
        calculo = 0 if calculo > 9 else calculo
        cpf_copia.append(calculo)

        cpf_valido = True if cpf[-2:] == cpf_copia[-2:] else cpf_valido
        if cpf_valido:
            break
        cpf, cpf_copia = [], []

    print()
    linha(vezes=14)
    print('CPF gerado: ', end='')
    for c in cpf:
        cont += 1
        if cont == 3:
            print(c, end='.')
        elif cont == 6:
            print(c, end='.')
        elif cont == 9:
            print(c, end='-')
        else:
            print(c, end='')

    deseja_encerrar = encerrar()
    if deseja_encerrar == 1:
        break

programa_encerrado()
