"""
As Organizações Tabajara resolveram dar um abono aos seus colaboradores em reconhecimento ao bom resultado alcançado
durante o ano que passou. Para isto contratou você para desenvolver a aplicação que servirá como uma projeção de quanto
será gasto com o pagamento deste abono.

Após reuniões envolvendo a diretoria executiva, a diretoria financeira e os representantes do sindicato laboral,
chegou-se a seguinte forma de cálculo:

a.Cada funcionário receberá o equivalente a 20% do seu salário bruto de dezembro; a.O piso do abono será de 100 reais,
isto é, aqueles funcionários cujo salário for muito baixo, recebem este valor mínimo; Neste momento, não se deve ter
nenhuma preocupação com colaboradores com tempo menor de casa, descontos, impostos ou outras particularidades.

Seu programa deverá permitir a digitação do salário de um número indefinido (desconhecido) de salários. Um valor de
salário igual a 0 (zero) encerra a digitação. Após a entrada de todos os dados o programa deverá calcular o valor do
abono concedido a cada colaborador, de acordo com a regra definida acima. Ao final, o programa deverá apresentar:

O salário de cada funcionário, juntamente com o valor do abono;
O número total de funcionário processados;
O valor total a ser gasto com o pagamento do abono;
O número de funcionário que receberá o valor mínimo de 100 reais;
O maior valor pago como abono; A tela abaixo é um exemplo de execução do programa, apenas para fins ilustrativos. Os
valores podem mudar a cada execução do programa.

Projeção de Gastos com Abono
============================

Salário: 1000
Salário: 300
Salário: 500
Salário: 100
Salário: 4500
Salário: 0

Salário    - Abono
R$ 1000.00 - R$  200.00
R$  300.00 - R$  100.00
R$  500.00 - R$  100.00
R$  100.00 - R$  100.00
R$ 4500.00 - R$  900.00

Foram processados 5 colaboradores
Total gasto com abonos: R$ 1400.00
Valor mínimo pago a 3 colaboradores
Maior valor de abono pago: R$ 900.00
"""

salarios = []
abonos = []
contador_colaboradores = 0  # Total de colaboradores analisados
contador_valor_minimo_pago_a_colaboradores = 0  # Colaboradores que receberam abono minimo de 100 reais
ABONO_MINIMO = 100
PORCENTAGEM_ADICIONAL_DO_SALARIO = 20

print('\n\n\t\tDigite [ 0 ] para encerrar o programa.\n\n')

# Enquanto o usuario nao digitar 0
while True:

    # Tentando pegar o salario bruto do colaborador da vez
    try:
        print()
        print('--' * 20)
        salario_bruto = float(input(f'Digite o salario bruto do {contador_colaboradores + 1}º colaborador\n'
                                    f'Salario bruto: R$ '))

    # Se o usuario não informou um valor numerico para ser o salario bruto do colaborador
    except ValueError:
        print(f'\n\n\t\t[ERRO]: O valor informado não corresponde a um salario numerico.\n\n')

    # Se o usuario informou corretamente o salario bruto do colaborador
    else:
        if salario_bruto == 0:  # Se o usuario decidiu parar de adicionar os salarios dos colaboradores
            break

        salarios.append(salario_bruto)
        contador_colaboradores += 1

# Se o usuario informou pelo menos 1 salario
if len(salarios) > 0:

    # Fazendo calculos dos abonos de cada colaborador
    for salario in salarios:

        # Se salario do colaborador for maior que piso do abono, o abono sera 20% do salario
        if salario * PORCENTAGEM_ADICIONAL_DO_SALARIO / 100 > ABONO_MINIMO:
            abonos.append(salario * PORCENTAGEM_ADICIONAL_DO_SALARIO / 100)

        # Se o salario do colaborador for muito baixo, o abono sera de 100
        else:
            abonos.append(ABONO_MINIMO)
            contador_valor_minimo_pago_a_colaboradores += 1

    # Mostrando na tela o resultado dos calculos dos abonos
    print()
    print('--' * 14)
    print('Salarios\t|\tAbonos')
    print('--' * 14)
    for index, salario in enumerate(salarios):
        print(f'R$\t{salario:.2f}\t|\tR$\t{abonos[index]:.2f}')
    print('--' * 14)
    print(f"""
Foram processados {contador_colaboradores} colaboradores
Total gasto com abonos: R$ {sum(abonos):.2f}
Valor mínimo pago a {contador_valor_minimo_pago_a_colaboradores} colaboradores
Maior valor de abono pago: R$ {max(abonos):.2f}""")

# Se o usuario nao informou nenhum salario
else:
    print('\n\n\t\tVocê não informou nenhum salario.\n\n')
