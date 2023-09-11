"""
Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, o programa deve converter
14:25 em 2:25 P.M. A entrada é dada em dois inteiros.

Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída. Registre a informação A.M./P.M. como
um valor ‘A’ para A.M. e ‘P’ para P.M. Assim, a função para efetuar as conversões terá um parâmetro formal para
registrar se é A.M. ou P.M. Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada
todas as vezes que desejar.
"""


def converte_24hrs_para_am_ou_pm(horario: int, minutos: int) -> tuple:
    """
    Funcao que recebe o horario e os minutos como parametros, e
    converte o horario de 24hrs para horario de AM/PM.
    :param horario: Horario em 24 horas
    :param minutos: Minutos do horario
    :return: Retorna uma tupla com o horario convertido para o formato AM/PM
    """
    turno = ''

    # Convertendo horario e colocando o turno
    if 12 <= horario < 24:  # Se o horario corresponde ao turno da tarde
        if not horario == 12:
            horario = horario - 12

        turno = 'P'

    elif 1 <= horario <= 11 or horario == 24:  # Se o horario corresponde ao turno da manha
        if horario == 24:
            horario = horario - 12

        turno = 'A'

    if 0 <= minutos <= 59:  # Se o minuto informado corresponde a um minuto correto (Estiver entre 0 e 59)
        if turno == 'P' or turno == 'A':  # Se nao houve erro na conversao do horario, retorna o horario convertido.
            return horario, minutos, turno


def imprimi_horario_formatado(horario: int, minutos: int, turno: str) -> None:
    """
    Funcao que verifica se o horario necessita de um 0 no inicio e imprimi o horario na tela.
    :param horario: Horario formatado
    :param minutos: Minutos formatados
    :param turno: Turno do horario
    :return: None
    """
    if horario < 10:
        horario = f'0{horario}'

    if minutos < 10:
        minutos = f'0{minutos}'

    print(f'\n\n\t\tHorario convertido: {horario}:{minutos} {turno}.M\n\n')


# Recebendo horarios do usuario
while True:  # Enquanto o usuario nao quiser encerrar o programa
    try:
        hora_informada = int(input('Informe a hora (01-24): '))
        minutos_informados = int(input('Informe os minutos (00-59): '))

    except ValueError:
        print('\n\n\t\t[ERRO]: Por favor, informe o horario e minutos corretamente!\n\n')

    else:
        horario_convertido = converte_24hrs_para_am_ou_pm(hora_informada, minutos_informados)

        if horario_convertido is not None:  # Se o usuario informou um horario com formato 24hrs valido
            imprimi_horario_formatado(*horario_convertido)
        else:
            print('\n\n\t\t[ERRO]: Por favor, informe o horario e minutos corretamente!\n\n')

        continuar = input("Deseja converter outro horário? (s/n) ")
        if continuar.lower() != 's':
            break
