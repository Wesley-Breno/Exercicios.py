"""
Faça um Programa que pergunte quanto você ganha por hora
e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês
"""

comissao_por_hora = float(input('Quanto voce ganha por hora?\n'
                                '-> R$ '))

horas_trabalhadas_no_mes = float(input('Quantas horas voce trabalhou no mês?\n'
                                       '-> Total de horas: '))

# Multiplicando o salario por hora com as horas trabalhadas do mês
salario_total = comissao_por_hora * horas_trabalhadas_no_mes

print(f'\n\nTrabalhando {horas_trabalhadas_no_mes:.1f}Hrs por mês e recebendo R\033[;32m$\033[m{comissao_por_hora:.2f} '
      f'por hora\n'
      f'Seu salario total é de: R\033[;32m$\033[m{salario_total:.2f}')
