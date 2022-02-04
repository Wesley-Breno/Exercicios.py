"""
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
e mostre sua categoria, de acordo com a idade:

- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER
"""

from functions import titulo, press_enter, encerrar, programa_encerrado, pular    # Funcoes que criei.
import datetime    # Pegando a data atual do sistema.

data_atual = datetime.datetime.now()    # Pegando a data e hora atual.
data = data_atual.date()    # Pegando apenas a data.
ano_atual = data.strftime('%Y')    # Pegando o ano atual.

deseja = 0    # Recebe 1 se o usuario desejar encerrar o programa, recebe 0 se nao quiser encerrar.

titulo('Confederecao Nacional de Natacao')

while deseja != 1:    # Enquanto o usuario nao desejar encerrar o programa.
    ano_nascimento = int(input('Informe o ano de nascimento do atleta: '))    # Pegando o ano de nascimento do atleta.

    idade = int(ano_atual) - ano_nascimento    # Pegando a idade do atleta.

    if idade <= 9:
        print(f'\n\n{f"Idade: {idade}":^45}\n{"Sua categoria é MIRIM.":^45}\n\n')
    elif idade <= 14:
        print(f'\n\n{f"Idade: {idade}":^45}\n{"Sua categoria é INFANTIL.":^45}\n\n')
    elif idade <= 19:
        print(f'\n\n{f"Idade: {idade}":^45}\n{"Sua categoria é JUNIOR.":^45}\n\n')
    elif idade <= 25:
        print(f'\n\n{f"Idade: {idade}":^45}\n{"Sua categoria é SENIOR.":^45}\n\n')
    else:
        print(f'\n\n{f"Idade: {idade}":^45}\n{"Sua categoria é MASTER.":^45}\n\n')

    press_enter()
    deseja = encerrar()    # Perguntando ao usuario se ele quer encerrar o programa.
    if deseja == 0:    # Se o usuario nao quiser encerrar, o programa ira pular 5 linhas.
        pular(5)

programa_encerrado()    # Mensagem de despedida apos o usuario decidir encerrar o programa.
