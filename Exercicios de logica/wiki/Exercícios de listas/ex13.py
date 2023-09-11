"""
Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a
média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar
o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
"""

meses_do_ano = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho',
                'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
medias_dos_meses = []
media_anual = 0

while True:  # Enquanto o usuario nao informar as medias dos meses corretamente
    try:
        for index, mes in enumerate(meses_do_ano):
            print()
            print('--' * 25)
            medias_dos_meses.append(float(input(f'Informe a media de temperatura do mes de {mes}\n'
                                                f'Media de temperatura: ')))

    except ValueError:  # Caso o usuario informe um dado invalido
        print('\n\n\t\t[\033[;31mERRO\033[m]: Por favor, informe os dados corretamente\n\n')
        medias_dos_meses = []  # Apagando as medias para serem informadas novamente

    else:  # Se o usuario informou os dados corretamente
        break

media_anual = sum(medias_dos_meses) / 12  # Pegando a media anual

print()
print('--' * 30)
print('\t\t\t\t\tResultado\n\n'
      f'Meses que tiveram a temperatura acima da media anual de {media_anual:.1f}\n')

for index, temperatura in enumerate(medias_dos_meses):
    if temperatura > media_anual:  # Se a temperatura do mes for maior que a temperatura media anual
        print(f'\t\t\t\t\t{meses_do_ano[index]}: {temperatura:.1f}')
