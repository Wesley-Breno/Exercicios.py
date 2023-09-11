# Faça um algoritmo que leia o salário de um funcionário e
# mostre seu novo salário, com 15% de aumento.

from functions import erro, pular

encerrar = ''
while encerrar != 'S':

    print(f'\n\n\033[;1m{"_- Aumento salarial -_":^45}\033[m\n\n')

    try:
        salario = float(input('Digite o seu salario: R\033[1;32m$\033[m '))
    except:
        erro()
    else:
        aumento = salario + (salario * 15 / 100)
        pular(2)
        print('__' * 20)
        print(f'Seu aumento de 15% foi adicionado...\n\nSalario antes: R\033[1;32m$\033[m{salario:.2f}\nSalario com aumento: R\033[1;32m$\033[m{aumento:.2f}')
        print('__' * 20)

        while True:
            try:
                encerrar = str(input('Deseja parar? [S]/[N] -> ')).upper()[0]
            except:
                erro()
            else:
                if encerrar == 'S' or encerrar == 'N':
                    break
                else:
                    erro()

print(f'\n\n\033[;1m{"Programa encerrado. Ate logo :D":^45}\033[m\n\n')
