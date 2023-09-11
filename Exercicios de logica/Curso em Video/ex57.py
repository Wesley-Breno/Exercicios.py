"""
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto.
"""

from functions import erro, press_enter, linha  # Funções que criei.

linha(vezes=19)
press_enter('para informar o sexo.')

while True:  # Enquanto o usuario nao digitar o sexo corretamente.

    try:
        sexo = str(input('\n\nDigite o sexo [ F / M ]: ')).strip().upper()[0]
    except:
        erro('Por favor\nDigite o sexo corretamente\nExemplo: F = Feminino, M = Masculino.')
    else:
        if sexo in 'mMfF':  # Se o usuario digitou o sexo corretamente.
            print(f'\n\n\033[;1m{"Sexo informado com sucesso":^45}\n{"Ate logo :D":^45}\033[m')
            break

        erro('Por favor\nDigite o sexo corretamente\nExemplo: F = Feminino, M = Masculino.')
