"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.

calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.
"""

while True:  # Enquanto o usuario nao digitar os valores corretamente
    try:
        salario_por_hora = float(input('\nInforme quanto voce ganha por hora: '))
        horas_trabalhadas_no_mes = float(input('Informe quantas horas voce trabalhou no mês: '))

    except:
        print('\n\n\t\t\033[;31mDIGITE OS VALORES CORRETAMENTE.\033[m')

    else:  # Se o usuario digitou os valores corretamente
        break

salario_bruto = salario_por_hora * horas_trabalhadas_no_mes  # Salario bruto
ir = salario_bruto * 11 / 100  # Quantidade que o IR retirou do salario
inss = salario_bruto * 8 / 100  # Quantidade que o INSS retirou do salario
sindicato = salario_bruto * 5 / 100  # Quantidade que o sindicato retirou do salario
salario_liquido = salario_bruto - (ir + inss + sindicato)  # Salario liquido

print(f'\n\n\t\tResultado\n\n'
      f'Salario bruto do mês: R${salario_bruto:.2f}\n'
      f'Desconto do IR: R${ir:.2f}\n'
      f'Desconto do INSS: R${inss:.2f}\n'
      f'Desconto do sindicato: R${sindicato:.2f}\n'
      f'Salario liquido: R${salario_liquido:.2f}\n')
