# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

from functions import titulo, press_enter, erro, pular, encerrar, programa_encerrado  # Funcoes que criei para me ajudar

deseja = 0  # Variavel para saber se o usuario deseja encerrar o programa.

while deseja != 1:  # Enquanto o usuario nao desejar encerrar o programa.
    titulo('Aumento salarial')
    press_enter('para fazer o aumento.')

    try:
        pular(5)
        print('__' * 20)
        salario = int(input('Informe o seu salario > R\033[1;32m$\033[m '))
    except:
        erro('Por favor\nVerifique os dados informados.')
        pular(5)
    else:
        if salario > 1250:  # Se o salario for maior que 1250, o usuario tera um aumento de 10%
            aumento = salario + (salario * 10 / 100)    # Calculo do aumento
            print(f'\033[;1m\n\n{"Aumento salarial de 10%":^45}\n\033[m')
            print(f'> Salario anterior: R\033[1;32m$\033[m {salario:.2f}\n> Salario atual: R\033[1;32m$\033[m {aumento}\n')
            press_enter()
        else:
            aumento = salario + (salario * 15 / 100)    # Se o salario for menor ou igual a 1250, o aumento sera de 15%
            print(f'\033[;1m\n\n{"Aumento salarial de 15%":^45}\n\033[m')
            print(f'> Salario anterior: R\033[1;32m$\033[m {salario:.2f}\n> Salario atual: R\033[1;32m$\033[m {aumento}\n')
            press_enter()

        deseja = encerrar()  # Perguntando ao usuario se quer encerrar o programa, deseja = 1 para sim e 0 para nao.
        if deseja == 0:  # Se o usuario nao quiser encerrar, o programa ira pular 5 linhas.
            pular(5)

programa_encerrado()
