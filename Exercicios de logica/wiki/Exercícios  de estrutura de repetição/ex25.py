"""
Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma
varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média
calculada.
"""

idades = []  # Lista onde ficara as idades informadas
contador = 1  # Contador para informar quantas idades ja foram informadas

print('\n\n\t\t\033[;37mDigite [ 0 ] para encerrar o programa\033[m\n')

while True:  # Enquanto o usuario nao digitar 0
    try:
        idade = int(input(f'Informe a idade da {contador}º pessoa\nIdade: '))

    except:
        print('\n\n\t\t[\033[;31mERRO\033[m]: Por favor, informe a idade corretamente.\n\n')

    else:
        if idade == 0:
            break

        idades.append(idade)
        contador += 1

media_das_idades = sum(idades) / len(idades)

print(f'\n\n\t\tA media das idades foi igual a [ {int(media_das_idades)} ]\n'
      f'Conforme a media calculada, esta turma é considerada [ ', end='')

if media_das_idades < 26:  # Se for uma turma considerada jovem
    print('Jovem ]')

elif 25 < media_das_idades < 61:  # Se for uma turma considerada adulta
    print('Adulta ]')

else:  # Se for uma turma considerada idosa
    print('Idosa ]')
