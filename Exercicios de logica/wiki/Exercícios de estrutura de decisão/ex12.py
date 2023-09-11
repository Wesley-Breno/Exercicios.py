"""
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende
do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não
é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos.

O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20%

Imprima na tela as informações, dispostas conforme o exemplo abaixo.
No exemplo o valor da hora é 5 e a quantidade de hora é 220.

        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00
"""

while True:
    try:
        salario_por_hora = float(input('Informe quanto voce ganha por hora: R$ '))
        horas_trabalhadas_no_mes = float(input('Informe quantas horas voce trabalhou no mes: '))
    except:
        print('\n\n\t\t\033[;31mDIGITE OS VALORES CORRETAMENTE\033[m\n')
    else:
        break

salario_bruto = salario_por_hora * horas_trabalhadas_no_mes

if salario_bruto <= 900:
    desconto_ir = 0

elif salario_bruto <= 1500:
    desconto_ir = salario_bruto * 5 / 100

elif salario_bruto <= 2500:
    desconto_ir = salario_bruto * 10 / 100

else:
    desconto_ir = salario_bruto * 20 / 100

desconto_inss = salario_bruto * 10 / 100
desconto_fgts = salario_bruto * 11 / 100
total_de_descontos = desconto_ir + desconto_inss
salario_liquido = salario_bruto - total_de_descontos

print(f"""
\t\tResultado 

Salario bruto: R$ {salario_bruto:.2f}
Desconto IR: R$ {desconto_ir:.2f}
Desconto INSS: R$ {desconto_inss:.2f}
Desconto FGTS: R$ {desconto_fgts:.2f}
Total de descontos: R$ {total_de_descontos:.2f}
Salario liquido: R$ {salario_liquido:.2f}""")
