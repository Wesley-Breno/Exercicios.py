# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

from functions import titulo, press_enter, pular, erro, encerrar, programa_encerrado  # Funcoes que criei para me ajudar

titulo('Emprestimo bancário')
press_enter('para comecar.')

deseja = 0  # Recebe 0 se o usuario nao quiser encerrar o programa, recebe 1 se quiser encerrar o programa.

while deseja != 1:  # Enquanto o usuario nao encerrar o programa.
    try:
        valor_da_casa = float(input('\nDigite o valor da casa: R\033[1;32m$\033[m '))
        salario = float(input('\nInforme o seu salario: R\033[1;32m$\033[m '))
        anos = int(input('\nEm quantos anos deseja pagar a casa? '))
    except:
        erro('Por favor\nVerifique os valores informados.')
        pular(5)
    else:
        mensalidade = (valor_da_casa / anos) / 12   # Calculo da mensalidade da casa
        salario_30_porcento = salario * 30 / 100    # 30% do salario do usuario.

        if mensalidade > salario_30_porcento:   # Se a mensalidade exceder os 30% do salario.
            pular(2)
            print('__' * 23)
            print(f'\033[1;31m{"AVISO":^45}\033[m')
            print('''\nA prestacao mensal da casa nao pode
ultrapassar 30% do seu salario.

Seu emprestimo foi \033[1;31mNEGADO\033[m.''')
            print('__' * 23)
            pular(2)

        else:
            pular(2)
            print('__' * 23)
            print(f'\033[1;32m{"Parabens":^45}\033[m')
            print(f'''\nSeu emprestimo foi \033[1;32mAPROVADO\033[m.

Mensalidade por {anos} anos: R\033[1;32m$\033[m {mensalidade:.2f}''')
            print('__' * 23)
            pular(2)

        press_enter()
        deseja = encerrar()  # Perguntando ao usuario se ele deseja encerrar o programa.
        if deseja == 0:  # Se o usuario nao querer encerrar o programa, o programa ira pular 5 linhas.
            pular(5)

programa_encerrado()    # Mensagem de despedida para o usuario.
