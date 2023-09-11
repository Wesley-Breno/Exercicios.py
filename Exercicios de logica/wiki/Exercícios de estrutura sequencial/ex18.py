"""
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
"""

tamanho_arquivo = float(input('Informe o tamanho do arquivo em MB: '))
velocidade_internet = float(input('Informe a velocidade da sua internet em Mbps: '))

tempo = tamanho_arquivo / (velocidade_internet / 8) / 60  # Pegando quantos minutos de download serao

if tempo >= 1:  # Se for maior que zero, ou seja, se for 1 minuto ou mais.
    print('\n\n\t\tResultado do calculo\n\n'
          f'Tamanho do arquivo: {tamanho_arquivo:.1f}MB\n'
          f'Velocidade da internet: {velocidade_internet:.1f}Mbps\n'
          f'Tempo de download: {int(tempo)} minutos')

else:  # Se o tempo de download nao chega a ser 1 minuto.
    tempo = tamanho_arquivo / (velocidade_internet / 8)
    print('\n\n\t\tResultado do calculo\n\n'
          f'Tamanho do arquivo: {tamanho_arquivo:.1f}MB\n'
          f'Velocidade da internet: {velocidade_internet:.1f}Mbps\n'
          f'Tempo de download: {int(tempo)} segundos')
