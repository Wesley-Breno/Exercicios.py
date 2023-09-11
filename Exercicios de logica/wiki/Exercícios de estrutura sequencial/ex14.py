"""
João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo
(50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a
variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do
limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com mensagens adequadas.
"""

while True:  # Enquanto o usuario nao digitar o peso dos peixes corretamente
    try:
        peso_de_peixes = float(input('\nInforme o peso dos peixes em Kgs: '))
    except:
        print('\n\n\t\t\033[;31mINFORME OS DADOS CORRETAMENTE.\033[m')
    else:  # Se o usuario digitou o peso dos peixes corretamente
        break

excesso = peso_de_peixes - 50  # Retirando 50Kgs (Limite estabelecido pelo regulamento de pesca)

if excesso > 0:  # Se o usuario passou do limite de 50Kgs
    multa = excesso * 4  # Para cada Kgs ultrapassado do limite, recebe 4 reais de multa.
    print(f'\n\n\t\tVoce passou o limite de 50Kgs com {excesso:.1f}Kgs a mais\n'
          f'\t\t\tVoce tera que pagar um multa de R${multa:.2f}\n\n')

else:
    print('\n\n\t\tTudo OK (∩^o^)⊃━☆\n'
          'Voce esta dentro do limite do regulamento de pesca.')
