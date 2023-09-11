"""
Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior.
Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo que
o usuário digite o salário inicial do funcionário.
"""

from datetime import date  # Funcao que sera usada para saber o ano atual

ano_inicial = 1995
ano_atual = int(date.today().year)
percentual_inicial = 0.75  # Percentual que sera dobrado a cada loop
salario_inicial = 1000  # Salario inicial que tera a adição percentual a cada loop

while ano_inicial != ano_atual:  # Enquanto o ano inicial for diferente do ano atual
    ano_inicial += 1
    percentual_inicial = percentual_inicial * 2
    salario_inicial = 1000 + (1000 * percentual_inicial / 100)  # A cada loop, ele faz uma adição percentual

print('__' * 25)
print(f'Salario atual com aumentos percentuais a cada ano\n\n'
      f'Ano 1995 [salario inicial]\n'
      f'R$ 1000.00\n'
      f'----------------------------------\n'
      f'Ano {ano_atual} [salario atual]\n'
      f'R$ {salario_inicial:.2f}')

while True:  # Enquanto o usuario nao informar um salario inicial para fazer o propio calculo
    try:
        print()
        print('__' * 25)
        salario_inicial = float(input('Informe o salario inicial do funcionario para\n'
                                      'ver o resultado do calculo.\n'
                                      'Salario inicial: R$ '))
    except:
        print('\n\n\t\t[\033[;31mERRO\033[m]: Por favor, informe o salario inicial corretamente.\n')
    else:
        break

ano_inicial = 1995
salario_final = 0  # Variavel que tera o salario atual
percentual_inicial = 0.75
while ano_inicial != ano_atual:
    ano_inicial += 1
    percentual_inicial = percentual_inicial * 2
    salario_final = salario_inicial + (salario_inicial * percentual_inicial / 100)

print('__' * 25)
print(f'Salario atual com aumentos percentuais a cada ano\n\n'
      f'Ano 1995 [salario inicial]\n'
      f'R$ {salario_inicial:.2f}\n'
      f'----------------------------------\n'
      f'Ano {ano_atual} [salario atual]\n'
      f'R$ {salario_final:.2f}')
