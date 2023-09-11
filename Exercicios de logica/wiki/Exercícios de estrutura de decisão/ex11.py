"""
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o
programa que calculará os reajustes.

Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:

salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5%

Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.
"""

while True:  # Enquanto o usuario nao digitar o salario corretamente.
    try:
        antigo_salario = float(input('Informe o seu salario: R$ '))

    except:
        print('\n\n\t\t\033[;31mDIGITE O SALARIO CORRETAMENTE.\033[m\n')

    else:
        break

if antigo_salario <= 280:  # Aumento de 20%
    novo_salario = antigo_salario + (antigo_salario * 20 / 100)
    valor_aumentado = antigo_salario * 20 / 100
    percentual = 20

elif 208 < antigo_salario <= 700:  # Aumento de 15%
    novo_salario = antigo_salario + (antigo_salario * 15 / 100)
    valor_aumentado = antigo_salario * 15 / 100
    percentual = 15

elif 700 < antigo_salario <= 1500:  # Aumento de 10%
    novo_salario = antigo_salario + (antigo_salario * 10 / 100)
    valor_aumentado = antigo_salario * 10 / 100
    percentual = 10

else:  # Aumento de 5%
    novo_salario = antigo_salario + (antigo_salario * 5 / 100)
    valor_aumentado = antigo_salario * 5 / 100
    percentual = 5

print('\n\n\t\tResultado\n\n'
      f'Antigo salario: R$ {antigo_salario:.2f}\n'
      f'Percentual de aumento aplicado: {percentual}%\n'
      f'Valor do aumento: R$ {valor_aumentado:.2f}\n'
      f'Novo salario com o aumento: R$ {novo_salario:.2f}')
