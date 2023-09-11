"""
Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta.
O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para a
função valorPagamento, que calculará o valor a ser pago e devolverá este valor ao programa que a chamou.

O programa deverá então exibir o valor a ser pago na tela. Após a execução o programa deverá voltar a pedir outro valor
de prestação e assim continuar até que seja informado um valor igual a zero para a prestação.

Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total de
prestações pagas no dia.

O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem atraso, cobrar o valor da prestação.
Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.
"""


def valor_pagamento(prestacao: float, dias_atraso: int) -> float:
    """
    Funcao que recebe o valor de uma prestacao e os dias em atraso. Se houver atraso na prestacao, o programa ira somar
    o valor da prestacao com 3% de multa e mais 0,1% para cada dia de atraso, e retornando o valor que foi gerado. Se
    nao houver dias em atraso o programa apenas ira retornar o valor da prestacao.
    :param prestacao: Valor da prestacao que ira ser calculado
    :param dias_atraso: Dia em atraso, se for 0, o programa nao ira somar com a multa e juros.
    :return: Retorna o valor total a ser pago pela prestacao
    """
    if dias_atraso == 0:  # Se nao houver dias de atraso no pagamento da prestacao
        return prestacao

    # Se houver atraso no pagamento da prestacao
    total_a_pagar = prestacao + (prestacao * 3 / 100)  # Adicionando 3% de multa na prestacao
    juros = 0

    for c in range(dias_atraso):  # Adicionando 0,1% na prestacao para cada dia em atraso
        juros += prestacao * 0.1 / 100

    return total_a_pagar + juros


total = 0  # Total a pagar pela prestacao informada
total_das_prestacoes = 0  # Total a pagar por todas as prestacoes informadas
contagem_prestacoes_do_dia = 0

while True:  # Enquanto o usuario nao encerrar o programa

    # Recebendo o valor da prestacao e os dias em atraso que serao calculados
    try:
        print()
        print('--' * 27)
        valor_da_prestacao = float(input("Digite o valor da prestação (ou 0 para encerrar): "))

        if valor_da_prestacao == 0:
            break

        dias_em_atraso = int(input('Informe os dias em atraso (0 = sem atraso): '))

    # Se o usuario informou algum dado invalido
    except ValueError:
        print('\n\n\t\t[ERRO]: Por favor, informe corretamente os dados necessarios.\n\n')

    # Se o usuario informou os dados corretamente
    else:
        if valor_da_prestacao > 0 and dias_em_atraso >= 0:  # Se o usuario nao informou um valor negativo
            total = valor_pagamento(valor_da_prestacao, dias_em_atraso)  # Chamando funcao e retornando valor a ser pago
            print(f'\n\n\t\tTotal a pagar: R$ {total:.2f}\n\n')  # Mostrando o total a pagar pela prestacao informada
            total_das_prestacoes += total
            contagem_prestacoes_do_dia += 1

        else:
            print('\n\n\t\t[ERRO]: Nao é possivel fazer calculos de valores negativos.\n\n')

print('\n\n\t\tRelatorio do dia\n\n'
      f'Total do valor que foi pago em prestacoes\nTotal: R$ {total_das_prestacoes:.2f}\n\n'
      f'Total de prestacoes pagas do dia: {contagem_prestacoes_do_dia}')
